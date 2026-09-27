# Initial validation — 2026-09-26

Local validation uses the source project's existing Windows Python environment
with anthropic 1.3.0, streamlit 1.63.0, and python-dotenv 1.2.3.

- Local configuration and selected example files checked.
- Synthetic reference values checked: n=60, mean=3.0, satisfied count=24.
- Python source syntax and relative documentation links checked.
- Streamlit interface checked with simulated API responses: missing key,
  first question, follow-up, file/container reuse, and conversation reset.

Run the local checks from the repository root:

```powershell
& '.\.venv\Scripts\python.exe' scripts/check_setup.py
& '.\.venv\Scripts\python.exe' scripts/test_app.py
```

No paid/live Claude API request was made. These checks do not validate model
availability, billing, hosted execution, remote file retention, or the model's
research accuracy. A clean installation on another computer, other operating
systems, SFO downloads, and production hosting have not been tested. Complete
the manual question checks before relying on this assistant.
