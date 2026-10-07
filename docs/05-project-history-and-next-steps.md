# Where this example came from

Brent began by using the ChatGPT app, `grill-with-docs`, and ChatGPT Voice to
talk through the idea one question at a time. The
[opening chapter](00-start-with-a-conversation.md) teaches that planning workflow
and provides a portable conference adaptation of the skill. The implementation
history below describes the later code found in the source workspace.

The source workspace contains an earlier R/plumber analytics engine and a current
Python/Streamlit app. The R engine is explicitly marked retired on 2026-09-04.
It had a planner, query DSL, compiler, executor, semantic catalog, and policy gate.
The current app instead delegates computation to Claude's hosted code execution.

The teaching repository starts with the current approach. It preserves its key
research ideas: fresh computation, explicit definitions, unweighted subgroup n,
weighting choices, limited causal inference, and honest dataset boundaries.
It separates the prompt and file configuration from the UI, adds fictional data,
local setup checks, a chat reset, bounded pause continuation, and input checks.
The SFO summary JSON, legacy engine, and historical answer/grade artifacts are not
required to run this version and are not included. The original question notes
and full question battery are now included under `evaluation/`, along with the
complete 29-question historical run mapping. See the
[running guide](06-running-the-question-battery.md) to evaluate the current app.

The source planning document proposed Render hosting. The observed current app
is a local Streamlit application; this tutorial does not claim that hosting was
completed. Historical R-engine results do not establish correctness of this app.

## Teaching release improvements

The repository now includes verified source downloading, an input audit, independent
numerical references, a reviewed local statistics tool, generated-file retrieval,
evidence export, remote-file cleanup and an automated live battery runner. Code
and original documentation are licensed under Apache 2.0. The completed research
brief and statistical policy explain the decisions behind these changes.

See [validation](VALIDATION.md) for observed results and unresolved limitations.
Future work includes independent human review, inferential survey methods where
the design is documented, and authenticated hosting after data handling and usage
controls are designed. A passing local test suite is not a production release gate.

## Technical references

- [Anthropic code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool): hosted execution, file attachments, containers, and compatibility.
- [Anthropic Files API](https://platform.claude.com/docs/en/build-with-claude/files): uploading and managing remote files.
- [Streamlit documentation](https://docs.streamlit.io/): app development and operation.
- [Python virtual environments](https://docs.python.org/3/library/venv.html): isolated local dependencies.

API details change. The code-execution request structure was checked against
official documentation when this starter was prepared on 2026-09-26. The default
model is retained from the source project, not a guarantee of account access.
