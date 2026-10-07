# Research brief and design decisions

This is a reconstruction from the implemented project, updated for the teaching
release. It is not a transcript of Brent's original voice interview. The
[planning interview](00-start-with-a-conversation.md) is a way to create these
artifacts for your own project.

## Research brief

**Audience:** researchers and decision makers who want to ask questions of a
customer survey without writing every calculation themselves. Conference readers
should also be able to reproduce the example and inspect how answers were checked.

**Purpose:** shorten the path from a research question to an inspectable descriptive
answer. The assistant supports investigation; a research owner reviews externally
reported conclusions. Its scope is the 2018 SFO survey, one respondent per row.

**Must answer:** overall ratings, valid-answer percentages, explicitly defined
subgroup comparisons, questions about the dictionary, and recommendations grounded
in computed findings. Examples are preserved in the full question battery.

**Must distinguish:** observations from recommendations, sample descriptions from
weighted estimates, and unavailable evidence from a result of zero.

**Must decline or clarify:** unsupported trends and causality, individual profiling,
nonempty respondent-level exports, and clustering without specified inputs or an
analytic objective. Raw-data privacy for a future client deployment needs a
separate approved design; this local teaching app is not a disclosure-control system.

**Evidence:** original CSV and XLSX dictionary. Reviewed field definitions live in
`profiles/sfo.json`. Reference answers and evaluation grades are deliberately kept
out of uploaded inputs. The meaning of the undocumented Q15A column remains a
source-documentation limitation; comments must not substitute for representative counts.

**Success:** an attendee can install the app, reproduce known calculations, inspect
the calculation and denominator, obtain requested artifacts, and understand the
remaining failure cases. A release's scorecard must show failures as well as passes.

## Working glossary

| Term | Meaning in this example |
|---|---|
| Respondent | One survey record with a unique RESPNUM |
| Valid n | Unweighted number of included answers after filters and response-code exclusions |
| Weighted estimate | Statistic using the provided WEIGHT values; its base n still counts people |
| Overall satisfaction | Operational shorthand for Q7ALL, the airport-as-a-whole rating |
| Happy | A declared analytic definition, usually Q7ALL 4 or 5; not a separate measured emotion |
| Resident | For this example, Q17LIVE=1, the nine-county Bay Area |
| Elsewhere / visitor | Q17LIVE=2 or 3; a residency grouping, not a verified trip-status measure |
| NPS | 100 times the share of valid NETPRO scores 9–10 minus the share 0–6 |
| Trusted calculation | Fixed local code with reviewed field definitions and boundary tests |
| Hosted calculation | Python written by the model and run by the provider; requires independent review |
| Evidence bundle | Question, answer, tool calls/results, hashes, usage, timing and generated files |

## Why this architecture?

The main task is aggregation across structured rows. Text retrieval cannot itself
count all qualifying respondents. A precomputed summary cannot anticipate every
combination of filters. The example therefore uses a model to interpret questions,
a small local calculator for reviewed descriptive operations, and hosted Python
for analyses and artifacts outside that calculator's scope.

The original R pipeline had a planner, query language, compiler and policy gate.
Moving to hosted execution reduced custom infrastructure and broadened exploratory
analysis, but removed that deterministic boundary around all analytics. This
release restores a narrow, inspectable calculator rather than implying that prompt
instructions replaced enforcement. The model can still use hosted code and write
incorrect prose. Passing a calculator test does not certify the entire answer.

No vector database, fine-tuning, autonomous agent team or additional provider is
needed for this example. Revisit retrieval if the task becomes searching a large
document collection, and revisit a controlled analytics backend if enforceable
access or disclosure restrictions become a requirement.

## Decisions for readers adapting the example

Choose a dataset and five important questions before changing tools. Agree on
definitions, defaults and exclusions with the research owner. Keep authoritative
data unchanged. Write an independent reference calculation before evaluating the
model. Define measurable acceptance criteria before looking at its answers.
Keep a record of each important change and the evidence that motivated it.

The maintainer owns code and dependency changes. A research owner owns definitions,
permitted uses and interpretation. These can be the same person for a local demo;
write down who has each responsibility when adapting this to a client project.
