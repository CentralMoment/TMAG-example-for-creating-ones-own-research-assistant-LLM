I'll check the data dictionary for any documented methodology, and look at the structure of the data file itself.

**[Computed + Metadata]** The provided files contain no methodology narrative — no technical report, no sampling plan, no response rate. What follows is what I could reconstruct from the data dictionary's field definitions plus the distribution of the design fields in the CSV itself.

## What the design fields tell us

**Total records: 2,809** (unweighted; every row has a WEIGHT value).

**Mode of collection (METH)** — n = 2,809, no missing:

| Method | n | % |
|---|---|---|
| 1 = At gate | 2,779 | 98.9% |
| 2 = Mail-in | 25 | 0.9% |
| 3 = Online | 5 | 0.2% |

This is overwhelmingly an **intercept survey conducted at departure gates**. Mail-in and online are residual (n=25 and n=5 — too small to summarize separately; raw counts only, per reliability rules).

**Administration (SAQ)** — n = 2,809:

| | n | % |
|---|---|---|
| 2 = Self-administered | 2,473 | 88.0% |
| 1 = Interviewer-administered | 336 | 12.0% |

Cross-tabbed, all 336 interviewer-administered cases were at the gate; all mail-in and online cases were self-administered.

**Languages offered (LANG)** — the questionnaire existed in four languages: English (2,639), Chinese (75), Spanish (72), Japanese (23). The three non-English groups are small; Japanese at n=23 is below the threshold for a reliable summary statistic.

## Sampling structure

The dictionary documents an explicitly **stratified** design with several frame variables:

- **STRATA** — departure time band: AM, before 11am (679); MID, 11am–5pm (1,035); PM, after 5pm (1,095).
- **PEAK** — domestic peak (8am–1pm, 600); domestic off-peak (1,154); international (1,055).
- **BAREA** — boarding area A–G, derived from gate number. A (705), G (528), D (521), F (436), B (251), C (198), E (170). 71 distinct gates appear.
- **DAY** — day of week, all seven represented, heaviest Tue/Wed/Thu (618/581/563), lightest Monday (99).
- **RUNID** — "run on which survey was conducted": 205 distinct runs, 12 rows blank. A "run" appears to be a single sampling shift at a gate, with roughly 1–43 completes each. This is the practical clustering unit of the design.

**Weighting (WEIGHT)**: defined in the dictionary as "weight assigned to each record to proportionally represent SFO passengers." Range 0.208 to 3.888, mean exactly 1.0, summing to 2,809 — i.e. the weights are **normalized to sample size**, not scaled to a passenger count. Do not read the weight sum as a number of travelers.

## What is *not* in the files

- **Fieldwork period.** `INTDATE` holds only a day-of-month (values 1–31, with 7, 14, 25–28 absent). There is no month or year field, so the calendar window and number of fieldwork days can't be recovered from these files.
- **Response/refusal rate**, number approached, or cooperation rate — no disposition field exists.
- **Sampling frame construction and weighting targets** — the dictionary states the weight's purpose but not the variables or control totals used to build it.
- **Screening/eligibility rules**, interviewer training, quota targets, or fielding contractor. "CCGID" implies an outside firm assigned IDs, but the firm is not named in the files.
- Several `ARRTIME`/`DEPTIME` values carry a 12/31/1899 date stub, a spreadsheet time-only artifact — treat those as times of day, not dates.

I won't guess at any of the above; if you have SFO's accompanying methodology report, that's where those details would live.

---

**Evidence note.** Source: `2018 SFO Customer Survey Data Dictionary.xlsx` (sheet "Code List," field definitions for METH, SAQ, LANG, STRATA, PEAK, BAREA, DAY, RUNID, WEIGHT) and design-field frequencies computed from `2018 SFO Customer Survey.csv` (model-written pandas, subject to independent review; column headers trimmed of whitespace). Unweighted n = 2,809 for all frequencies above; no missing values on METH, SAQ, LANG, STRATA, PEAK, DAY, BAREA. Limitations: fieldwork dates, response rate, and weighting construction are not documented in the provided files. Single 2018 snapshot — no comparison to other years is possible.