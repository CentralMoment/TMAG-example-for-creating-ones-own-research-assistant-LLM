# Statistical policy and enforcement boundaries

The policy describes this example's analytic choices. Review it before adopting it
for a different survey. The machine-readable field profile is part of the evidence
hashes, and the shared research prompt is in `prompts/research-policy.md`.

## What the estimate describes

An unweighted statistic describes responding records with a valid answer. A weighted
statistic applies the survey's WEIGHT column to those same valid records. It does
not establish coverage of every traveler or correct all nonresponse bias. Do not
label the sum of normalized weights as the number of passengers in the population.

Explicit requests for weights take precedence. Population-worded questions use
weights; sample-worded and unqualified descriptive questions use unweighted
results. State the choice. If an interpretation matters, show both or clarify.

Every answer must identify the source field, analytic definition, filters, valid
response codes, exclusions, weight mode and unweighted valid n. Denominators default
to valid answers to the specific item after filtering. An all-respondents denominator
is a different estimand and must be requested and labeled explicitly.

## Missing answers and scales

Q7 and Q9 ratings use codes 1–5. Code 6 is not applicable and 0 is blank. The CSV's
Q7ALL column also contains literal `BLANK`. Do not average them. Q9Restroom's endpoints
are Dirty and Clean; Q7's are Unacceptable and Outstanding. Intermediate unlabeled
codes must not be given invented dictionary labels.

NETPRO includes zero as a valid score; 11 is blank. Trim header whitespace, including
`NETPRO  `, but preserve original input files. NPS is a derived measure, not the mean
NETPRO score. Means of ordinal ratings are descriptive conventions. Include or
inspect the distribution before treating a mean as a complete account of experience.

Do not impute missing survey answers by default. Report exclusions. Missingness
may be informative; an estimate among people who rated wifi is not necessarily an
estimate among all respondents or all wifi users.

## Groups and uncertainty

Q17LIVE=1 defines Bay Area residents in this example. Codes 2 and 3 define people
living elsewhere; exclude 0. Q11TSAPRE=1 versus 2 compares reported PreCheck use and
nonuse; do not fold "don't know" or "did not go through security" into No.

Q2PURP1/2/3 are multiple-response slots. Count each person once per selected purpose,
then cross purpose with residency. Groups may overlap. Do not present them as an
exclusive partition or add their percentages as though they sum to 100%.

The local calculator withholds summary statistics for n<20, adds strong caution
for n<30 and caution for n<50. Distribution cells use the same count thresholds;
their weighted frequencies and percentages are withheld when n<20. Counts remain
visible. A percentage request also withholds the percentage when its numerator
cell has fewer than 20 observations, matching the distribution rule. Counts remain
visible. This is a reporting/reliability convention, **not a privacy guarantee**:
counts, totals, repeated filters and other outputs can disclose information.

Different means do not prove statistical significance or practical importance.
The supplied dictionary does not provide a complete reviewed variance-estimation
design. Do not fabricate design-based confidence intervals. A future inferential
extension needs the sampling units, strata/cluster interpretation, weight rationale,
variance method and target estimand verified by a researcher. Merely seeing columns
named STRATA or RUNID does not establish how to use them in survey inference.

## Exploration, recommendations and clustering

State which comparisons were searched. Treat the largest observed gap as exploratory,
not a confirmed effect; searching more gaps creates more opportunities for chance
findings. Confirm consequential hypotheses in independent data or an agreed analysis.
For recommendations, distinguish the measured weakness, possible explanation, and
proposed action. This cross-sectional dataset does not establish intervention effects.

For k-means, record variables, complete-case exclusions or other missingness treatment,
scaling, k, seed, implementation and group sizes. Inspect stability under alternate
seeds and reasonable preprocessing before treating groups as useful segments. A
single fitted clustering is a worked exploratory output, not validated segmentation.

## What is actually enforced?

| Requirement | Mechanism | Limit |
|---|---|---|
| Reviewed schema/codes, unique IDs, positive finite weights | Pre-upload audit | Covers configured fields, not all methodology |
| Valid denominators and small-group rules | Local survey_statistic code | Applies to this tool's results |
| Input changes cannot silently reuse old state | Input hashes and session check | Restart/new conversation still needed |
| Bounded tool loop | Six API requests per turn, 8,192 output tokens each | Not a dollar-spend cap |
| Causality, source attribution, row-export rules | Prompt and evaluation | Model behavior; not an enforcement boundary |
| Correct prose and interpretation | Independent reference and reviewer | No automatic guarantee |

Hosted Python can bypass the local calculator, and a model can misstate its result.
For private production use, put sensitive data behind an approved aggregate-only
service and enforce disclosure rules there. Do not upload row-level private data
to this teaching app on the assumption that its prompt provides that protection.
