I'll compute the weighted distribution of Q7ALL (SFO airport as a whole).

[Computed] — weighted distribution of **Q7ALL**, the rating of "SFO Airport as a whole" (1 = lowest / 5 = highest).

| Code | Unweighted n | Weighted % of valid |
|---|---|---|
| 1 (lowest) | 6 | **suppressed** (n < 20) |
| 2 | 46 | 1.7% *(small cell, n < 50)* |
| 3 | 514 | 17.7% |
| 4 | 1,428 | 54.7% |
| 5 (highest) | 631 | 25.8% |

**Weighted mean: 4.04** (valid unweighted n = 2,625)

Notes on reading this:
- The listed percentages do not sum to 100% because the code-1 cell is suppressed under the n<20 reporting rule. I have not back-filled it by subtraction.
- The code-2 cell rests on only 46 respondents — treat that 1.7% as a small-cell estimate.
- The dictionary supplies verbal anchors only for the scale endpoints on this Q7 item, so codes 2, 3 and 4 are left as numeric codes rather than given invented labels.
- Beyond the mean: the distribution is concentrated at code 4 — a solid-but-not-top-box pattern — with about a sixth of valid responses sitting at the midpoint code 3.

**Evidence note**
- Source field: Q7ALL (Code List!A234:C255), 1–5 scale.
- Filters: none. Denominator: valid answers only.
- Weight mode: **weighted** (WEIGHT field); sum of weights = 2,618.67. That sum is a weight total, not a count of passengers.
- Valid unweighted n = 2,625 of 2,809 selected; 184 excluded as missing/not-applicable (blank, 0, 6, and the literal text "BLANK", which Q7ALL is known to contain). Missing codes are never treated as ratings.
- Limitation: this is a descriptive 2018 snapshot. No significance tests or confidence intervals are offered, as no reviewed sampling/variance design is available here.

If you'd like, I can also show the unweighted distribution for comparison, or a top-two-box ("4 or 5") share — each would be a separate calculation.