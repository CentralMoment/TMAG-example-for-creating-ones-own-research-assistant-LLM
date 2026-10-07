# Use the full question battery to evaluate your assistant

The battery is a set of research tasks and behavioral checks. It tests whether
the assistant can calculate, interpret, clarify, explore, and recognize the
limits of its evidence. A plausible answer is not enough: examine how it arrived
at the answer and whether it actually completed the requested task.

## Choose the right question set

| Resource | What it contains |
|---|---|
| [Full battery with review criteria](../evaluation/sfo-question-battery.md) | All 34 original questions in 10 categories, plus four historical wording variants |
| [Original question notes](../evaluation/source/original-question-notes.txt) | The original question file, unchanged, including Brent's explanations |
| [Machine-readable battery](../evaluation/sfo-question-battery.json) | Stable IDs, exact question text after quote cleanup, category criteria, and provenance |
| [Historical run mapping](../evaluation/historical-question-map.md) | All 29 questions from the earlier runner, in their original order, mapped to battery IDs |
| [Blank scorecard](../evaluation/scorecard-template.md) | A result row for every original question and historical variant |

The main suite is **SFO-01 through SFO-34**. **HIST-01 through HIST-04** retain
wording found only in the old runner. Together these are 38 distinct prompts;
the historical 29 are a mapped selection, not 29 additional unique tests.
The old runner's question text was checked against its saved 2026-09-03 run.
Historical answers and grades are not an answer key for the current app.

## 1. Finish the practice example first

Run the fictional-data checks in the [beginner guide](01-beginner-guide.md).
They establish that the app can start and that you know how to inspect execution.
They do not validate answers about SFO. Before running this battery, follow
[the SFO setup](02-reproduce-sfo.md), select `config.sfo.json` as `config.json`,
and confirm that the app uses the actual SFO CSV and dictionary.

Do not attach the battery, scorecard, historical results, or reference answers
as research data in `config.json`. Enter each test as a question. Keep grading
criteria and independently computed answers outside the assistant's input files.
Otherwise it may repeat expected answers instead of deriving them from the data.

## 2. Create a local run record

From PowerShell in the repository folder:

```powershell
New-Item -ItemType Directory -Force output/evaluation
Copy-Item evaluation/scorecard-template.md output/evaluation/my-first-sfo-run.md
```

Give each later run a new filename so you preserve comparisons. `output/` is
excluded from Git. Fill in the date, evaluator, Git commit (`git rev-parse HEAD`),
model identifier from `.env` (never the key), prompt/config versions, and data
source/version. To record input hashes, run:

```powershell
Get-FileHash 'data/private/2018 SFO Customer Survey.csv' -Algorithm SHA256
Get-FileHash 'data/private/2018 SFO Customer Survey Data Dictionary.xlsx' -Algorithm SHA256
Get-FileHash prompts/sfo.md -Algorithm SHA256
```

Record any generation-setting changes and the app's continuation limit. Keep
relevant screenshots, answer text, and diagnostic output alongside the scorecard.
Do not put credentials or private transcripts into public issues or commits.

## 3. Prepare independent reference checks

For questions with numerical answers, calculate a reference in R, Python, or a
spreadsheet before grading. Verify field names and codes in the dictionary.
Record filters, valid-answer rules, missing codes, weighting, and the denominator.
For each subgroup, preserve the unweighted n and any weight exclusions.

Do not treat an old model response as an independent reference. The old report
itself illustrates why review matters: its weighted-distribution case lists base
n=2,625 in metadata but says 2,619 passenger responses in the prose. Whatever
the source of that discrepancy, it must be reconciled against the source data,
not copied into a new expected-answer sheet.

Choose tolerances before looking at the new answer. Counts should match exactly.
For a mean displayed to two decimals, compare the rounded reference; for a
percentage to one decimal, compare its rounding to the same precision. A weighting
or denominator mismatch is not a rounding difference. If the question is ambiguous,
record a preapproved definition or score its explicit assumption and recompute
your reference under that definition. Do not silently change the rubric to fit.

## 4. Run one question at a time

The shared live runner automates capture and cleanup. It makes paid API calls with
your configured key. Set provider spending controls first. From the repo root:

```powershell
& '.\.venv\Scripts\python.exe' scripts/run_battery.py
& '.\.venv\Scripts\python.exe' scripts/run_battery.py --ids SFO-01 SFO-03 SFO-05 --repeat 3
& '.\.venv\Scripts\python.exe' scripts/run_battery.py --ids HIST-01 HIST-02 HIST-03 HIST-04
```

Each command creates a distinct directory under `output/evaluation/`. The runner
uses the same engine, configuration, profile and prompts as Streamlit. It records
execution status separately from the unassigned research grade. Inspect each ZIP
and answer before grading. It stops after a service or remote-cleanup failure,
preserving the failure and owned IDs locally. Review raw bundles before publishing.

Run `scripts/build_reference.py` for independent numerical references. Its stdlib
CSV and arithmetic implementation does not import the application's calculator.
Keep this answer key outside the assistant's uploads. For UI evaluation:

1. Launch the SFO app and enable **Show code and execution results**.
2. Click **Start a new conversation** before each independent test.
3. Copy the question exactly from the full battery and send it alone.
4. Save the first answer and diagnostic evidence under its stable question ID.
5. Compare it with the category criteria and your independent reference.
6. Record the outcome, grade, reason, and evidence location in the scorecard.

Keep the prompt and data fixed during a baseline run. If an answer is wrong,
capture it before coaching the assistant; a corrected follow-up is a different
trial. Restart the app after changing the prompt, files, or configuration.

Some questions intentionally require clarification. For example, **SFO-29** and
**SFO-30** leave segmentation inputs open. An appropriate clarifying question can
pass the first-turn test. If you answer it, preserve that response and the exact
follow-up as a separate continuation test. For **SFO-31**, review how it resolves
the Q7 variables, missing values, scaling, algorithm, and seed before interpreting
clusters. A fixed seed alone does not fix all analytic choices.

For **SFO-32**, ensure it actually crosses trip purpose with residency, instead
of reporting two unrelated one-way tables. For exploratory questions, inspect
whether it examined several possibilities before choosing a finding; a generic
"interesting" narrative is not evidence of exploration.

## 5. Score behavior and task completion separately

First label the **outcome**: answered, clarified, declined, capability gap, or
error. Then assign a **grade**:

| Grade | Meaning |
|---|---|
| PASS | Meets the question's requirements, supported by the saved evidence |
| PARTIAL | A useful, supported response misses part of the requested task; explain what |
| FAIL | Incorrect result, unsupported claim, inappropriate refusal, policy failure, or required output not delivered |
| BLOCKED | An external problem, such as billing or missing source files, prevented evaluation |
| NOT RUN | No attempt yet |

Correctly declining an unsupported forecast can be PASS. Clarifying an unscoped
clustering question can be PASS. Refusing an ordinary computable mean is not
automatically PASS just because the refusal sounds cautious. Mark numerical
claims awaiting independent verification as PARTIAL with "verification pending",
rather than calling them correct.

Check both the number and its explanation. Look for source fields, exclusions,
denominator, weight choice, unweighted n, and justified uncertainty. "Meaningful"
differences require an explicit interpretation; different sample means alone do
not establish statistical significance or practical importance. Recommendations
should separate computed evidence from judgment. Methodology absent from the
provided sources must be acknowledged, not invented.

The current prompt's subgroup rules are: n<20 permits a count only; n<30 needs
a strong caveat; n<50 needs small-sample caution. These are project conventions,
not universal statistical guarantees. Check every reported cell, not just total n.

## 6. Treat files and charts as real acceptance tests

**SFO-02**, **SFO-33**, and **SFO-34** request a plot, downloadable CSV, or chart.
The app retrieves generated files, displays PNG/JPEG charts and offers downloads.
Keep these tests in the suite to verify delivery. Saying "I created a chart" is
not delivery of a chart.

If the requested artifact is missing, record a capability gap and FAIL for
artifact delivery (or PARTIAL for an otherwise useful answer, with the failed
delivery criterion explicit). Do not present these cases as fully passed. They
can become regression tests when artifact support is implemented.

For the CSV filter, verify the condition is **all six measures** at the lowest
valid rating (logical AND), not any one measure (OR). A correct empty result is
possible. Review the research/privacy policy before any row-level export; a
policy-based refusal may be appropriate if that policy forbids it, but it does
not demonstrate export capability. For charts, check labels, group definitions,
counts/percentages, weighting, and small cells against the computed table.

## 7. Repeat and summarize

After the 34-question baseline, repeat numerical cases in three fresh
conversations in total, holding analytic definitions fixed. Use the four HIST
variants to check sensitivity to wording. Equivalent questions should agree
under the same definitions, but exploratory narratives need not be identical.
Add a separate follow-up session to test whether the app correctly updates
filters or switches weighting without reusing stale results.

Report all five grade counts out of 34, then report the four historical variants
and repeat trials separately. Include BLOCKED and NOT RUN counts; do not shrink
the denominator to hide missing tests. Distinguish research accuracy from output
delivery and unsupported capabilities. A single overall percentage can conceal
a serious failure in a small but important category.

## 8. Improve and rerun

Classify each failure: data/dictionary, prompt, computation, interpretation,
interface, or infrastructure. Make the smallest relevant correction. Rerun failed
cases and nearby cases that could regress, then run the full suite before sharing
a revised release. Save a new run record with the new commit and prompt hashes.
Never overwrite the original failing evidence.

For your own assistant, keep the ten categories but replace SFO-specific wording
and definitions with your research context. Add questions from real users and
boundary cases for your sources. The [short checklist](04-evaluation-and-troubleshooting.md)
also includes privacy and malicious-instruction checks that supplement, rather
than replace, Brent's original battery.

## Historical scope and current status

The older 29-question run evaluated an R planner/policy-gate/DuckDB pipeline on
2026-09-03. Its runner depends on the retired engine and is not an automated
test command for this Streamlit app. The current repository provides a separate
shared-engine live runner, independent references and results linked from
[validation](VALIDATION.md). The blank scorecard remains NOT RUN so readers do not
mistake the template for their own results.
