I'll gather grounding facts first — the Q7 service ratings, restroom cleanliness, and NPS — before forming a view.

Now let me read the Q7 scale definitions and compute all service ratings.

[Synthesis — grounded in computed figures below]

## The headline

**Food & beverage is the single biggest opportunity.** It is simultaneously the lowest-rated service SFO asks about, the one with the largest answering base, and the most-cited improvement suggestion in the survey. Retail is statistically right alongside it, but food carries far more passenger voice behind it.

---

## The evidence

**1. Food and retail sit at the bottom of the Q7 service ratings.**

All Q7 items, unweighted means (scale: 5 = Outstanding, 1 = Unacceptable; codes 2–4 have no verbal labels in the dictionary):

| Service | Mean | Valid n |
|---|---|---|
| Retail shops and concessions | 3.55 | 2,277 |
| Restaurants | 3.56 | 2,342 |
| Long term parking lot shuttle | 3.78 | 649 |
| Airport rental car center | 3.82 | 910 |
| Airport parking facilities | 3.83 | 1,065 |
| Info booths (lower level) | 3.85 | 1,518 |
| Info booths (upper level) | 3.87 | 1,529 |
| Signs/directions on roadways | 3.94 | 1,772 |
| Artwork and exhibitions | 3.95 | 2,160 |
| Free wi-fi | 3.98 | 2,074 |
| Signs/directions inside SFO | 4.04 | 2,648 |
| AirTrain | 4.05 | 1,309 |
| Information on screens/monitors | 4.09 | 2,611 |
| Escalators/elevators/walkways | 4.11 | 2,537 |
| **SFO as a whole** | — | 2,625 |

The items below food and retail (parking shuttle, rental car, parking) are rated on much smaller bases — they touch a minority of respondents. Food and retail are rated by ~83% and ~81% of the sample respectively. **Scale of exposure is what separates them.**

**2. The distributions show the problem is a big mushy middle, not a vocal minority.**

- **Restaurants** (valid n=2,342; 467 excluded as N/A-never-used/blank): code 5 = 15.0%, code 4 = 39.1%, code 3 = 34.6%, code 2 = 9.8%, code 1 = 36 respondents (1.5%, small cell).
- **Retail** (valid n=2,277; 532 excluded): code 5 = 14.8%, code 4 = 36.5%, code 3 = 38.6%, code 2 = 8.9%, code 1 = 27 respondents (1.2%, very small cell).

Compare with the airport overall (valid n=2,625; 184 excluded): code 5 = 24.0%, code 4 = 54.4%, code 3 = 19.6%, code 2 = 1.75%, code 1 = 6 respondents (**suppressed**, n<20). Roughly a third of respondents park food and retail at the midpoint, versus about a fifth for the airport as a whole.

**3. It is also the top thing passengers actually ask for.**

Of 2,809 respondents, 1,367 gave at least one coded Q8 improvement suggestion. Distinct respondents per theme (a respondent can appear in several themes; these do not sum to 100%):

| Theme (Q8 codes) | Respondents |
|---|---|
| Amenities, broad bucket (11–27) | 374 |
| **Restaurants (101–110)** | **327** |
| Signage/wayfinding, excl. positive (51–61, 63–67) | 212 |
| Security/TSA, negative codes only | 211 |
| Boarding areas/gates (31–36) | 133 |
| Getting to the airport (71–78) | 128 |
| Shops (151–155) | 102 |
| Airlines (501–505) | 37 |

The *amenities* bucket is nominally larger but is a grab-bag of 17 distinct codes. The **single most-cited individual code in the entire survey is 102, "offer a wider variety/selection of restaurants/add more restaurants," at 159 respondents** — ahead of charging stations/plugs (code 14, 98), wi-fi (code 11, 93), and security inefficiency (code 202, 82). Price (code 101, 49) and more casual/fast-food options (code 103, 49) follow.

So food is the only area where the *rating* and the *unprompted ask* point to the same place. Note that retail's near-identical rating is backed by only 102 suggestion respondents — weaker signal.

**4. Food and retail ratings co-vary sharply with advocacy.**

Overall NPS = **31.0** (valid n=2,650; 159 excluded).

| Group | NPS | Valid n |
|---|---|---|
| Rated restaurants 1–3 | 1.9 | 1,012 |
| Rated restaurants 4–5 | 56.8 | 1,214 |
| Rated retail 1–3 | 5.0 | 1,050 |
| Rated retail 4–5 | 56.9 | 1,113 |

**Read this associatively, not causally.** This is cross-sectional data; a general halo — people who like SFO rate everything higher — would produce a similar pattern. It does not establish that improving concessions would move NPS.

---

## What I'd say to leadership

**From the data:** Concessions are SFO's weakest link on its own scorecard, and food specifically is where passenger demand is loudest and most specific. The ask is not primarily "cheaper" — variety/selection (159) outweighs price (49) by more than three to one in the coded suggestions. That's a merchandising-mix question more than a pricing one.

**Hypotheses worth testing, not findings:** that mid-point ("3") ratings reflect indifference to a generic offer rather than active dissatisfaction; and that variety complaints concentrate in particular boarding areas or at particular hours. The dataset contains BAREA and STRATA fields that could be cross-tabbed to check the second — say the word and I'll run it.

**Beyond the data (general industry practice):** airports typically address this through concession-mix reviews at lease renewal, local/regional brand tenanting, and extending operating hours at the shoulders of the day. I have no evidence in these files about SFO's lease cycle, tenant mix, or the cost or effectiveness of any such intervention, so I won't characterize any of it as cheap or proven here.

**Runner-up worth a second slot:** electrical outlets/charging stations (code 14, 98 respondents) — a frequent, concrete ask that the Q7 battery doesn't measure at all, so it's invisible in the ratings table above.

---

### Evidence note
- **Source fields:** Q7ART–Q7ALL (Rating SFO, 5=Outstanding/1=Unacceptable; 6=never used/NA and 0=blank excluded); Q9Restroom (cleanliness, 5=Clean/1=Dirty — a separate scale, computed at 4.01, n=2,589, and not a driver here); NETPRO (0–10, 11=blank); Q8-1…Q8-6 multiple-response suggestion codes.
- **Weight mode:** unweighted throughout. The question is unqualified, so I used unweighted descriptive estimates. Ask and I'll rerun weighted.
- **Denominators:** valid answers to each specific question after exclusions, not all 2,809 rows. Exclusion counts are listed per item above.
- **Tooling:** Q7/Q9/NETPRO figures from the fixed survey_statistic calculator (suppression at n<20; caution at n<30 and n<50). Q8 theme tabulation is **model-written hosted code** and should be independently reviewed — theme groupings are my reading of the dictionary's code blocks, not an official SFO taxonomy.
- **Suppressed:** Q7ALL code 1 (n=6) and Q7ALL overall mean were not released by the calculator; Q7STORE code 1 (n=27) and Q7FOOD code 1 (n=36) carry small-cell cautions.
- **Limits:** single 2018 snapshot — no trend or post-2018 inference possible. Means are descriptive summaries; I've shown distributions alongside. No significance testing or confidence intervals, as no reviewed variance design is available. Q8 codes are interviewer-assigned categories, not verbatim text, and only 1,367 of 2,809 respondents offered any suggestion — so suggestion counts describe who chose to speak, not the full passenger population.