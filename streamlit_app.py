"""Run locally with: python -m streamlit run streamlit_app.py."""

import json
import mimetypes
import os
from pathlib import Path

import anthropic
import streamlit as st
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")
st.set_page_config(page_title="My research assistant", layout="centered")

# Resolve every data path relative to this repository, not the terminal directory.
try:
    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8-sig"))
    prompt = (ROOT / config["prompt_file"]).read_text(encoding="utf-8-sig")
    paths = [ROOT / name for name in config["files"]]
    if not paths or any(not path.is_file() for path in paths):
        raise ValueError("One or more configured data files are missing.")
except (OSError, ValueError, KeyError) as exc:
    st.error(f"Check config.json and your files: {exc}")
    st.stop()

st.title(config["title"])
st.caption(config["description"])
st.info("Starting a chat uploads the configured files to Anthropic. API usage may incur charges.")
diagnostics = st.checkbox("Show code and execution results")
key = os.environ.get("ANTHROPIC_API_KEY", "")
model = os.environ.get("ANTHROPIC_MODEL", "claude-opus-5")
if not key or key == "replace_with_your_own_key":
    st.error("Create .env from .env.example and enter your API key. Then restart the app.")
    st.stop()

# State belongs to one browser session. Resetting a chat does not delete remote files.
for name, default in [("history", []), ("file_ids", []), ("container_id", None)]:
    if name not in st.session_state:
        st.session_state[name] = default
if st.button("Start a new conversation"):
    st.session_state.history = []
    st.session_state.container_id = None
    st.rerun()


def render(blocks):
    """Display prose and optionally the provider's raw code/result blocks."""
    for block in blocks:
        if block.type == "text":
            st.markdown(block.text)
        elif diagnostics:
            with st.expander(block.type):
                st.json(block.model_dump(mode="json"))


def ask(question):
    """Upload selected files once per session and request a computed answer."""
    client = anthropic.Anthropic(api_key=key)
    if not st.session_state.file_ids:
        uploaded = []
        try:
            for path in paths:
                mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
                with path.open("rb") as handle:
                    uploaded.append(client.files.upload(file=(path.name, handle, mime)).id)
        except Exception:
            # Best-effort cleanup if only some files uploaded successfully.
            for file_id in uploaded:
                try:
                    client.files.delete(file_id)
                except anthropic.APIError:
                    pass
            raise
        st.session_state.file_ids = uploaded

    content = [{"type": "text", "text": question}]
    if not st.session_state.history:
        content += [{"type": "container_upload", "file_id": fid}
                    for fid in st.session_state.file_ids]
    messages = st.session_state.history + [{"role": "user", "content": content}]
    container = st.session_state.container_id
    for attempt in range(3):
        kwargs = {"container": container} if container else {}
        response = client.messages.create(
            model=model, max_tokens=4096, system=prompt,
            tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
            messages=messages, **kwargs,
        )
        messages.append({"role": "assistant", "content": response.content})
        if response.container:
            container = response.container.id
        if response.stop_reason != "pause_turn":
            break
    st.session_state.history = messages
    st.session_state.container_id = container
    if response.stop_reason in ("pause_turn", "max_tokens"):
        st.warning("The response stopped before completion. Narrow the question or start a new conversation.")


for turn in st.session_state.history:
    with st.chat_message(turn["role"]):
        if turn["role"] == "user":
            st.write(next(b["text"] for b in turn["content"] if b["type"] == "text"))
        else:
            render(turn["content"])

question = st.chat_input("Try: Compute the mean satisfaction and report valid n.")
if question:
    with st.chat_message("user"):
        st.write(question)
    previous_length = len(st.session_state.history)
    with st.chat_message("assistant"):
        with st.spinner("Uploading files or computing an answer..."):
            try:
                ask(question)
            except (anthropic.APIError, OSError) as exc:
                st.error(f"Request failed ({type(exc).__name__}). Check your key, billing, model access, files, and connection.")
                st.stop()
        for turn in st.session_state.history[previous_length + 1:]:
            render(turn["content"])
