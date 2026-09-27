# Repeat the SFO example

This walkthrough reconstructs the approach visible in the source project's files.
It is not a transcript of every development conversation or a claim that the
initial design was implemented in exactly this order.

## 1. Define the research task

The original question was how to let someone query the 2018 San Francisco
International Airport customer survey conversationally: exact statistics,
comparisons, ambiguous concepts such as "happy," and evidence-based recommendations.
Define what your assistant should answer before choosing software.

## 2. Obtain the source data and dictionary

The source project's documented DataSF identifiers are:

- Survey: [2018 SFO Customer Survey, 3w8r-nuxp](https://data.sfgov.org/d/3w8r-nuxp)
- Dictionary: [wkh6-n369](https://data.sfgov.org/d/wkh6-n369)

Open the survey page and export the full dataset as CSV. Obtain the Excel data
dictionary from the dictionary page or its attachments. The portal may change;
these identifiers come from the source project and the downloads have not been
independently verified for this starter. If a link fails, search DataSF for the
exact survey title and year. Do not substitute a screening-checkpoint survey or
another year without updating the prompt and validating its definitions.

Save the files locally under these exact names:

```text
data/private/2018 SFO Customer Survey.csv
data/private/2018 SFO Customer Survey Data Dictionary.xlsx
```

If you have the original workspace, copy its two files from `Data/Raw/` instead.
Do not copy the entire workspace: it contains credentials, logs, and old environments.
Check the source's reuse terms yourself; this repository does not redistribute
the SFO files. Record the source URL and download date in your own research notes.

## 3. Inspect before asking the model to interpret

Open the dictionary and confirm field names match the CSV. Check the row count,
response scales, missing/N/A codes, weight field, and which fields are genuine text.
The original project's prompt describes 2,809 respondents and 97 columns. Treat
these as expectations to verify against your downloaded file, not permission to
ignore a mismatch. Confirm `Q15A` really contains useful free text in your copy.

Do not infer that every numeric code is a quantity. An airport rating code for
"not applicable" must not become part of an average. Distinguish percentages of
valid answers from percentages of all survey respondents. Inspect `WEIGHT` before
using population estimates, and report the unweighted n even when using weights.

## 4. Choose an architecture that fits the data

The existing project considered a vector retrieval system, a precomputed summary
in the prompt, and live calculation. Most of this survey consists of structured
fields, so the current implementation uses live Python calculations through Claude.
A summary cannot anticipate every subgroup query. Semantic text retrieval does
not by itself calculate reliable counts or means across every row.

The original workspace contains an optional precomputed summary JSON. This
tutorial deliberately needs only the raw data and dictionary. New numbers should
be computed from the raw data; the summary is not a required source of truth.

## 5. Switch this app to SFO

Stop the app, then run these commands from the repository folder:

```powershell
Copy-Item config.json config.practice.backup.json
Copy-Item config.sfo.json config.json
& '.\.venv\Scripts\python.exe' scripts/check_setup.py
& '.\.venv\Scripts\python.exe' -m streamlit run streamlit_app.py --server.address 127.0.0.1 --server.port 8787
```

Read `prompts/sfo.md`. It is adapted from the source app, with unsupported claims
about this being the latest available survey removed and methodology guessing
tightened. Review its small-sample rules and weighting defaults for your use case.
They are prompt instructions, not hard enforcement in Python.

## 6. Validate the research behavior

Ask for the overall satisfaction mean and the distribution of `Q7ART`; compare
the result with an independent calculation using the dictionary's valid codes.
Then ask a subgroup question not covered by a precomputed summary, such as the
wifi mean among visitors. Verify the visitor definition and exclusions.

Ask `What share of the sample is happy with SFO?` The assistant should state a
definition before calculation. Ask `What should SFO improve?` It should gather
evidence and separate findings from recommendations. Ask `How has this changed
since COVID?` It should explain the 2018-only scope. Ask for undefined customer
segments; it should request variables or a research objective.

Next, run the [full question battery](../evaluation/sfo-question-battery.md) using
the [running and grading instructions](06-running-the-question-battery.md). Save
the first answer, execution evidence, and independent reference for each case in
a copy of the scorecard. Passing the synthetic example does not validate the SFO
statistics. The [short checklist](04-evaluation-and-troubleshooting.md) adds
privacy and malicious-instruction checks.

## 7. Adapt the pattern

The transferable steps are: define questions → inspect data → document meanings
and limitations → select analysis tools → write research instructions → build the
interface → test against known answers → revise. [Customize your own assistant](03-customize-your-assistant.md).
