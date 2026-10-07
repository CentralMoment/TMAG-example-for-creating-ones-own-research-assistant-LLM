"""Shared API orchestration, artifact retrieval, and evidence capture."""

import hashlib
import io
import json
import mimetypes
import re
import time
import uuid
import zipfile
from datetime import datetime, timezone
from importlib.metadata import version

from .statistics import calculate, tool_definition

MAX_REQUESTS = 6
MAX_ARTIFACT_BYTES = 20 * 1024 * 1024
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "csv", "json", "txt", "pdf", "xlsx"}


def new_session():
    """Create independent conversation and remote-file ownership state."""
    return {"history": [], "file_ids": [], "container_id": None, "turns": [],
            "owned_file_ids": [], "incomplete": False}


def plain(value):
    """Convert SDK response objects to portable JSON values."""
    return value.model_dump(mode="json") if hasattr(value, "model_dump") else value


def generated_file_ids(blocks):
    """Find artifact IDs only inside server-tool results, never user/model text."""
    found = []

    def visit(value):
        """Walk nested result blocks without interpreting their contents as commands."""
        if isinstance(value, dict):
            if isinstance(value.get("file_id"), str):
                found.append(value["file_id"])
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    for block in blocks:
        if block.get("type", "").endswith("tool_result"):
            visit(block)
    return list(dict.fromkeys(found))


