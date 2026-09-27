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
  "files": ["data/private/my-survey.csv", "data/private/my-dictionary.md"]
}
```

Use forward slashes, double quotes, and no trailing commas. Filenames must match
exactly. Every file in this list is uploaded when the first question is sent.
Avoid giving two files the same basename. The prompt should describe the files
actually selected, not a dataset from an earlier version of the project.

Stop and restart the app after changing files, configuration, or instructions.
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
