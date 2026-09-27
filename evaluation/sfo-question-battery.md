# Full SFO research-assistant question battery

All **34 original questions across 10 categories** appear below, followed by four
wording variants preserved from the retired R runner. Use the [running guide](../docs/06-running-the-question-battery.md)
and [scorecard](scorecard-template.md) to evaluate them. These are test inputs, not claims that the current app passes.

Question wording is preserved; only inconsistent surrounding quotation marks and
punctuation outside those marks were removed. The [source notes](source/original-question-notes.txt)
are included unchanged. The original explanatory notes are historical; verify their
data counts against your source files. Review criteria below were added for this tutorial.

## 1. Fact lookup

**Review criteria:** Compute from the CSV with dictionary-validated codes. State valid n, exclusions, denominator, and weighting. Deliver an actual plot when requested; prose alone is insufficient.

### SFO-01

> Give me the mean rating of restroom cleanliness

### SFO-02

> I need a plot that gives me the weighted frequency of the responses to the general satisfaction question.

### SFO-03

> What percentage of respondents rated SFO's free wifi as a 5 (outstanding)?

### SFO-04

> What is the average rating for restroom cleanliness at SFO?

### SFO-05

> What is the weighted distribution of responses to the overall satisfaction question?

## 2. Judgment and synthesis

**Review criteria:** Gather computed evidence, distinguish recommendations from findings, and explain the reasoning. Label outside knowledge and avoid unsupported causal claims.

### SFO-06

> What's your recommendation SFO do to improve traveler experience?

### SFO-07

> Based on this survey, what would you tell SFO's leadership team is the single biggest opportunity for improvement?

### SFO-08

> Is SFO doing a good job overall, in your view?

## 3. Hybrid: define, then compute

**Review criteria:** State an operational definition before computing. Explain judgment calls, calculate from the relevant fields, and offer to recompute under another definition.

### SFO-09

> What share of the sample would you say is overall happy with SFO?

### SFO-10

> How loyal are SFO's passengers, based on how likely they are to recommend it?

### SFO-11

> Would you say wifi at SFO is a strong point or a weak point?

## 4. Comparative

**Review criteria:** Validate group definitions, compute both groups, report unweighted subgroup n and weighting, and apply small-cell rules. Explain what meaningful means; do not infer significance from different point estimates alone.

### SFO-12

> How does satisfaction differ between residents and visitors?

### SFO-13

> Is there a meaningful difference in NPS between people who used TSA PreCheck and those who didn't?

### SFO-14

> Do Clear members rate their SFO experience differently than non-members?

## 5. Causal why

**Review criteria:** Check the premise with evidence. Separate associations and explicitly labeled hypotheses from causal conclusions. Do not claim this cross-sectional survey establishes causes.

### SFO-15

> Why is retail rated lower than food?

### SFO-16

> Why do some passengers report problems with security screening?

### SFO-17

> Does using TSA PreCheck cause higher satisfaction with SFO overall?

## 6. Out of scope

**Review criteria:** Explain the specific missing years, forecast evidence, or other-airport data. Do not invent trends, predictions, or benchmarks; an appropriate refusal passes.

### SFO-18

> How has this changed since COVID?

### SFO-19

> What's the trend over the last 5 years?

### SFO-20

> What will passenger satisfaction look like in 2027?

### SFO-21

> How does SFO's satisfaction compare to other major US airports?

## 7. Exploratory

**Review criteria:** Inspect multiple candidate patterns and show the scope of exploration. Support the chosen finding with fresh computations and subgroup checks rather than generic commentary.

### SFO-22

> What's the most interesting thing in this data?

### SFO-23

> Surprise me -- what's a finding in this data I might not expect?

### SFO-24

> What's the biggest gap between how residents and visitors experience SFO?

## 8. Metadata and methodology

**Review criteria:** Use the dictionary or other provided documentation. Explain definitions and codes accurately; admit when methodology is absent. Do not fill documentation gaps with guesses.

### SFO-25

> How was this survey conducted?

### SFO-26

> What's Q7ART mean?

### SFO-27

> What does the NETPRO variable measure?

### SFO-28

> What counts as a 'problem' in this survey, and how is it recorded?

## 9. Segmentation and advanced analytics

**Review criteria:** Clarify unscoped segmentation before selecting inputs. For scoped analysis, compute and disclose variables, missing-value treatment, scaling, algorithm, seed, and group sizes. For named segments, cross the requested variables and check cell sizes.

### SFO-29

> What distinct customer segments do you see?

### SFO-30

> Perform a K-means clustering on these data?

### SFO-31

> Cluster respondents into 3 groups based on their Q7 service ratings, using a fixed random seed.

### SFO-32

> Segment passengers by trip purpose and residency and tell me which segment is least satisfied.

## 10. Download or display

**Review criteria:** Deliver an accessible artifact and verify it against the calculated data. For the CSV, apply AND across all six requested ratings and check export policy. For the chart, validate grouping, labels, scale, weighting, and sample sizes.

### SFO-33

> I want a .csv file of the respondent records that gave the lowest rating (unacceptable) to *all* of the following measures: artwork, concessions, signage, vertical transportation, information displays, and restroom cleanliness.

### SFO-34

> Give me a bar chart showing the distribution of total satisfaction by male and female travelers.

## Additional wording from the historical runner

These four prompts are retained for historical coverage and wording-sensitivity tests.
The [historical mapping](historical-question-map.md) reproduces the full 29-question order.

### HIST-01 — Fact lookup

> What is the mean overall satisfaction score?

**Review criteria:** Compute from the CSV with dictionary-validated codes. State valid n, exclusions, denominator, and weighting. Deliver an actual plot when requested; prose alone is insufficient.

### HIST-02 — Judgment and synthesis

> What's your recommendation for what SFO should do to improve traveler experience?

**Review criteria:** Gather computed evidence, distinguish recommendations from findings, and explain the reasoning. Label outside knowledge and avoid unsupported causal claims.

### HIST-03 — Segmentation and advanced analytics

> What distinct customer segments do you see in this data?

**Review criteria:** Clarify unscoped segmentation before selecting inputs. For scoped analysis, compute and disclose variables, missing-value treatment, scaling, algorithm, seed, and group sizes. For named segments, cross the requested variables and check cell sizes.

### HIST-04 — Segmentation and advanced analytics

> Perform a K-means clustering on these data.

**Review criteria:** Clarify unscoped segmentation before selecting inputs. For scoped analysis, compute and disclose variables, missing-value treatment, scaling, algorithm, seed, and group sizes. For named segments, cross the requested variables and check cell sizes.
