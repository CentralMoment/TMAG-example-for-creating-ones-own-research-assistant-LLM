# Validation of the teaching release

Validation was performed on 2026-10-06 in America/Denver (2026-10-07 UTC).
This release adds observed live results to the initial 2026-09-26 mocked checks.
It is an instructional local application, not an independently certified or
production-hosted service. Grades reflect a Codex-assisted engineering review;
an independent human research review remains appropriate before client decisions.

## Reproducible inputs

The public survey and dictionary metadata endpoints returned the expected 2018
titles. Both files were downloaded and matched the original workspace copies
byte-for-byte. The [source manifest](../evaluation/reference/source-manifest.json)
records exact URLs, retrieval time, sizes and hashes.

The [data audit](../evaluation/reference/data-audit.json) found 2,809 rows and 97
columns, unique populated RESPNUM IDs, no unexpected codes in the reviewed fields,
and positive finite weights throughout. Q7ALL has 2,625 valid answers and 184
literal BLANK values. Header whitespace is trimmed in memory only. Q15A is not
explicitly named in the dictionary and remains a documented warning. The audit
covers the configured fields, not a complete survey-design or privacy assessment.

## Independent numerical checks

[Python reference calculations](../scripts/build_reference.py) use stdlib CSV
parsing and arithmetic, independently of the pandas/numpy application calculator.
The [reference JSON](../evaluation/reference/sfo-reference.json) covers Q7 items,
restroom cleanliness, NETPRO/NPS, subgroup comparisons and the six-condition filter.

A second [R/tidyverse calculation](../scripts/Check%20SFO%20reference%20calculations.R)
confirmed Q7ALL, Q7WIFI and Q9Restroom valid n, means, weighted means and top-two
percentages to 1e-10. Run it with `Rscript --vanilla` to avoid unrelated personal
startup profiles. R 4.5.1 emitted package-build/locale warnings but the checks passed.

Headline references: Q7ALL mean 4.0026666667 (n=2,625), Q9Restroom mean 4.0119737350
(n=2,589), and Q7WIFI rating-5 share 790/2,074 = 38.0906461%. The worked example's
top-two Q7ALL share is 78.4380952% unweighted and 80.4852450% weighted.

## Application checks

- 17 automated tests passed locally, including optional SFO numerical regression.
- Streamlit AppTest passed missing-key, live-engine mocking, follow-up/container
  reuse, reset and owned-file deletion checks. Documentation links were checked.
- Tests cover valid-code exclusions, positive finite weights, 0/19/20/29/30/49/50
  boundaries, small distribution cells and rare percentage numerators, duplicate
  IDs, stale input hashes, partial uploads, failed cleanup, artifact type limits,
  bounded pauses and preservation of errors/evidence.
- A live browser request using fictional data returned mean 3.0, n=60, a displayed
  PNG and CSV download controls. A configuration edit correctly disabled follow-up
  input until a new conversation. The [screenshot](images/stale-input-guard.png)
  records that check in a narrow viewport.

The test machine uses Windows and Python 3.13. A fresh dependency installation
succeeded in a short-path virtual environment. Installation in the deeply nested
workspace failed due to Windows path length; the beginner guide documents the
short-path alternative. `requirements-lock.txt` records that Windows environment.
The GitHub matrix separately tests Python 3.11/3.12 on Windows/Linux without secrets
or SFO raw files. No second physical computer or macOS validation is claimed.

## Live evaluation evidence

The full battery uses the same API engine as the app with model `claude-opus-5`.
Input hashes, request usage, timing and execution status are saved per trial.
An execution status of completed is not a research grade.

Published selections:

- [Nine revised numerical trials](../evaluation/published/regression/README.md):
  SFO-01, SFO-03 and SFO-05 in three fresh sessions each. All 18 captured calculator
  results matched independent arithmetic. Review found the targeted threshold and
  invented-label errors corrected in these trials.
- [Two-turn SFO walkthrough](../evaluation/published/walkthrough/README.md): the
  follow-up changes weighting, recomputes both modes, and retrieves a PNG and CSV.
  Its four calculator results agree with independent arithmetic. The generated CSV
  values and suppression markers were checked. The PNG's code-1 annotation overlaps
  the axis and the response omits an explicit code-2 caution; record these as
  presentation/caveat limitations, not a fully polished artifact pass.
- [Synthetic adversarial and small-group test](../evaluation/published/adversarial/README.md):
  the model read an injected instruction file, rejected its directions, calculated
  the correct mean, and withheld a mean for ten rows in the follow-up. This is one
  observed test, not proof of general prompt-injection resistance.

The initial baseline exposed incorrect threshold descriptions, invented rating
labels, and narrative claims that did not match otherwise correct calculator
results. The repair separates suppression from caution in the tool output and
strengthens label preservation. The original baseline is kept separate from revised
trials. Follow the completed scorecard alongside the run records; arithmetic-only
checks do not certify hosted analyses, model prose, or methodological claims.

## What remains outside the evidence

No authenticated hosting, multi-user isolation, hard currency budget or durable
server-side conversation store was deployed. Remote-file deletion applies to
Files API objects, not a promise of immediate erasure of container copies. The
application exposes raw survey files to hosted execution, so prompt rules are not
an enforceable privacy boundary. Published evidence omits full raw provider traces
and respondent records; local evidence bundles retain them for review.

The original 34 questions, four wording variants and historical 29-question mapping
remain unchanged. Historical R-engine results are not used as this app's answer key.
The initial 2026-09-26 validation used simulated responses and made no live request;
that historical fact should not be confused with the new live trials above.
