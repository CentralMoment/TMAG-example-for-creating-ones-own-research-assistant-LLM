# SFO evaluation scorecard

Copy this file into `output/evaluation/` before filling it in. Follow the running
guide in the repository at `docs/06-running-the-question-battery.md`. All rows are
initially NOT RUN; this template contains no model results.

## Run metadata

- Run ID / date / evaluator:
- Git commit / app version:
- Model ID (never API key) / settings:
- Prompt filename / SHA256:
- Config version / selected files:
- Dataset source / date / SHA256:
- Dictionary source / SHA256:
- Independent reference method / evidence location:
- Preselected definitions, weights, exclusions, and rounding tolerances:

## Baseline: original 34 questions

Outcome: answered / clarified / declined / capability gap / error.
Grade: PASS / PARTIAL / FAIL / BLOCKED / NOT RUN.

| ID | Category | Outcome | Grade | Reference / evidence path | Reason / follow-up |
|---|---|---|---|---|---|
| SFO-01 | Fact lookup | — | NOT RUN | — | — |
| SFO-02 | Fact lookup | — | NOT RUN | — | — |
| SFO-03 | Fact lookup | — | NOT RUN | — | — |
| SFO-04 | Fact lookup | — | NOT RUN | — | — |
| SFO-05 | Fact lookup | — | NOT RUN | — | — |
| SFO-06 | Judgment and synthesis | — | NOT RUN | — | — |
| SFO-07 | Judgment and synthesis | — | NOT RUN | — | — |
| SFO-08 | Judgment and synthesis | — | NOT RUN | — | — |
| SFO-09 | Hybrid: define, then compute | — | NOT RUN | — | — |
| SFO-10 | Hybrid: define, then compute | — | NOT RUN | — | — |
| SFO-11 | Hybrid: define, then compute | — | NOT RUN | — | — |
| SFO-12 | Comparative | — | NOT RUN | — | — |
| SFO-13 | Comparative | — | NOT RUN | — | — |
| SFO-14 | Comparative | — | NOT RUN | — | — |
| SFO-15 | Causal why | — | NOT RUN | — | — |
| SFO-16 | Causal why | — | NOT RUN | — | — |
| SFO-17 | Causal why | — | NOT RUN | — | — |
| SFO-18 | Out of scope | — | NOT RUN | — | — |
| SFO-19 | Out of scope | — | NOT RUN | — | — |
| SFO-20 | Out of scope | — | NOT RUN | — | — |
| SFO-21 | Out of scope | — | NOT RUN | — | — |
| SFO-22 | Exploratory | — | NOT RUN | — | — |
| SFO-23 | Exploratory | — | NOT RUN | — | — |
| SFO-24 | Exploratory | — | NOT RUN | — | — |
| SFO-25 | Metadata and methodology | — | NOT RUN | — | — |
| SFO-26 | Metadata and methodology | — | NOT RUN | — | — |
| SFO-27 | Metadata and methodology | — | NOT RUN | — | — |
| SFO-28 | Metadata and methodology | — | NOT RUN | — | — |
| SFO-29 | Segmentation and advanced analytics | — | NOT RUN | — | — |
| SFO-30 | Segmentation and advanced analytics | — | NOT RUN | — | — |
| SFO-31 | Segmentation and advanced analytics | — | NOT RUN | — | — |
| SFO-32 | Segmentation and advanced analytics | — | NOT RUN | — | — |
| SFO-33 | Download or display | — | NOT RUN | — | — |
| SFO-34 | Download or display | — | NOT RUN | — | — |

## Historical wording variants (separate from baseline)

| ID | Outcome | Grade | Reference / evidence path | Reason |
|---|---|---|---|---|
| HIST-01 | — | NOT RUN | — | — |
| HIST-02 | — | NOT RUN | — | — |
| HIST-03 | — | NOT RUN | — | — |
| HIST-04 | — | NOT RUN | — | — |

## Detailed evidence for each attempted question

Duplicate this block for each trial:

- Question ID / trial number / fresh session or follow-up:
- Exact question and any clarification supplied:
- Full answer location:
- Code and execution-output location:
- Independent expected result or required behavior:
- Actual result / n / denominator / weights / exclusions:
- Assumptions, sources, and uncertainty checked:
- Artifact path and delivery check, if requested:
- Outcome / grade / reason:
- Failure type / proposed correction:

## Repeat trials and follow-ups

Record trials 2 and 3 here or in separate evidence files. Keep their IDs distinct
from baseline rows. Record exact follow-up wording and inherited context.

## Summary

- Baseline: PASS __ / PARTIAL __ / FAIL __ / BLOCKED __ / NOT RUN __ (sum = 34)
- Historical variants: PASS __ / PARTIAL __ / FAIL __ / BLOCKED __ / NOT RUN __ (sum = 4)
- Repeat-trial agreement:
- Research-accuracy failures:
- Artifact-delivery gaps:
- Unresolved reference checks:
- Changes required and next run ID:
