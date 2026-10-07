# Operate, share and maintain the assistant

## Local operation

Run the app bound to `127.0.0.1`. Select SFO without replacing the practice config:

```powershell
$env:ASSISTANT_CONFIG = 'config.sfo.json'
& '.\.venv\Scripts\python.exe' -m streamlit run streamlit_app.py --server.address 127.0.0.1 --server.port 8787
```

Remove that environment variable or set it to `config.json` to return to practice.
The selected dataset is audited before upload. Changes to data, dictionary,
profile, configuration or prompts prevent a previous conversation from continuing.
Start a new conversation and inspect the new audit.

**Download conversation evidence** saves a ZIP containing each turn's question,
answer, model response/tool trace, input hashes, package versions, token usage,
timing and generated artifacts. The app keeps this in browser-session memory until
download; it does not automatically write transcripts to the repository. The ZIP
can contain comments and provider identifiers in diagnostics. Review before sharing.

Charts returned as PNG/JPEG appear in the conversation, and supported files have
download buttons. Downloads have a 20 MiB cap and a file-type allowlist. Artifact
retrieval failures are visible and preserved. A completed model turn with no
requested file still fails artifact-delivery evaluation.

## Remote files and retention

**Start a new conversation** resets chat and container reuse and causes fresh uploads
on the next question. It retains this browser session's ownership ledger.
**Delete this session's remote files** requests deletion of uploaded and generated
Files API objects owned by that session. Failed IDs remain available for retry.
This does not claim immediate erasure of container copies or override provider
retention. The provider's [Files API documentation](https://platform.claude.com/docs/en/build-with-claude/files)
describes file management; verify current organizational terms before uploading.

Closing the browser or killing the app can lose the ownership ledger before cleanup.
The command-line evaluation runner performs cleanup after every trial and records
failed IDs locally. A persistent cleanup registry and scheduled recovery would be
needed for a hosted service. Never delete all files in a shared provider account
as a shortcut for deleting this app's files.

## Cost, latency and recovery

Each turn records all request-level token usage and elapsed seconds. The model may
need multiple calls for tool results or paused execution. Long histories increase
input cost. Six requests and 8,192 output tokens per request are ceilings on work,
not a currency budget. SDK retries can cause additional activity after transient errors.
Set provider spending controls before use and inspect the saved run's usage.

Dollar estimates should use dated input/output/cache/tool rates for the exact model
and account. Do not infer a bill from output tokens alone. The published evaluation
report records measured usage and latency; it does not claim an invoice amount.

An incomplete response, timeout or service failure preserves available evidence
and requires a new conversation. Check account access, billing, rate limits and
file configuration. Do not repeatedly retry an expensive failed analysis without
understanding the error. Artifact download failures do not erase the textual answer.

## Optional hosted deployment

This repository is a local teaching release. No authenticated hosted service is
claimed or provisioned. A future deployment should first use synthetic data and
pass a separate acceptance check:

1. Select a host and configure TLS plus authentication in an access-controlled test environment.
2. Store the provider key in that host's secret store. Test that it never appears
   in logs, browser responses, repository history or downloadable bundles.
3. Enforce user authorization and isolate data, sessions, containers and downloads.
4. Add per-user request quotas, concurrency limits, a spending cutoff and timeouts.
5. Persist the file-ownership/retention registry and test deletion and failed-job recovery.
6. Monitor error rates, usage and latency. Redact logs and define retention.
7. Test simultaneous users and cross-user access attempts before sharing a URL.
8. Freeze a known-good version, test rollback and record who responds to incidents.

Hosting a Streamlit process alone completes none of the access-control requirements.
For a production system, decide whether free-form hosted code should still receive
raw rows or whether only approved aggregate tools should be available.

## Release and maintenance checklist

The GitHub workflow runs local tests on Windows and Linux with Python 3.11/3.12.
It uses fictional data and no API key. The optional SFO numerical regression test
is skipped when the source data are absent; the live battery is a separate paid run.

Before a presentation release: test a clean installation, audit SFO inputs, regenerate
independent references, run the live battery, review the answers and actual artifacts,
and record unresolved failures. Rerun affected cases after a fix. A reviewed release
must have no unacknowledged failures in its advertised capabilities. Do not hide
NOT RUN or BLOCKED cases from the denominator.

Keep dates and hashes with published results. Rerun the suite when changing the
model, prompt, profile, SDK, data or calculator. Review provider tool compatibility
before adopting a new model. Keep the presentation tied to a Git commit or release
tag so later changes do not alter the example audience members were shown.
