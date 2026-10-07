I'll check the data dictionary for the official definition.

**[Computed + dictionary lookup]**

**NETPRO is the Net Promoter / likelihood-to-recommend item.** Per the data dictionary (Code List!A579:C591), the question wording is:

> "On a scale of 0 to 10, how likely is it that you would recommend SFO to a friend or colleague?"

**Response codes**
- Valid: **0–10**, where **10 = "Extremely likely"** and **0 = "Not at all likely"** (1–9 are unlabeled scale points)
- **11 = Blank** — a missing code, not a rating. It must be excluded from any numeric summary.

**How it's conventionally used:** NETPRO is the input to Net Promoter Score, calculated as 100 × (share scoring 9–10, "promoters") − (share scoring 0–6, "detractors"); 7–8 are "passives" and drop out of the NPS arithmetic.

**Unweighted distribution of valid responses (n = 2,650; 159 excluded as blank/11):**

| Score | n | % of valid |
|---|---|---|
| 10 | 770 | 29.1% |
| 9 | 498 | 18.8% |
| 8 | 601 | 22.7% |
| 7 | 334 | 12.6% |
| 6 | 133 | 5.0% |
| 5 | 205 | 7.7% |
| 4 | 24 | 0.9% |
| 3 | 26 | 1.0% |
| 2 | 24 | 0.9% |
| 1 | 11 | **suppressed** (small cell) |
| 0 | 24 | 0.9% |

Note: the score-of-1 cell (n = 11) is **suppressed** by the calculator as too small to report a percentage; the raw count only is shown. Cells with n < 50 (scores 0–4) are flagged as small and individually unstable.

**One caution on the field name:** in the CSV the header carries trailing whitespace (`"NETPRO  "`), so it needs trimming before use — otherwise a lookup by the clean name `NETPRO` will fail.

**Evidence note** — Source: Data Dictionary "Code List" rows 579–591 for definition/codes; NETPRO column of the 2018 CSV for the distribution. Filters: none. Weight mode: unweighted (no population wording in the question). Valid n = 2,650 of 2,809 rows; 159 excluded as code 11/blank. Limitation: this is a single 2018 snapshot, and percentages here describe respondents, not SFO's passenger population — ask me for the weighted version or the NPS itself if you want either.