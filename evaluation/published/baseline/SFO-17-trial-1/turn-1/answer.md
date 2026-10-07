I'll start by checking the dictionary for the TSA PreCheck question wording and codes, then compute the association.

## Short answer: No — this data can't establish causation, and the overall-satisfaction gap is negligible anyway.

**[Computed — unweighted** (question is unqualified), Q11TSAPRE=1 "Yes" vs =2 "No"; codes 3 (Don't know), 4 (Did not go through security), 0 (blank) excluded**]**

### Overall satisfaction with SFO as a whole (Q7ALL, 1=Unacceptable … 5=Outstanding)

| | PreCheck = Yes | PreCheck = No |
|---|---|---|
| Mean | **4.02** | **3.99** |
| Valid n (unweighted) | 934 | 1,221 |
| Rated 5 (Outstanding) | 23.8% | 23.8% |
| Rated 4 | 56.4% | 54.1% |
| Rated 3 | 18.2% | 19.9% |
| Rated 2 | *suppressed, n=13* | 2.0% (n=25, small cell) |
| Rated 1 | *suppressed, n=2* | *suppressed, n=2* |

The mean difference is 0.03 points on a 5-point scale — essentially nothing. Top-two-box (4 or 5) is 80.2% vs 77.9%. I have no reviewed variance design here, so I'm not calling this significant or non-significant; descriptively it's a trivial gap.

### Where there *is* a visible gap: likelihood to recommend
NETPRO (0–10): NPS **+39.1** for PreCheck users (valid n=965) vs **+26.8** for non-users (valid n=1,228) — a ~12-point difference. So the two satisfaction-adjacent measures point in different directions in magnitude, which is itself a reason for caution.

### Why "cause" is the wrong word here
This is a cross-sectional, single-day intercept survey — nobody was randomly assigned to PreCheck. PreCheck use **co-occurs with** being a different kind of traveler:

- **Flight frequency** (Q5TIMESFLOWN, model-written cross-tab, subject to independent review): 25.4% of PreCheck users flew out of SFO 7+ times in the past year vs 12.2% of non-users; 42.6% of non-users flew just once vs 27.9% of PreCheck users.
- **Residency** (Q17LIVE): 40.6% of PreCheck users are Bay Area residents (valid n=972) vs 33.4% of non-users (valid n=1,238).

Frequent flyers and locals both self-select into PreCheck *and* tend to rate airports differently (familiarity, fewer navigation problems, loyalty-program exposure). Any of that could sit behind the NPS gap. The data cannot separate "PreCheck improved the trip" from "people who already like/know SFO are the ones enrolled."

**What you'd need instead:** a pre/post enrollment comparison, or at minimum a model holding flight frequency, residency, and trip purpose constant — and even then it would be an adjusted association, not a causal effect.

---
**Evidence note.** Source: 2018 SFO Customer Survey CSV. Fields: Q11TSAPRE (1=Yes, 2=No; 3/4/0 excluded), Q7ALL (1–5; 6=N/A, 0/BLANK excluded), NETPRO (0–10; 11=blank excluded), Q17LIVE (0 excluded), Q5TIMESFLOWN. Unweighted throughout. Q7ALL/NETPRO/Q17LIVE figures from the fixed survey_statistic tool; two Q7ALL cells (n=13 and n=2 for PreCheck users; n=2 for non-users) were **suppressed as small cells** and are reported as raw counts only. The Q5TIMESFLOWN cross-tab is model-written code and should be independently reviewed. Limitations: observational design, self-selection into PreCheck, no recruitment or response-rate documentation in the provided files.