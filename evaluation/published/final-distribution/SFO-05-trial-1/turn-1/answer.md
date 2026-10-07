I'll compute the weighted distribution for Q7ALL (the airport-as-a-whole rating) and check its dictionary definition.

[Computed] — Weighted distribution of **Q7ALL, "SFO airport as a whole"** (the overall airport rating), scale 1 = Unacceptable to 5 = Outstanding.

| Code | Weighted % | Unweighted n |
|---|---|---|
| 5 — Outstanding | 25.8% | 631 |
| 4 | 54.7% | 1,428 |
| 3 | 17.7% | 514 |
| 2 | 1.7% | 46 |
| 1 — Unacceptable | **Suppressed (n<20)** | 6 |

Notes on the cells:
- **Code 1 is suppressed** per the calculator's reporting rule (suppress below n=20); only the raw count of 6 can be shown.
- **Code 2 carries a small-cell caution** (n<50) — treat that 1.7% as imprecise.
- Codes 2, 3 and 4 have no verbal labels in the dictionary; only 5 (Outstanding) and 1 (Unacceptable) are labeled, so I've left the middle points as numeric codes.

**Evidence note**
- Source field: Q7ALL ("SFO airport as a whole"), dictionary reference Code List!A234:C255.
- Valid codes: 1–5. Excluded as non-ratings: blank/0, 6 ("Have never used or visited / Not applicable"), and the literal "BLANK" text.
- Weight mode: **weighted** (WEIGHT field), as requested. Denominator = valid answers only.
- Unweighted valid n = **2,625**; 184 of 2,809 rows excluded as missing/N/A. Sum of weights = 2,618.67 — this is a weight total, not a passenger headcount.
- Percentages shown exclude the suppressed cell, so the four reported cells do not sum to 100%.
- Limitation: this is a descriptive distribution from a single 2018 cross-section; no significance tests or confidence intervals are implied.

If useful, I can also compute the mean of Q7ALL, the unweighted distribution for comparison, or break this out by residency (Q17LIVE) — each as a separate calculation.