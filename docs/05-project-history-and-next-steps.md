# Where this example came from

The source workspace contains an earlier R/plumber analytics engine and a current
Python/Streamlit app. The R engine is explicitly marked retired on 2026-09-04.
It had a planner, query DSL, compiler, executor, semantic catalog, and policy gate.
The current app instead delegates computation to Claude's hosted code execution.

The teaching repository starts with the current approach. It preserves its key
research ideas: fresh computation, explicit definitions, unweighted subgroup n,
weighting choices, limited causal inference, and honest dataset boundaries.
It separates the prompt and file configuration from the UI, adds fictional data,
local setup checks, a chat reset, bounded pause continuation, and input checks.
The SFO summary JSON, legacy engine, and historical evaluation artifacts are not
required to run this version and are not included.

The source planning document proposed Render hosting. The observed current app
is a local Streamlit application; this tutorial does not claim that hosting was
completed. Historical R-engine results do not establish correctness of this app.

## Suggested next development steps

1. Run live API checks against the fictional data and record model access and cost.
2. Validate the SFO source downloads and independently compute reference results.
3. Evaluate SFO questions against the current app, including follow-up turns.
4. Decide on a software license and intended repository visibility.
5. Add enforceable statistical checks where prompt compliance is insufficient.
6. Add authenticated hosting only after data handling and usage controls are designed.

## Technical references

- [Anthropic code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool): hosted execution, file attachments, containers, and compatibility.
- [Anthropic Files API](https://platform.claude.com/docs/en/build-with-claude/files): uploading and managing remote files.
- [Streamlit documentation](https://docs.streamlit.io/): app development and operation.
- [Python virtual environments](https://docs.python.org/3/library/venv.html): isolated local dependencies.

API details change. The code-execution request structure was checked against
official documentation when this starter was prepared on 2026-09-26. The default
model is retained from the source project, not a guarantee of account access.
