I'll compute that now.

[Computed]

**Mean rating of restroom cleanliness (Q9Restroom): 4.01**

- Scale: 1 = Dirty to 5 = Clean (3 = Average)
- Unweighted valid n = 2,589
- Excluded: 220 rows (blanks / missing / "N/A" code 6) out of 2,809 total
- Weight mode: unweighted (the question is unqualified, so I used unweighted descriptive estimates)

**Distribution behind that mean** (same denominator, n = 2,589, unweighted):

| Code | Label | n | % of valid |
|---|---|---|---|
| 1 | Dirty | 19 | suppressed (n < 20) |
| 2 | — | 109 | 4.2% |
| 3 | Average | 567 | 21.9% |
| 4 | — | 1,021 | 39.4% |
| 5 | Clean | 873 | 33.7% |

The percentage for code 1 is suppressed under the calculator's reporting rule (suppress below n = 20); only the raw count of 19 is reportable. Codes 2 and 4 have no verbal labels in the data dictionary, so I've left them as numeric codes.

**Reading it:** the mean sits just above 4, and the distribution is clearly skewed toward the clean end — roughly three-quarters of valid responses fall at 4 or 5, with dissatisfaction concentrated in a small tail. A mean alone would understate how much of the response mass is bunched at the top two points.

**Evidence note**
- Source field: Q9Restroom (restroom cleanliness, Code List!A376:C389). This is a distinct scale from the Q7 service-rating battery.
- Filters/definition: none; all respondents with a valid 1–5 answer.
- Weight mode: unweighted. If you want a passenger-population estimate instead, I can rerun with WEIGHT.
- Exclusions: 220 of 2,809 rows lack a valid 1–5 rating and are not in the denominator.
- Limitation: single 2018 snapshot; no trend or benchmark comparison is possible from these files. Means of ordinal rating scales are descriptive summaries only.