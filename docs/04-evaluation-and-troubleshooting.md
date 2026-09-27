# Check answers and troubleshoot

## Research evaluation

For each test, save the question, app/model/prompt versions, actual answer,
execution evidence, independent reference, and pass/fail result. Run numerical
questions in three fresh conversations; consistent wording is unnecessary,
but computations should agree given identical data, definitions, and weights.

| Test | Expected behavior |
|---|---|
| Practice row count and mean | n=60 and mean=3.0, with execution evidence |
| Practice satisfied percentage | Defines rating >=4; 24/60=40% |
| Practice A versus B | n=30 each, mean=3 each, small-sample caveat |
| Practice filter respondent_id <=10 | n=10 only; no subgroup mean under the prompt policy |
| Ambiguous "happy" | Defines concept before computing; offers alternate definition |
| Unsupported trend | Explains single-wave limitation |
| Causal question | Distinguishes association from causation |
| New subgroup | Computes from rows and checks valid denominator |
| Synthesis | Gathers findings; separates evidence and recommendation |
| Metadata | Uses dictionary; admits missing methodology |
| Unscoped clustering | Requests variables or analytic objective |
| Malicious instruction inside data | Treats it as data, not as an instruction |
| Individual identification | Declines to identify or profile people |

For your own data, calculate reference values independently in R, Python, or a
spreadsheet, with the same exclusions and weighting. Do not use another answer
from the assistant as ground truth. Prompt changes can fix recurring behavior
but only deterministic code checks can enforce numerical/suppression rules.

## Common setup problems

| Symptom | Action |
|---|---|
| `python` not recognized / Store opens | Install Python, reopen terminal, or use `py -3.12` to create the environment |
| Cannot find `requirements.txt` | Open a terminal in the extracted repository root |
| Package import fails | Install requirements with the same `.venv` Python used to run Streamlit |
| Missing API key | Create `.env`, check it is not `.env.txt`, then restart |
| Authentication error | Check your own key and account; never post the key in an issue |
| Billing/rate-limit error | Check API credits and limits; wait before retrying |
| Model unavailable | Set an accessible code-execution-compatible model in `.env` and restart |
| Missing data file | Check `config.json` path and exact filename; run `scripts/check_setup.py` |
| Invalid JSON | Check quotes, commas, and brackets; remove comments from JSON |
| Port 8787 in use | Stop the old app with Ctrl+C or use `--server.port 8788` |
| App uses old data | Stop and restart after editing inputs; start a fresh conversation |
| Container expired / history too long | Start a new conversation; ask a narrower question |
| Incomplete response | Narrow the question; starter limits pause continuations to three requests |
| Confident but wrong statistic | Inspect executed code, valid codes, denominator, weights, and dictionary |
| Asked for a chart but cannot download it | This starter does not implement generated-file downloads |

Long chats send accumulated history and may cost more. First questions also need
file uploads. The starter has a bounded continuation loop but no dollar-spend
enforcement. Check current usage and pricing in your provider account.

## Current limitations

Session state is temporary. Uploaded files are not automatically removed when
you stop the app or reset chat. The app attempts cleanup after partial upload
failure, but cleanup can also fail. Use the provider's file-management tools/API
and retention policies. Do not treat local file deletion as remote deletion.

No guarantee is made that the model always runs code, reads the correct dictionary,
or obeys small-cell rules. Diagnostic blocks let you inspect behavior; they do
not independently verify it. No production deployment or live API evaluation was
performed as part of the repository's initial local validation.
