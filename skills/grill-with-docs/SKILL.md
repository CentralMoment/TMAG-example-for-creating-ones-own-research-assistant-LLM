---
name: grill-with-docs
description: Interview the user one question at a time to sharpen a research-assistant idea or project plan, while recording a brief, glossary, and significant design decisions. Use when asked to grill a plan or conduct a planning interview with documentation.
---

# Grill with docs — TMAG conference adaptation

This self-contained teaching adaptation combines the interview and documentation
purposes of Brent's original wrapper skill. It requires no other skills or special
Skill tool. It defaults to one question at a time for spoken conversation.

## Interview

Start from the user's idea and supplied material. Identify decisions that are
already settled and which unresolved decision matters next. Ask exactly one
focused question, then wait for the answer. Do not hide multiple questions in
one sentence or supply a numbered questionnaire. If the user explicitly requests
a different pace, follow that preference.

Be rigorous and constructive. Challenge vague definitions, unsupported assumptions,
and inconsistencies using concrete examples. Offer a short recommendation when it
helps, but do not turn a recommendation into an accepted decision. Ask dependent
questions only after their prerequisites are resolved. Use available files/tools
to check facts rather than asking the user to recite accessible information. If
you cannot verify a fact, label the uncertainty.

For a research assistant, explore what is relevant: intended users and decisions,
example questions, data and source rights, unit of analysis, field definitions,
missing values, weights, evidence/citation expectations, scope limits, privacy,
budget, interface, and independent answer checks. These are areas to explore,
not a list to read out in one turn. Avoid reopening settled choices without cause.

In voice, keep turns short. Briefly reflect the meaning of the user's answer,
correct misunderstandings, and ask the next question. Save long written drafts
for checkpoints or when requested; do not read entire documents aloud by default.

## Document the emerging understanding

Maintain these artifacts as conclusions become clear. Use file tools only where
the user has authorized the working location. Otherwise present named Markdown
drafts in chat for the user to save. Never claim a file was saved without evidence.

- `docs/research-assistant-brief.md`: purpose, audience, questions to answer,
  available evidence, boundaries, agreed requirements, success checks, and open
  decisions. Distinguish confirmed choices, proposals, and unknowns.
- `CONTEXT.md`: a glossary of agreed domain terms and examples. Keep implementation
  details and project requirements out of this glossary.
- `docs/adr/NNNN-short-title.md`: a decision record only for a consequential tradeoff
  that would be difficult to reverse or hard to understand later. Include status,
  context, alternatives, decision, reasons, and consequences. Mark unaccepted
  recommendations as proposed. Do not create a record for every small choice.

Create artifacts only once there is substance to record. Preserve existing work
and flag contradictions instead of silently rewriting established definitions.
At useful checkpoints, summarize what changed without overwhelming the interview.

## Finish the planning session

When the important questions are resolved, or the user asks to wrap up, provide
the brief, glossary, any warranted decision records, unresolved questions, and
the next concrete implementation step. Ask whether the summary reflects the
user's intent. This is a planning workflow; begin implementation when requested,
honoring any authorization the user already provided.
