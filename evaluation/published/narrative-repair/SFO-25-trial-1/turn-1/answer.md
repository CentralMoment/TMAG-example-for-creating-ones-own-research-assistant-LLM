I'll read the data dictionary and inspect the structural fields in the CSV.

[Computed + Metadata lookup] — field definitions below come from the data dictionary's "Code List" sheet; the counts come from model-written hosted code over the CSV (97 columns, 2,809 rows), and are subject to independent review. `survey_statistic` does not cover these administrative fields.

## What the files document about method

**Mode of collection (METH — "Method of collecting"), all 2,809 rows:**

| METH | Label (dictionary) | n | % of 2,809 |
|---|---|---|---|
| 1 | At gate | 2,779 | 98.9% |
| 2 | Mail-in | 25 | 0.9% |
| 3 | Online | 5 | count only — suppressed (n<20) |

This is overwhelmingly an **intercept survey of departing passengers at the boarding gate**, with a very small mail-in and online tail. The mail-in cell (n=25) is itself too small for a reliable summary.

**Administration (SAQ — "Survey Administration"):**

| SAQ | Label | n | % |
|---|---|---|---|
| 1 | Interviewer Administered | 336 | 12.0% |
| 2 | Self Administered | 2,473 | 88.0% |

So most respondents filled out the questionnaire themselves at the gate; about one in eight was walked through it by an interviewer.

**Languages offered (LANG — "Language of questionaire"):**

| LANG | Label | n | % |
|---|---|---|---|
| 1 | English | 2,639 | 93.9% |
| 2 | Spanish | 72 | 2.6% |
| 3 | Chinese | 75 | 2.7% |
| 4 | Japanese | 23 | 0.8% |

Four-language instrument. The Japanese cell (n=23) is small enough that any statistic broken out by it would need a strong caveat.

**Sampling structure.** The dictionary defines a stratified gate-based design:
- `STRATA` — departure time band: 1 = AM (before 11am) n=679 (24.2%); 2 = MID (11am–5pm) n=1,035 (36.8%); 3 = PM (after 5pm) n=1,095 (39.0%)
- `PEAK` — 1 = Domestic peak (dep. 8am–1pm) n=600 (21.4%); 2 = Domestic offpeak n=1,154 (41.1%); 3 = International n=1,055 (37.6%)
- `BAREA` — boarding area derived from gate: A n=705 (25.1%), B n=251 (8.9%), C n=198 (7.0%), D n=521 (18.5%), E n=170 (6.1%), F n=436 (15.5%), G n=528 (18.8%)
- `RUNID` — "Run on which survey was conducted": 206 distinct run values present, 12 rows blank. Fieldwork was clearly spread across many separate shifts/flights rather than one sitting.
- `DAY` — day of week: Tue n=618, Wed n=581, Thu n=563, Fri n=403, Sun n=305, Sat n=240, Mon n=99. Weekday-heavy, with Monday thinnest.

**Weighting.** `WEIGHT` is defined as "Weight assigned to each record to proportionally represent SFO passengers." All 2,809 records carry a weight; weights range 0.208 to 3.888, mean 1.000, summing to 2,809 — i.e. the weights are normalized to sample size, **not** scaled to a passenger population count. Weighted results represent a reweighted sample, and the sum of weights should not be read as a number of passengers.

**Timing.** `INTDATE` ("Date of interview") contains day-of-month values only (25 distinct values, 1–31, no missing). There is no month or year field in the file, so the exact fieldwork window cannot be recovered from these files — only that interviewing occurred on at least 25 distinct calendar days.

## What is *not* in the provided files

The dictionary documents field definitions and codes, not a methodology report. Not available here, and I won't guess at them:
- Recruitment/approach procedure and refusal handling
- **Response rate / cooperation rate**
- The sampling frame and how flights/gates were selected within strata
- The weighting formula, weighting targets, or variance/design specification (note: a field named `STRATA` or `RUNID` documents a label on each record, not a validated variance design — so I would not produce design-based confidence intervals from this file)
- Calendar month/year of fieldwork
- Questionnaire translation and back-translation procedure

One further scope note: free text is thin by design — `Q15A` ("why is that?") is populated for 354 of 2,809 rows; other follow-ups were coded into fixed categories rather than kept as verbatims.

**Evidence note.** Source: data dictionary "Code List" sheet (rows defining RUNID, INTDATE, DAY, BAREA, STRATA, PEAK, METH, SAQ, LANG, WEIGHT) plus frequency counts over all 2,809 CSV rows. No filters applied; denominator is all rows, not valid answers to a question. Unweighted counts. METH=3 suppressed at n<20 per reporting rules; METH=2 (n=25) and LANG=4 (n=23) flagged as small. Limitation: administrative fields describe how records were tagged, not an independently documented methodology.