# Your first working assistant

## 1. Understand the pieces

Python runs the app. Streamlit makes its browser interface. An API is the service
the app calls to ask Claude a question. Your API key identifies your account and
must remain secret. A system prompt supplies standing research instructions.
A data dictionary explains the columns, codes, and missing values in your data.
Git tracks file changes; GitHub stores a shared copy of the project.

You need internet access, a computer on which you can install Python, an Anthropic
API account with billing and access to a code-execution-compatible model, and
permission to send your selected research files to that service.

## 2. Get the project

On the repository's GitHub page, click **Code → Download ZIP**. Extract the ZIP
to a folder you can find, such as `Documents/research-assistant`. Do not run from
inside the ZIP. A private repository requires an invitation and GitHub sign-in.

Alternatively, if Git is installed:

```powershell
git clone https://github.com/CentralMoment/TMAG-example-for-creating-ones-own-research-assistant-LLM.git
cd TMAG-example-for-creating-ones-own-research-assistant-LLM
```

## 3. Install Python and open a terminal

Install Python 3.11 or 3.12 from [python.org](https://www.python.org/downloads/).
On Windows, enable the installer's PATH option if offered. Reopen the terminal
after installation. In File Explorer, open your extracted project folder,
right-click an empty area, and choose **Open in Terminal**. Use PowerShell.

Type the following and press Enter after each line:

```powershell
python --version
Get-ChildItem
```

You should see a Python version and files including `streamlit_app.py`,
`requirements.txt`, and `config.json`. If not, change to the correct folder.
If `python` opens the Microsoft Store, use `py -3.12` instead of `python` in
the environment-creation command below, or fix your Python installation.

## 4. Create an isolated environment

A virtual environment keeps this project's packages separate from other projects.
These commands intentionally use its Python executable directly; activation and
PowerShell execution-policy changes are unnecessary.

```powershell
python -m venv .venv
& '.\.venv\Scripts\python.exe' -m pip install -r requirements.txt
& '.\.venv\Scripts\python.exe' scripts/check_setup.py
```

The final command should print `PASS`. It checks local files and the known
practice answers without uploading data or spending API credits.

On macOS/Linux, use `python3 -m venv .venv`, then `.venv/bin/python` in place of
`& '.\.venv\Scripts\python.exe'`. Use `cp` instead of `Copy-Item` below.
Windows is the source project's platform; the other platforms are not validated here.

## 5. Configure your own API key

Use [Anthropic's API console](https://platform.claude.com/) to obtain an API key
and configure billing/spending controls. Consult its current account instructions.
Do not paste the key into GitHub, the chat box, or a public support request.

```powershell
Copy-Item .env.example .env
notepad .env
```

Replace `replace_with_your_own_key` with your key and save. Keep the variable name
`ANTHROPIC_API_KEY` unchanged. Confirm the filename is `.env`, not `.env.txt`.
The model setting starts with `claude-opus-5`, matching the source project;
replace it with an accessible model that supports code execution if needed.
See the provider's [compatibility guidance](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool).
Restart the app whenever you edit `.env`.

## 6. Launch the app

```powershell
& '.\.venv\Scripts\python.exe' -m streamlit run streamlit_app.py --server.address 127.0.0.1 --server.port 8787
```

Keep this terminal open. Visit <http://127.0.0.1:8787> in your browser if it does
not open automatically. You should see **My research assistant — practice survey**.
The first question uploads the two configured fictional data files; later
questions in the same browser session reuse their file IDs and execution container.

## 7. Ask questions with known answers

Enable **Show code and execution results**. Ask one question at a time:

1. `Read the dictionary. Compute the number of rows and mean satisfaction.`
2. `What percentage of respondents are satisfied? State your definition and n.`
3. `Compare satisfaction in groups A and B. Include subgroup sample sizes.`
4. `Has satisfaction improved since last year?`

Expected: 60 rows, mean 3.0; 40% satisfied using ratings 4–5 (24 of 60);
both groups have n=30 and mean 3.0, with small-sample caution; the last question
should explain that a single wave cannot establish a trend. Confirm the diagnostics
show actual execution. A correct-looking answer alone does not establish that.

## 8. Stop and restart

Press Ctrl+C in the terminal to stop. To restart, open the project folder and
repeat the launch command. **Start a new conversation** clears chat history and
the execution-container reference; it does not delete files uploaded to Anthropic.
Refreshing/closing the browser may also reset session state. This app has no
saved chat history. Use the provider's file-management API for remote deletion;
see [Files API documentation](https://platform.claude.com/docs/en/build-with-claude/files).

Next: [reproduce SFO](02-reproduce-sfo.md) or [use your own data](03-customize-your-assistant.md).
