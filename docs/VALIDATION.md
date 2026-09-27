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

## Question-battery publication checks

The published battery was checked for all 34 questions from the original notes
and all 29 historical runner prompts, including four wording variants absent
from the notes. The historical order matches the saved 2026-09-03_20-51-34 results.
The source notes are copied byte-for-byte. Stable IDs, category counts, scorecard
coverage, JSON structure, and relative documentation links were checked locally.
This validates completeness of the published materials, not the assistant's
answers. The new scorecard is intentionally NOT RUN throughout.
