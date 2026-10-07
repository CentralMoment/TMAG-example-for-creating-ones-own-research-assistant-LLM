# Create your own research assistant

## 1. Write a small research brief

In a local note, answer: who will use this, what decisions will it support, what
five questions must it answer, and what must it decline? Identify the unit of
analysis (person, transaction, study, observation), dates, population, and coverage.
Start with a small dataset you are allowed to upload.

## 2. Prepare data and a dictionary

Place your CSV and dictionary in `data/private/`. Give columns stable names and
document each field's meaning, units, response codes, missing values, and valid
range. Include weights and their purpose, filters, denominator rules, known
limitations, source, date, and ownership. Explain multiple-response fields so
the assistant does not assume their percentages must sum to 100%.

### Define recurring measures before loading the data

If your project has a global definition of "satisfaction," "loyalty," "high value,"
or another recurring concept, decide its meaning ahead of time and add a derived
variable to the analysis dataset. Do the same for predefined segments, composite
scores and eligibility flags. Otherwise, you leave the definition to whichever
LLM you use and its interpretation of the question. It may choose a different
threshold, item, composite or denominator from one query to the next.

For example, an analyst could define **satisfied = Q7ALL is 4 or 5**:

| Source Q7ALL | Derived `satisfied` | Meaning |
|---|---|---|
| 4 or 5 | 1 | Meets the project's satisfaction definition |
| 1, 2 or 3 | 0 | Does not meet that definition |
| Blank, BLANK, 0 or 6 | Missing | No valid overall rating; exclude from the valid-answer denominator |

This is a proposed project definition, not an official SFO measure or a new column
already present in the supplied files. Missing answers must not become zeroes.
Under this definition, the SFO reference is 2,059 satisfied out of 2,625 valid
answers (78.4381% unweighted), with 184 missing. Weighting changes the estimate,
not the respondent-level definition of `satisfied`.

To implement a fixed definition in your own project:

1. Agree on the source fields, formula, thresholds, eligibility and missing-data
   rules with the research owner. For a composite, also specify item direction,
   item weights and the minimum number of answered items.
2. Calculate the new column in a reproducible R or Python preparation script.
   Preserve the original file and save a separate prepared dataset; do not ask
   the LLM to recreate this variable independently for every question.
3. Add the variable to the dictionary with its exact definition, codes, exclusions,
   version and derivation script. For `satisfied`, use valid codes 0 and 1, and
   document that zero is a valid answer while missing is excluded.
4. Point both `data_file` and the matching entry in `files` at the prepared CSV.
   Update the dictionary, field profile and expected column count. Approve the
   percentage statistic for `satisfied`, using success code 1 and valid codes
   [0, 1], so the fixed calculator can use the stored variable.
5. In the assistant instructions, map "satisfaction" to this authoritative column
   and definition. Require the assistant to use it across questions and fresh
   conversations. An explicitly requested alternative must be named as a separate
   measure; it must not silently replace the global definition.
6. Check the derived column against its source, including boundary and missing
   cases. Compare independent counts and weighted/unweighted percentages. Test
   differently worded questions and fresh sessions, then restart the app with
   the updated inputs. Version the data, dictionary, profile and instructions
   together whenever the definition changes.

A predefined column makes the definition stable and inspectable. It does not
guarantee that the model will select the right field or describe it accurately;
verify the field, filters, denominator and weighting in the calculation evidence.

For documents, include readable source text and a source index. This app does not
implement an indexed literature search or page-level citation verification; do
not promise those capabilities merely by uploading PDFs. Scanned documents may
need OCR and separate checks. Large collections require a different design.

## 3. Write your assistant's instructions

Copy `prompts/practice.md` to `prompts/my-research.md`. Replace the fictional
survey description with your research brief and file descriptions. Remove every
SFO-specific assumption if using the SFO prompt as a starting point. Include:

- Which files are authoritative and how to cite fields or sources.
- What must be computed and what may be interpretive judgment.
- Treatment of missing values, weights, exclusions, and sample sizes.
- Definitions of important concepts and when to ask for clarification.
- Limits on time comparisons, causality, individual identification, and small groups.
- How to respond when evidence is unavailable or computation fails.

Do not simply write "be accurate." Give observable requirements such as "show
valid n and the denominator for every percentage." Agree on suppression thresholds
with the research owner; the example's 20/30/50 thresholds are project conventions.

## 4. Point the app at your files

Edit `config.json` with a text editor. For example:

```json
{
  "title": "My customer research assistant",
  "description": "Customer survey, one wave, 2026",
  "prompt_file": "prompts/my-research.md",
  "profile_file": "profiles/my-research.json",
  "data_file": "data/private/my-survey.csv",
  "dictionary_file": "data/private/my-dictionary.md",
  "files": ["data/private/my-survey.csv", "data/private/my-dictionary.md"]
}
```

Use forward slashes, double quotes, and no trailing commas. Filenames must match
exactly. Every file in this list is uploaded when the first question is sent.
Avoid giving two files the same basename. The prompt should describe the files
actually selected, not a dataset from an earlier version of the project.

Stop and restart the app after changing files, configuration, or instructions.
Copy `profiles/practice.json` as a starting profile and review every field, valid
code, missing code, allowed statistic, ID column, weight column and expected shape.
Remove or update the SFO-specific paragraph in the shared `prompts/research-policy.md`
for a non-SFO dataset. Do not assume copying the SFO prompt alone customizes the app.
This avoids mixing old uploads/conversation context with a new dataset. Run the
setup checker again, then independently validate at least three statistics for
your new data. Its built-in numerical assertions cover only the practice fixture.

## 5. Use a coding assistant to help you build

These reusable prompts describe bounded tasks; they are examples rather than a
record of the original project's conversations. Share only approved data.

> Inspect my CSV header and dictionary. Explain the unit of analysis, available
> measures, missing-value codes, weights, and questions this dataset cannot answer.
> Identify uncertainties before recommending a design.

> Help me adapt prompts/my-research.md for these five questions: [insert questions].
> Require fresh computation for numeric claims, explicit assumptions, source names,
> valid sample sizes, and an honest response when evidence is unavailable.

> Create an evaluation table with ten questions, independently computed expected
> answers or observable behavior, and pass/fail criteria. Include a small subgroup,
> an ambiguous term, an unsupported trend, and a causal question.

> Review this app and explain which research rules are merely prompt instructions
> and which are actually enforced in code. Do not claim prompt compliance is guaranteed.

Use the [full SFO battery](../evaluation/sfo-question-battery.md) as a concrete
example of that evaluation design. Preserve the ten kinds of questions when
adapting it, then replace SFO fields and assumptions with your own. Follow the
[running guide](06-running-the-question-battery.md) for independent references,
fresh conversations, repeat trials, and grading.

## 6. Keep a reproducible record

Record dataset version/hash, prompt version, model identifier, package versions,
questions, exclusions, reference computations, and evaluation results. Save local
outputs under `output/` (ignored by Git). Preserve meaningful changes with Git
commits, reviewing staged files before every push. Do not commit raw private data,
keys, uploaded-file IDs, or transcripts just because `.gitignore` exists.

## 7. Share carefully

This starter binds to your own computer and has no authentication or per-user
budget controls. Before hosting, implement login, user/file isolation, spending
limits, remote-file cleanup, retention choices, and operational monitoring.
Evaluate statistical reliability separately from software availability. A shared
public demo should start with synthetic data and an explicit usage budget.
