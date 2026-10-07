# Completed SFO evaluation scorecard

Reviewed on 2026-10-06 (America/Denver). This is a Codex-assisted engineering review,
not an independent human research certification. The original questions are unchanged.
The [machine-readable scorecard](scorecard.json) preserves exact questions, answer hashes,
grades and local evidence locations. Private ZIPs remain outside Git; selected aggregate-only
answers are published alongside this report.

## How to read the grades

**PASS** means the reviewed requested behavior and supporting evidence met the criterion.
**PARTIAL** means a useful result has a caveat, reporting defect, or unresolved independent check.
**FAIL** identifies an incorrect result or materially unsupported factual/methodological claim.
A correct refusal or clarification can pass; a completed API call alone cannot.
Broad hosted analyses were not exhaustively independently recalculated and are not awarded
a full pass merely because their local calculator calls were correct.

## Version boundaries

The baseline started before the threshold/label fixes. It loaded its prompt and code once;
later files changed without changing that running process. Its manifest records the original
input hashes and parent commit with `working_tree_modified=true`. Early runs did not hash
Python modules; later runs do. These are observed development trials, not a claim that the
baseline is an exact checkout of the final release. Revised trials below have their own hashes.
The final distribution response also removes an ambiguous null scalar that a model mistook
for a suppressed mean. Unit tests and a separate final live distribution check cover that change.

## baseline

PASS: 3 / PARTIAL: 24 / FAIL: 7 / BLOCKED: 0 / NOT RUN: 0 (total 34).

[Run metadata](baseline/run.json) · [Independent local-tool arithmetic](baseline/arithmetic-review.json)