def download_artifact(client, file_id):
    """Download a bounded artifact with a safe basename, without executing it."""
    metadata = plain(client.files.retrieve_metadata(file_id))
    basename = re.split(r"[/\\]", metadata["filename"])[-1]
    basename = re.sub(r"[^A-Za-z0-9._ -]", "_", basename).strip(" .") or "artifact"
    extension = basename.rsplit(".", 1)[-1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError("Artifact type is not supported for download.")
    if metadata.get("size_bytes", 0) > MAX_ARTIFACT_BYTES:
        raise ValueError("Artifact exceeds the 20 MiB download limit.")
    data = bytearray()
    response = client.files.download(file_id)
    try:
        for chunk in response.iter_bytes():
            data.extend(chunk)
            if len(data) > MAX_ARTIFACT_BYTES:
                raise ValueError("Artifact exceeds the 20 MiB download limit.")
    finally:
        response.close()
    return {"name": basename, "mime": mimetypes.guess_type(basename)[0] or "application/octet-stream",
            "sha256": hashlib.sha256(data).hexdigest(), "size_bytes": len(data), "data": bytes(data)}


def cleanup_files(client, session):
    """Delete only files owned by this session, retaining failed IDs for retry."""
    failed = []
    for file_id in list(dict.fromkeys(session["owned_file_ids"])):
        try:
            client.files.delete(file_id)
        except Exception:
            failed.append(file_id)
    session["owned_file_ids"] = failed
    session["file_ids"] = [fid for fid in session["file_ids"] if fid in failed]
    # Containers may hold copies; a Files API deletion is not a container-erasure guarantee.
    session["container_id"] = None
    session["incomplete"] = True
    return failed


def run_turn(client, project, session, question, model, max_requests=MAX_REQUESTS):
    """Run a bounded turn; capture all requests and local-tool results for later review."""
    if session["incomplete"]:
        raise ValueError("Start a new conversation after an incomplete or failed turn.")
    if session.get("fingerprint", project["fingerprint"]) != project["fingerprint"]:
        raise ValueError("Inputs changed. Start a new session before uploading the new files.")
    session["fingerprint"] = project["fingerprint"]
    started = time.monotonic()
    record = {"id": str(uuid.uuid4()), "started_utc": datetime.now(timezone.utc).isoformat(),
              "question": question, "model": model, "hashes": project["hashes"],
              "system_prompt": project["prompt"], "tool_results": [],
              "fingerprint": project["fingerprint"], "responses": [], "calculations": [],
              "artifacts": [], "artifact_errors": [], "status": "running", "usage": {},
              "max_requests": max_requests, "max_tokens_per_request": 8192,
              "packages": {name: version(name) for name in ("anthropic", "streamlit", "pandas")}}
    session["turns"].append(record)
    try:
        if not session["file_ids"]:
            uploaded = []
            for path in project["paths"]:
                with path.open("rb") as handle:
                    uploaded.append(client.files.upload(file=(path.name, handle,
                        mimetypes.guess_type(path.name)[0] or "application/octet-stream")).id)
                session["owned_file_ids"].append(uploaded[-1])
            session["file_ids"] = uploaded
        content = [{"type": "text", "text": question}]
        if not session["history"]:
            content += [{"type": "container_upload", "file_id": fid} for fid in session["file_ids"]]
        messages = list(session["history"]) + [{"role": "user", "content": content}]
        for _ in range(max_requests):
            kwargs = {"container": session["container_id"]} if session["container_id"] else {}
            response = plain(client.messages.create(
                model=model, max_tokens=8192, system=project["prompt"],
                tools=[{"type": "code_execution_20260521", "name": "code_execution"},
                       tool_definition(project["profile"])], messages=messages, **kwargs))
            record["responses"].append(response)
            for name, count in response.get("usage", {}).items():
                if isinstance(count, (int, float)):
                    record["usage"][name] = record["usage"].get(name, 0) + count
            if response.get("container"):
                session["container_id"] = response["container"]["id"]
            blocks = response["content"]
            messages.append({"role": "assistant", "content": blocks})
            for file_id in generated_file_ids(blocks):
                if file_id in session["owned_file_ids"]:
                    continue
                session["owned_file_ids"].append(file_id)
                try:
                    record["artifacts"].append(download_artifact(client, file_id))
                except Exception as exc:
                    record["artifact_errors"].append(type(exc).__name__ + ": artifact download failed")
            results = []
            for block in blocks:
                if block.get("type") != "tool_use":
                    continue
                try:
                    if block["name"] != "survey_statistic":
                        raise ValueError("Unknown client tool.")
                    result = calculate(project["data"], project["profile"], **block["input"])
                    record["calculations"].append(result)
                    results.append({"type": "tool_result", "tool_use_id": block["id"],
                                    "content": json.dumps(result)})
                except (ValueError, KeyError, TypeError) as exc:
                    results.append({"type": "tool_result", "tool_use_id": block["id"],
                                    "content": str(exc), "is_error": True})
            if results:
                record["tool_results"].extend(results)
                messages.append({"role": "user", "content": results})
            stop = response["stop_reason"]
            if stop == "end_turn" and not results:
                record["status"] = "completed"
                break
            if stop not in ("pause_turn", "tool_use"):
                break
        if record["status"] != "completed":
            record["status"] = "incomplete"
            session["incomplete"] = True
        session["history"] = messages
    except Exception as exc:
        record.update(status="error", error_type=type(exc).__name__)
        session["incomplete"] = True
        raise
    finally:
        record["elapsed_seconds"] = round(time.monotonic() - started, 3)
    return record


def answer_text(record):
    """Collect visible model prose, preserving intermediate explanations."""
    return "\n\n".join(block["text"] for response in record["responses"]
                        for block in response["content"] if block.get("type") == "text")


def evidence_zip(session):
    """Export a local audit bundle; never include API keys or original uploaded files."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for index, turn in enumerate(session["turns"], 1):
            record = {key: value for key, value in turn.items() if key != "artifacts"}
            record["artifacts"] = [{key: value for key, value in artifact.items() if key != "data"}
                                   for artifact in turn["artifacts"]]
            archive.writestr(f"turn-{index}/evidence.json", json.dumps(record, indent=2))
            archive.writestr(f"turn-{index}/answer.md", answer_text(turn))
            for number, artifact in enumerate(turn["artifacts"], 1):
                archive.writestr(f"turn-{index}/artifacts/{number}-{artifact['name']}", artifact["data"])
        archive.writestr("README.txt", "Local research evidence. May contain respondent information, comments, "
                         "generated code, and provider identifiers in tool outputs. Review before sharing. "
                         "Calculator results validate only their own computations, not all model prose.")
    return buffer.getvalue()
