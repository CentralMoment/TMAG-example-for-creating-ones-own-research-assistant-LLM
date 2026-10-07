I'll start by confirming the field definition and computing the weighted distribution with the trusted calculator.

The calculator suppressed one cell. Let me pull the exact question wording and scale labels, then build the chart.

Dictionary confirms **Q7ALL = "SFO airport as a whole," 5=Outstanding … 1=Unacceptable** (6 = never used/N/A, 0 = blank — both excluded). Now the chart:

**[Computed]** Both files are attached: `q7all_weighted.png` (the chart) and `q7all_weighted.csv` (the underlying aggregate table).

**Question used:** Q7ALL — *"SFO airport as a whole,"* rated 5 = Outstanding down to 1 = Unacceptable. This is the general/overall satisfaction item, as distinct from the 14 specific service ratings (Q7FOOD, Q7WIFI, etc.).

**Weighted distribution**

| Rating | Weighted freq. | Weighted % | Unweighted n |
|---|---|---|---|
| 5 — Outstanding | 674.5 | 25.8% | 631 |
| 4 | 1,433.1 | 54.7% | 1,428 |
| 3 | 462.8 | 17.7% | 514 |
| 2 | 43.4 | 1.7% | 46 |
| 1 — Unacceptable | *suppressed* | *suppressed* | 6 |
| **Total valid** | **2,618.67** | **100%** | **2,625** |

**Two things to read carefully on the chart:**

- **Code 1 is suppressed, not zero.** Only 6 respondents rated SFO "Unacceptable" — below the n<20 threshold, so I report the raw count only and no summary statistic. On the plot it appears as a hatched, labeled placeholder, deliberately *not* a zero-height bar, so it can't be misread as "nobody chose this."
- **Code 2 (n=46) is a small cell** — under n=50, so treat that 1.7% as indicative rather than precise.

The shape is a strong left-skew: roughly four in five weighted responses sit at 4 or 5, with the mode firmly at 4 rather than 5.

**Evidence note**
- **Source:** Q7ALL, 2018 SFO Customer Survey; wording and scale labels read from the Data Dictionary (Code List!A234:C255).
- **Weight mode:** Weighted, using WEIGHT, per your request for weighted frequency.
- **Valid n:** 2,625 unweighted of 2,809 rows; 184 excluded (code 6 = "have never used/not applicable", code 0/blank, and the literal text `BLANK`).
- **Computation:** Distribution came from the trusted `survey_statistic` calculator; the chart and CSV are model-written rendering of those returned values and are subject to independent review.
- **Limitations:** Bar heights are **sums of survey weights, not passenger population counts**. This is a single 2018 snapshot — no trend reading. Percentages are of valid answers, not all 2,809 rows.

Happy to redo this as weighted *percent* instead of frequency, overlay the unweighted distribution for comparison, or split it by residency (Q17LIVE) or TSA PreCheck (Q11TSAPRE) if that's useful.