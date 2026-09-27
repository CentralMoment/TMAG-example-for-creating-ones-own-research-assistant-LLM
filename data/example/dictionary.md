# Fictional practice survey

This deliberately simple dataset is synthetic and contains 60 invented rows.
No record represents a real person. One fictional wave only; no date comparison.

| Field | Meaning |
|---|---|
| respondent_id | Artificial row number, not a person identifier |
| group | A or B, artificial groups with 30 rows each |
| satisfaction | Integer 1–5, higher means more satisfied; all rows valid |
| weight | All 1.0; weighted and unweighted results match |

Define satisfied as satisfaction >= 4, unless explicitly asked otherwise.
Known checks: n=60; mean satisfaction=3.0; satisfied=24/60=40%; each group
has mean=3.0 and 12/30=40% satisfied. Group estimates need a small-sample caveat.
These convenient results are for debugging only, not a research conclusion.
