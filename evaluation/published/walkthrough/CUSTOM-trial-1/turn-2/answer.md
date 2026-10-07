**[Computed]**

**Weighted: 80.5% "happy"** (Q7ALL = 4 or 5), vs. **78.4% unweighted** — a gap of about 2.0 percentage points.

| Measure | Unweighted | Weighted (WEIGHT) |
|---|---|---|
| Happy (Q7ALL 4 or 5) | 78.44% | 80.49% |
| Unweighted valid n (denominator) | 2,625 | 2,625 |
| Numerator (unweighted n) | 2,059 | 2,059 |
| Sum of weights | 2,625.0 | 2,618.67 |

Same valid-answer denominator in both modes, as requested: 2,625 valid Q7ALL ratings, with 184 of the 2,809 rows excluded as missing ('', '0', '6', 'BLANK').

**Full distribution, both modes** (n = 2,625):

| Code | n | Unweighted % | Weighted % |
|---|---|---|---|
| 1 (Unacceptable) | 6 | suppressed (n<20) | suppressed (n<20) |
| 2 | 46 | 1.75% | 1.66% |
| 3 | 514 | 19.58% | 17.67% |
| 4 | 1,428 | 54.40% | 54.73% |
| 5 (Outstanding) | 631 | 24.04% | 25.76% |

Weighting shifts a little mass out of code 3 and into code 5, which is where the 2-point lift in the top-two box comes from. Code 4 is essentially flat between modes.

**Files delivered** (both returned by the tool in `$OUTPUT_DIR`):
- `q7all_weighted_vs_unweighted.png` — two panels: the headline unweighted-vs-weighted "happy" comparison, and the full 1–5 distribution in both modes. The suppressed code-1 cell is labeled as suppressed and deliberately **not** plotted as zero.
- `q7all_weighted_vs_unweighted.csv` — the aggregate table behind the chart, including suppressed cells marked `SUPPRESSED`, the denominator row, and the excluded-missing row. Aggregate only; no respondent-level records.

**Evidence note**
- Source field: Q7ALL (SFO airport as a whole), valid codes 1–5; missing codes '', '0', '6', 'BLANK'.
- Definition: "happy" = Q7ALL ∈ {4,5}, your stated definition.
- Filters: none. Denominator: valid answers after filters, unweighted valid n = 2,625; excluded n = 184 of 2,809 selected rows.
- Percentages from the fixed survey calculator; the PNG/CSV were produced by model-written code that plots those calculator values and is subject to independent review.
- Limitations: the 2-point unweighted/weighted gap is a descriptive difference — I have no reviewed variance design here, so I can't call it statistically significant. Sums of weights (2,618.67) are not passenger counts. The dictionary gives verbal labels only for codes 1 and 5, so 2–4 are left as numeric codes.