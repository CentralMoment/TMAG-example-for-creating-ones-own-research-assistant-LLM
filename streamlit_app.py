"""Run locally with: python -m streamlit run streamlit_app.py."""
import os
from pathlib import Path

import anthropic
import streamlit as st
from dotenv import load_dotenv

from research_assistant.data import load_project
from research_assistant.engine import answer_text, cleanup_files, evidence_zip, new_session, run_turn

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")
st.set_page_config(page_title="My research assistant", layout="centered")
try:
    project = load_project(ROOT, os.environ.get("ASSISTANT_CONFIG", "config.json"))
except (OSError, ValueError, KeyError) as exc:
    st.error(f"Check configuration and data: {exc}")
    st.stop()
st.title(project["config"]["title"])
st.caption(project["config"]["description"])
st.info("Starting a chat uploads the configured files to Anthropic. API usage may incur charges.")
diagnostics = st.checkbox("Show code and execution results")
with st.expander("Data checks"):
    st.json(project["audit"])
key = os.environ.get("ANTHROPIC_API_KEY", "")
model = os.environ.get("ANTHROPIC_MODEL", "claude-opus-5")
if not key or key == "replace_with_your_own_key":
    st.error("Create .env from .env.example and enter your API key. Then restart the app.")
    st.stop()
client = anthropic.Anthropic(api_key=key, timeout=180.0, max_retries=1)
if "research_session" not in st.session_state:
    st.session_state.research_session = new_session()
session = st.session_state.research_session
if st.button("Start a new conversation"):
    # Keep ownership so old uploads can still be explicitly deleted in this browser session.
    owned = session["owned_file_ids"]
    st.session_state.research_session = new_session()
    st.session_state.research_session["owned_file_ids"] = owned
    st.rerun()
if st.button("Delete this session's remote files"):
    failures = cleanup_files(client, session)
    if failures:
        st.warning(f"{len(failures)} deletions failed. Retry before closing this browser session.")
    else:
        st.success("Files API deletion completed. Container copies follow provider retention. Start a new conversation.")
if session["turns"]:
    st.download_button("Download conversation evidence", evidence_zip(session),
                       "research-evidence.zip", "application/zip")
    st.caption("Evidence may contain respondent information and provider identifiers. Review before sharing.")
for turn in session["turns"]:
    with st.chat_message("user"):
        st.write(turn["question"])
    with st.chat_message("assistant"):
        st.markdown(answer_text(turn))
        st.caption(f"{turn['status']} · {turn['elapsed_seconds']:.1f}s · {turn['model']}")
        if turn["calculations"]:
            with st.expander("Calculator results — compare with the answer"):
                st.caption("These are fixed-code results. The model's wording still needs review.")
                for calculation in turn["calculations"]:
                    st.json(calculation)
        if turn["status"] != "completed":
            st.warning("This turn did not complete. Inspect evidence and start a new conversation.")
        for index, artifact in enumerate(turn["artifacts"]):
            if artifact["mime"] in ("image/png", "image/jpeg"):
                st.image(artifact["data"], caption=artifact["name"])
            st.download_button(f"Download {artifact['name']}", artifact["data"], artifact["name"],
                               artifact["mime"], key=f"{turn['id']}-{index}")
        for error in turn["artifact_errors"]:
            st.warning(error)
        if diagnostics:
            with st.expander("Execution evidence"):
                st.json({k: v for k, v in turn.items() if k != "artifacts"})
changed = session.get("fingerprint", project["fingerprint"]) != project["fingerprint"]
if changed:
    st.warning("Inputs changed. Start a new conversation before asking another question.")
question = st.chat_input("Ask a question about this survey", disabled=session["incomplete"] or changed)
if question:
    with st.spinner("Computing and collecting evidence..."):
        try:
            run_turn(client, project, session, question, model)
        except Exception as exc:
            st.error(f"Request failed ({type(exc).__name__}). Evidence is preserved; start a new conversation.")
    st.rerun()
