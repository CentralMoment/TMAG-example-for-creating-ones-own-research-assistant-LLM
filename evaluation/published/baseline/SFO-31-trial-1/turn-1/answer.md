I'll start by inspecting the files and the data dictionary for the Q7 fields.

**[Computed — model-written clustering code, subject to independent review]**

## Methodology

| Choice | Value |
|---|---|
| Algorithm | k-means (scikit-learn), `n_init=25` |
| k | 3 (as you specified) |
| Seed | **20180101** |
| Variables | 7 core Q7 terminal-experience items: Q7ART, Q7FOOD, Q7STORE, Q7SIGN, Q7WALKWAY, Q7SCREENS, Q7WIFI |
| Scaling | z-scored (each item standardized before clustering) |
| Valid codes | 1–5 only. Code 6 ("never used / N/A") and 0 ("blank") treated as missing, **not** as ratings |
| Case handling | Complete cases on all 7 items |
| **Unweighted n clustered** | **1,449 of 2,809 rows (51.6%)** |
| Weight mode | Unweighted for the clustering itself; weighted share shown for reference |

**Why only 7 of the 15 Q7 items:** the ground-transport items are mostly "not applicable" — e.g. Q7LTPARKING is code 6 for 1,927 respondents, Q7PARK for 1,534, Q7RENTAL for 1,669. Requiring all 14 service items leaves only n=343. Q7ALL (airport as a whole) was deliberately held *out* of the features and used to validate the clusters.

## Cluster profiles (item means, 1=Unacceptable … 5=Outstanding)

| | n | % of clustered | ART | FOOD | STORE | SIGN | WALKWAY | SCREENS | WIFI | Mean of 7 |
|---|---|---|---|---|---|---|---|---|---|---|
| **1. Critics** | 390 | 26.9% | 3.14 | 2.76 | 2.81 | 3.11 | 3.23 | 3.25 | 3.21 | **3.07** |
| **2. Satisfied-but-not-wowed** | 702 | 48.4% | 3.95 | 3.52 | 3.49 | 4.11 | 4.13 | 4.11 | 3.95 | **3.89** |
| **3. Enthusiasts** | 357 | 24.6% | 4.74 | 4.54 | 4.55 | 4.87 | 4.89 | 4.87 | 4.69 | **4.74** |

Weighted shares of the clustered sample: 24.2% / 49.0% / 26.8% — close to the unweighted split.

## Hold-out validation (clusters were not fit on these)

| | Q7ALL mean (n) | % rating SFO 4–5 | NPS (n) | % Bay Area (Q17LIVE=1) |
|---|---|---|---|---|
| 1. Critics | 3.30 (379) | 34.1% | **−24.9** (370) | 33.8% (372) |
| 2. Satisfied | 4.03 (681) | 87.7% | **+41.0** (667) | 39.9% (667) |
| 3. Enthusiasts | 4.73 (343) | 95.2% | **+77.9** (339) | 35.9% (343) |

All subgroups exceed n=50, so no reliability suppression applies. The clusters separate sharply on overall rating and NPS, which is a meaningful external check. Residency barely differentiates them.

## Important caveat: these are severity tiers, not distinct taste profiles

Every cluster ranks the items in roughly the same order (food and retail lowest, walkways/screens/signs highest); they differ almost entirely in *level*. I tested this by re-clustering on each respondent's deviation from their own mean (shape only, same seed): that produces different, weaker groupings — one group ~1.1 points relatively harsher on Wi-Fi, another ~0.8–0.95 relatively harsher on food/retail — and those shape groups have nearly identical overall levels (3.72–3.99). So the dominant signal in Q7 is a single general-positivity dimension.

## Sensitivity

- **All 14 Q7 items, complete cases (n=343):** reproduces the same three-tier structure; 85.1% label agreement with the primary solution on the overlapping cases.
- **6 items, dropping Q7WIFI (n=1,749):** 93.0% agreement with primary.
- **Seed robustness:** seeds 1 and 20180101 give identical sizes (702/390/357, inertia 5508.5); seed 42 lands in a marginally worse local optimum (686/408/355, inertia 5509.6). Solution is stable but not perfectly deterministic across seeds.

## Limitations

- k=3 was imposed by your request, not selected by a fit criterion (no elbow/silhouette search was run).
- The 48% of rows excluded for item non-response are not missing at random — they skew toward respondents who skipped Wi-Fi, art, or food/retail items, so the clustered subsample is not representative of all 2,809 respondents.
- Cluster labels are analyst-assigned descriptions of centroids, not natural categories, and k-means on 5-point ordinal items treats them as interval-scaled.
- Associations with NPS and Q7ALL are cross-sectional co-occurrence, not evidence that service ratings drive loyalty.

Two aggregate tables were exported: `sfo_q7_cluster_profile.csv` and `sfo_q7_cluster_outcomes.csv`. (No respondent-level records were exported.)

Want me to try a k-selection sweep, add Q7ALL as a feature, or pursue the shape-based segmentation instead?