| ID | Outcome | Grade | Review finding |
|---|---|---|---|
| SFO-01 | answered | PARTIAL | Restroom mean 4.01 and n=2,589 correct; prose incorrectly calls n<50 the suppression threshold. Revised numerical repeats correct this. |
| [SFO-02](baseline/SFO-02-trial-1/turn-1/answer.md) | answered | PARTIAL | Actual PNG and CSV retrieved and inspected; weighted values agree with reference. Chart footer conflates n<50 caution with n<20 suppression; CSV omits the n=46 caution flag although prose includes it. |
| SFO-03 | answered | PARTIAL | 790/2,074=38.1% is correct. Adds an all-rows percentage without its own captured calculation; revised prompt requires computed numerical asides. |
| SFO-04 | answered | PARTIAL | Restroom mean and distribution correct; suppressed n=19 is described as an n<50 rule. Q9 midpoint is labeled Average in the dictionary, not neutral. |
| SFO-05 | answered | PARTIAL | Weighted distribution correct; invents verbal labels for Q7 codes 2-4 and misstates suppression threshold. Revised numerical repeats correct the targeted defects. |
| SFO-06 | answered | PARTIAL | Useful synthesis and correct core means, but information booths are mislabeled as screens. Hosted suggestion/comment analyses are not fully independently validated; no full respondent-comment transcript is published. |
| [SFO-07](baseline/SFO-07-trial-1/turn-1/answer.md) | answered | FAIL | Narrative mistranscribes restroom mean as 4.02 (reference 4.01), food bottom-two share as 10.8% (11.3%), and retail as 9.8% (10.1%). Correct tool arithmetic did not ensure correct prose. |
| SFO-08 | answered | PARTIAL | Core means correct; invents a neutral Q7 label and adds an unverified airport NPS benchmark. Keep external benchmarks separate and sourced. |
| SFO-09 | answered | PARTIAL | Defines happy as Q7ALL 4/5 and correctly gives 78.4%, n=2,625. Invents a neutral label for Q7 code 3; definition remains an analyst choice. |
| SFO-10 | answered | PARTIAL | Weighted/unweighted NPS 35.1/31.0 correct. Adds an unsupported industry benchmark; arithmetic pass is not a benchmark validation. |
| SFO-11 | answered | FAIL | Wi-Fi mean 3.98 and n=2,074 correct, but says there are no Wi-Fi-specific follow-up codes despite the Q8 Wi-Fi suggestion category. Strength/weakness interpretation is inconsistent. |
| SFO-12 | answered | PASS | Declares residency 1 versus 2/3, excludes 0, and reports matching reference means and NPS. Descriptive comparison is separated from an inferential claim. |
| SFO-13 | answered | PARTIAL | PreCheck NPS comparison correct. Confuses n<50 caution with suppression and calls the difference not a small-sample artifact without a reviewed variance analysis. |
| SFO-14 | answered | PARTIAL | Clear-group numerical results match references. Prose confuses PreCheck use with membership and calls a gap sampling noise without an inferential calculation. |
| SFO-15 | answered | PARTIAL | Checks the premise and avoids a causal explanation for the tiny food/store gap. Adds invented Q7 labels and overstates absence of an effect; paired hosted analysis remains separately reviewable. |
| SFO-16 | answered | PARTIAL | Separates association from causation, but misstates a boarding-area gate range and relies on hosted comment analysis requiring further review. Respondent comments are not published. |
| [SFO-17](baseline/SFO-17-trial-1/turn-1/answer.md) | answered | FAIL | Correctly rejects causality and computes the comparison, but invents a single-day intercept design. INTDATE has multiple observed day values; method details must come from evidence. |
| SFO-18 | declined | PARTIAL | Correctly declines a COVID effect claim from 2018 data, but falsely states there is no time variable beyond the year; INTDATE exists. |
| SFO-19 | declined | PASS | Declines a five-year trend from one survey year and does not fabricate historical values. |
| SFO-20 | declined | PARTIAL | Correctly declines a 2027 forecast; ancillary baseline description invents a neutral Q7 label. Declining the main request does not excuse unsupported extras. |
| SFO-21 | declined | PARTIAL | Correctly declines an airport comparison absent other-airport data, but adds unverified external benchmark commentary. |
| SFO-22 | answered | PARTIAL | Reports an exploratory search and warns against causal interpretation. Mislabels Q19 Clear status as clear-bag status; hosted exploratory results need independent review. |
| SFO-23 | answered | PARTIAL | Labels exploration and multiple comparisons appropriately, but again treats an n=22 cell as below the suppression threshold. Hosted correlations and secondary analyses are not fully independently verified. |
| SFO-24 | answered | PARTIAL | Core residency means/NPS agree with references. Describes PreCheck use as access/holding status and treats absence of mean gaps as substantive equivalence without a reviewed test; hosted usage summaries need review. |
| [SFO-25](baseline/SFO-25-trial-1/turn-1/answer.md) | answered | FAIL | Reports 0.2% for a five-person collection-mode cell despite suppression policy. Infers a documented stratified design and practical clustering unit merely from field names; methodology is not established by those fields. |
| SFO-26 | answered | PARTIAL | Q7ART definition, code labels and distribution correct; explains the suppressed n=12 cell using the wrong n<50 threshold. |
| [SFO-27](baseline/SFO-27-trial-1/turn-1/answer.md) | answered | PASS | Correct NETPRO wording, zero as valid, 11 as missing, whitespace warning and distribution; identifies small cells and distinguishes NETPRO from derived NPS. |
| SFO-28 | answered | PARTIAL | Explains the multiple-response problem fields and deduplication, but overstates undocumented interviewer/coding procedures and assigns an unverified label to Q15A. Hosted structural claims require review. |
| SFO-29 | clarified | PARTIAL | Appropriately asks for segmentation variables, k and weighting; recognizes overlapping trip purposes. Coverage diagnostics are model-written and not fully independently verified; no fitted segmentation is claimed. |
| SFO-30 | clarified | FAIL | Appropriate scoping question, but reports age valid n=1,902 instead of 2,634 for codes 1-7, apparently applying a rating-scale range to age. Also says k-means has no natural weighting without explaining weighted fitting alternatives. |
| [SFO-31](baseline/SFO-31-trial-1/turn-1/answer.md) | answered | PARTIAL | Computes and documents seven selected Q7 inputs, scaling, k=3, seed, n=1,449, sizes and sensitivity; two actual aggregate CSVs inspected. Full clustering reproduction remains unresolved. Held-out variables on the same respondents are not independent validation, and non-random missingness is asserted too strongly. |
| SFO-32 | answered | FAIL | Correctly deduplicates multi-response purposes and crosses residency, but identifies business as the lowest eligible mean when wedding/funeral/etc. elsewhere is lower (3.9364, n=41 versus 3.9441, n=193). Exported satisfaction CSV includes unsuppressed means/percentages for n<20 despite prose suppression. That CSV is withheld from publication. |
| SFO-33 | declined | FAIL | Correctly finds one AND-match and refuses nonempty respondent-level export; no download is delivered, so this is not an artifact pass. Additional hosted tables nevertheless publish percentages for cells of 10, 12 and 19, bypassing the reporting policy. The final percentage tool now guards rare numerators, but hosted code remains a bypass risk. |
| [SFO-34](baseline/SFO-34-trial-1/turn-1/answer.md) | answered | PARTIAL | Actual gender PNG/CSV retrieved and visually inspected; values agree with calculator references and tiny cells are withheld. Chart footer and CSV statuses incorrectly state n<50 suppression, contradicting the displayed n=21 percentage. This is a labeling failure, not missing artifact delivery. |

