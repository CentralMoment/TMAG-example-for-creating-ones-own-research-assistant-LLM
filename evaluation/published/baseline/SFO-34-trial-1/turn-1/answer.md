I'll start by checking the data dictionary and the relevant fields.

**[Computed]** Chart and supporting table created: `sfo_q7all_by_gender.png` and `sfo_q7all_by_gender.csv`.

**Operationalization (judgment call):** I read "total satisfaction" as **Q7ALL — "SFO airport as a whole"**, the 1–5 rating (1=Unacceptable, 5=Outstanding). If you meant something else (e.g., a composite average across all Q7 service items, or NETPRO), say so and I'll recompute.

Because "travelers" is population language, these are **weighted** percentages; all n's reported are unweighted.

| Q7ALL rating | Male % (n) | Female % (n) |
|---|---|---|
| 1 Unacceptable | suppressed (n=1) | suppressed (n=3) |
| 2 | 1.8% (n=21) | suppressed (n=19) |
| 3 | 18.3% (n=229) | 17.0% (n=256) |
| 4 | 55.7% (n=639) | 54.0% (n=711) |
| 5 Outstanding | 24.2% (n=250) | 27.4% (n=345) |
| **Total valid** | **n=1,140** | **n=1,334** |

Notes on the chart: suppressed cells are drawn as hatched placeholders and labeled, **not** as zero-height bars. The male "2" bar is plotted but flagged as a small cell (n=21) — treat it as unreliable.

**What it shows:** the two distributions are close in shape — both are concentrated at "4," with roughly a quarter at "Outstanding." Female respondents sit slightly higher at "5" (27.4% vs 24.2%) and slightly lower at "3." This is a descriptive difference only; I have no reviewed variance design here, so I'm not claiming it is a statistically significant population difference.

**Evidence note**
- Source fields: Q7ALL (Code List!A234:C255), Q21Gender (Code List!A638:C642); computed by the trusted `survey_statistic` calculator, chart/CSV rendering by model-written code using those returned values.
- Filters: Q21Gender=1 (Male), =2 (Female). Valid Q7ALL codes 1–5.
- Exclusions: code 6 ("never used/N/A"), blanks and literal "BLANK" — 77 excluded among males, 80 among females; 170 respondents overall gave no usable gender.
- Weight mode: weighted (WEIGHT field) for percentages; unweighted n reported throughout. Sums of weights are not passenger population counts.
- **Non-binary respondents: raw count n=8 only** — below the n<20 threshold, so no summary statistic is reported or plotted for that group. This means the chart does not represent all travelers.