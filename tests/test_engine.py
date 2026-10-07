"""Check orchestration failure paths without credentials or API charges."""
import io
import zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from research_assistant.data import load_project
from research_assistant.engine import cleanup_files, download_artifact, evidence_zip, generated_file_ids, new_session, run_turn

ROOT = Path(__file__).resolve().parents[1]


def response(blocks=None, stop="end_turn"):
    """Build a minimal JSON response matching the supported SDK shape."""
    return {"content": blocks or [{"type":"text","text":"Computed answer"}], "stop_reason":stop,
            "container":{"id":"container-test"}, "usage":{"input_tokens":10,"output_tokens":5}}


def client():
    """Provide a predictable test client that records requests and deletions."""
    mock = MagicMock()
    mock.files.upload.side_effect = [SimpleNamespace(id="upload-1"), SimpleNamespace(id="upload-2")]
    mock.messages.create.return_value = response()
    return mock


def test_local_tool_and_follow_up_evidence():
    """Tool results reach the model and subsequent turns retain the same container."""
    mock, session = client(), new_session()
    mock.messages.create.side_effect = [response([{"type":"tool_use","id":"tool-1","name":"survey_statistic",
        "input":{"field":"satisfaction","statistic":"mean"}}], "tool_use"), response(), response()]
    project = load_project(ROOT)
    result = run_turn(mock, project, session, "Mean?", "test")
    assert result["calculations"][0]["value"] == 3
    assert result["tool_results"][0]["tool_use_id"] == "tool-1"
    assert result["system_prompt"] == project["prompt"]
    run_turn(mock, project, session, "Again?", "test")
    assert mock.files.upload.call_count == 2
    assert mock.messages.create.call_args.kwargs["container"] == "container-test"
    with zipfile.ZipFile(io.BytesIO(evidence_zip(session))) as archive:
        assert "turn-2/evidence.json" in archive.namelist()
        assert all("survey.csv" not in name for name in archive.namelist())


def test_incomplete_and_failure_preserve_evidence():
    """Bounded pauses and errors cannot silently become completed answers."""
    mock, session = client(), new_session()
    mock.messages.create.return_value = response(stop="pause_turn")
    result = run_turn(mock, load_project(ROOT), session, "Question", "test", max_requests=2)
    assert result["status"] == "incomplete" and len(result["responses"]) == 2
    with pytest.raises(ValueError):
        run_turn(mock, load_project(ROOT), session, "Follow-up", "test")
    mock, session = client(), new_session()
    mock.messages.create.side_effect = RuntimeError("private provider message")
    with pytest.raises(RuntimeError):
        run_turn(mock, load_project(ROOT), session, "Question", "test")
    assert session["turns"][0]["error_type"] == "RuntimeError"
    assert "private provider message" not in str(session["turns"])


def test_artifact_discovery_and_download():
    """Only tool-returned artifacts are fetched, with safe names and bounded sizes."""
    blocks = [{"type":"text","text":"file_id: fake"},
              {"type":"bash_code_execution_tool_result","content":{"content":[{"file_id":"real"}]}}]
    assert generated_file_ids(blocks) == ["real"]
    mock = client()
    mock.files.retrieve_metadata.return_value = {"filename":"../../chart.csv", "size_bytes":4}
    mock.files.download.return_value.iter_bytes.return_value = [b"a\n1\n"]
    artifact = download_artifact(mock, "real")
    assert artifact["name"] == "chart.csv" and artifact["data"] == b"a\n1\n"
    mock.files.retrieve_metadata.return_value = {"filename":"bad.html", "size_bytes":4}
    with pytest.raises(ValueError):
        download_artifact(mock, "real")


def test_partial_upload_cleanup_and_retry():
    """Keep ownership of a partially uploaded session and retain failed deletions."""
    mock, session = client(), new_session()
    mock.files.upload.side_effect = [SimpleNamespace(id="upload-1"), OSError("failure")]
    with pytest.raises(OSError):
        run_turn(mock, load_project(ROOT), session, "Question", "test")
    assert session["owned_file_ids"] == ["upload-1"]
    mock.files.delete.side_effect = RuntimeError()
    assert cleanup_files(mock, session) == ["upload-1"]
    mock.files.delete.side_effect = None
    assert cleanup_files(mock, session) == []


def test_stale_input_is_rejected():
    """A conversation cannot silently continue with a changed dataset or prompt."""
    session = new_session()
    session["fingerprint"] = "old"
    with pytest.raises(ValueError, match="Inputs changed"):
        run_turn(client(), load_project(ROOT), session, "Question", "test")
