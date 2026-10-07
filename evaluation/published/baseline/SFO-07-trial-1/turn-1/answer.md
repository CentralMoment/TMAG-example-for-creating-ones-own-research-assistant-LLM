I'll gather grounding facts first — the service-category ratings, restroom cleanliness, NPS, and the verbatim comments — before forming a recommendation.

Now let me compute the full service-category rating profile.

Food and retail are the two lowest-rated categories. Let me check their distributions and how they associate with NPS, plus read the dictionary for the problem-code fields.

Now the association analysis and the most common improvement-suggestion codes.

One more check: how each service category's rating correlates with NPS, so "biggest opportunity" reflects leverage, not just a low score.

## [Synthesis — grounded in computed findings]

**My recommendation: concessions — food & beverage first, retail alongside it. Specifically, variety and selection.**

Three independent lines of evidence in the 2018 data converge on this, which is why I'd put it ahead of anything else.

### 1. Food and retail are the two lowest-rated services at SFO

Unweighted means on the 1–5 Q7 service scale, valid answers only:

| Service | Mean | Valid n | % rating 1–2 |
|---|---|---|---|
| **Q7STORE (retail)** | **3.55** | 2,277 | 9.8% |
| **Q7FOOD (restaurants)** | **3.56** | 2,342 | 10.8% |
| Q7LTPARKING | 3.78 | 649 | — |
| Q7RENTAL | 3.82 | 910 | — |
| Q7PARK | 3.83 | 1,065 | — |
| Q7INFODOWN | 3.85 | 1,518 | — |
| Q7WALKWAY (highest) | 4.11 | 2,537 | 2.3% |

Food and retail are the only two categories below 3.6, and they carry roughly **4x the bottom-box rate** of the best-performing categories. On food, only 15.0% gave a top rating of 5 (n=351/2,342); 34.6% parked at a neutral 3. Retail is similar: 14.8% top-box, 38.6% neutral. The problem isn't a vocal minority of angry passengers — it's a very large middle that finds concessions merely adequate.

For context, the airport overall (Q7ALL) scores far better: 78.4% rate it 4 or 5 (n=2,625 valid, 184 excluded). Unweighted NPS is **+31.0** (n=2,650). Concessions are a visible soft spot inside an otherwise well-regarded airport.

### 2. It's also what passengers volunteer unprompted

Among the 1,367 respondents who gave at least one coded improvement suggestion (Q8, six multi-response slots, each respondent counted once per code):

- **Restaurants/food: 23.9%** (327) — the largest *specific* service theme
- Signage/wayfinding: 15.8% (216)
- Boarding areas/gates: 9.7% (133)
- Shops/retail: 7.3% (100)

The single most common individual code in the entire Q8 set is **"offer a wider variety/selection of restaurants" — 159 respondents, 11.6%**, ahead of charging stations (98) and Wi-Fi (93). Price is secondary but real: "too expensive" (101) at 49, "more casual/fast food" (103) at 49, "improve food quality" (105) at 33.

So the top-of-mind ask isn't cheaper food or cleaner food — it's **more and different food**.

### 3. Concessions ratings track strongly with willingness to recommend

NPS by food rating (unweighted): rating 1 → **−54.5** (n=33), 2 → −20.7 (n=208), 3 → +10.4 (n=771), 4 → +48.4 (n=881), 5 → **+79.3** (n=333). Retail follows nearly the same curve (rating 1: −39.1, but **n=23 — too small for a reliable estimate**; rating 5: +80.3, n=320).

That said, I want to be careful here: when I correlated every service item against NETPRO, food (r=0.43) and retail (r=0.42) rank mid-pack — signage (0.47), gate-info-up (0.47) and info-down (0.46) correlate slightly *higher*. **All fifteen items cluster between 0.27 and 0.47, so I would not claim food is the strongest NPS driver.** The case for concessions is that it combines *average* leverage with *the worst scores and the loudest volunteered demand* — that's where the headroom is, not where the lever is uniquely strong.

### What I'd actually do

**From the data:** prioritize restaurant *mix and breadth* over price cuts or cleanliness. Cleanliness is not the complaint — Q9Restroom (1=Dirty, 5=Clean) averages 4.02 (n=2,589), and "cleaner food areas" was raised by only 2 respondents. Dietary-specific gaps (vegan/halal/gluten-free, 16) and local Bay Area options (3) are small but directionally consistent with a variety story. Worth noting: only 369 of 2,645 respondents (14.0%) reported encountering any problem at all (Q15PROBLEM), so this is an satisfaction-ceiling issue, not a failure-recovery issue.

**Beyond the data (general industry practice):** concessions is also one of the few levers that's commercially self-funding through non-aeronautical revenue, and lease-cycle timing usually dictates how fast a mix can change — neither of which this survey speaks to.

---

**Evidence note.** Source: 2018 SFO Customer Survey, 2,809 rows. Fields: Q7FOOD/Q7STORE and 13 other Q7 items (1–5; 0/6/blank excluded as missing), Q7ALL (contains literal "BLANK"), Q9Restroom (1=Dirty…5=Clean, *not* the Q7 scale), NETPRO (0–10 valid, 11=blank; header whitespace trimmed), Q8-1…Q8-6 multi-response, Q15PROBLEM. **Unweighted throughout** — the question was not population-worded. Denominators are valid answers per item, so n varies by item (612–2,648); the Q8 denominator (1,367) is self-selected respondents who offered a suggestion and is **not** a prevalence estimate for all passengers. Means/distributions and NPS came from the fixed survey_statistic tool; the Q8 code aggregation and the NETPRO correlations are **model-written code and warrant independent review**. One cell suppressed by the tool (Q7ALL=1, n=6) and retail rating 1 (n=23) flagged as unreliable. **Limitations:** single 2018 cross-section — no trend or post-2018 inference is possible, and all relationships above are associative, not causal. Recruitment method and response rate are not documented in the provided files.

Want me to break concessions ratings out by terminal/boarding area, or by residency (Q17LIVE) or trip purpose, to see where the gap concentrates?