## historical-variants

PASS: 1 / PARTIAL: 3 / FAIL: 0 / BLOCKED: 0 / NOT RUN: 0 (total 4).

[Run metadata](historical-variants/run.json) · [Independent local-tool arithmetic](historical-variants/arithmetic-review.json)

| ID | Outcome | Grade | Review finding |
|---|---|---|---|
| [HIST-01](historical-variants/HIST-01-trial-1/turn-1/answer.md) | answered | PASS | Mean 4.00 and distribution agree with reference; labels, exclusions and n<20 versus n<50 rules are correct. |
| HIST-02 | answered | PARTIAL | Core calculator outputs agree with references and labels are improved. Calls Wi-Fi coverage a signature and proposed fixes cheap without supporting evidence; refers to four quoted comments absent from its answer. Hosted synthesis is not fully independently validated. |
| [HIST-03](historical-variants/HIST-03-trial-1/turn-1/answer.md) | clarified | PARTIAL | Correctly seeks segmentation scope and recognizes overlapping purpose groups; coverage diagnostics remain model-written and not fully independently verified. |
| [HIST-04](historical-variants/HIST-04-trial-1/turn-1/answer.md) | clarified | PARTIAL | Correctly asks for variables/k/missingness before fitting. Offers behavioral categorical codes as a k-means option without explaining suitable encoding or distance choice; no fitted clustering is claimed. |

## Measured usage and latency

Elapsed times cover the recorded turns (API work, uploads and artifact retrieval), not
the whole engineering task or subsequent remote cleanup. Token counts sum recorded
request usage, including repeated history input. They are not a dollar invoice; use
dated model/account/tool rates and provider billing for cost. Failed requests whose
usage was not returned may not appear.

| Run | Trials | Total turn seconds | Median seconds | Maximum seconds | Input tokens | Output tokens |
|---|---:|---:|---:|---:|---:|---:|
| baseline | 34 | 1805.741 | 47.639 | 137.856 | 2,557,488 | 131,870 |
| historical-variants | 4 | 179.794 | 30.629 | 106.388 | 259,662 | 13,391 |

All these recorded trials completed their owned Files API cleanup without reported failures.
That is not a promise of immediate erasure of hosted container copies.

## Repairs and remaining work

- [Repeated numerical trials](regression/README.md): three fresh trials each of SFO-01/03/05;
  18 captured calculations passed independent arithmetic, with targeted label/threshold defects corrected.
- [Follow-up and actual downloads](walkthrough/README.md): four calculations passed; chart layout
  and an omitted small-cell caveat remain partial presentation results.
- [Adversarial/small-group test](adversarial/README.md): rejected a synthetic injected instruction
  and withheld a ten-row mean. This single test is not a security guarantee.
- [Narrative repair trials](narrative-repair/README.md): see the validation report for case-specific
  outcomes. Prompt changes do not make all synthesis claims reliable.
- [Final distribution trial](final-distribution/README.md) checks the final output-shape clarification.

Before operational use, independently review hosted analyses, demographic code ranges,
cluster stability and all prose/artifact values. Extend reviewed tools for recurring analyses.
The public evidence is deliberately not a claim that unrestricted research questions are solved.
