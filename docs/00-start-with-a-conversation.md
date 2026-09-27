# How I began: ChatGPT, grill-with-docs, and voice

My first step was to open the ChatGPT app and talk through what I wanted to build.
I used `grill-with-docs` to help interrogate the idea and ChatGPT's voice mode to
have the conversation. The instruction that made it work was simple:
**Ask me one question at a time, and wait for my answer.**

It is almost surreal. You say what you are thinking, hear a thoughtful follow-up,
and discover an assumption you had not quite put into words. You can clarify,
change your mind, and keep talking. Asking the assistant to challenge you makes
the exchange especially useful: a vague ambition starts becoming something you
can actually build. For me, this is one of the most compelling ways to experience
what these tools can do.

This opening account reflects Brent's description of how the project began.
The prompts below are reusable examples, not a verbatim historical transcript.

## What the skill adds

A skill is a reusable set of instructions. `grill-with-docs` combines an exacting
planning interview with documentation: define the terms, clarify the decisions,
and capture the plan as it develops. Voice makes the interview conversational;
the written documents give you something concrete to carry into the build.

The original local skill is a short wrapper that invokes `grilling` and
`domain-modeling`. The original grilling component normally asks questions in
rounds; **one question at a time is the deliberate override for this workflow**.
The [conference version](../skills/grill-with-docs/SKILL.md) combines the behavior
in one portable file and makes that pacing the default. It is an adaptation,
not a claim that the original wrapper works unchanged in every application.

## Get the skill

Download [grill-with-docs.zip](../downloads/grill-with-docs.zip). On GitHub, open
that file and choose **Download raw file**. Or download and extract the whole
repository; the ZIP is in `downloads/` and its readable source is in
`skills/grill-with-docs/SKILL.md`.

The skill contains instructions only: no API keys, executable scripts, connector
requirements, or other skill dependencies. You do not need Python or the research
app's API key to conduct this planning interview. You do need access to the chosen
ChatGPT or Claude features through your own account.

## Option A: set it up in ChatGPT Work

Use the **ChatGPT desktop app** for this walkthrough. Standalone skill support
differs from plugin distribution and from ordinary file attachments.

1. Open a Work conversation. Attach `skills/grill-with-docs/SKILL.md` from your
   extracted repository (or paste its contents).
2. Select `@skill-creator` and send the setup prompt below.
3. Review the generated skill and complete the installation/enable step offered
   by the app. Open **Skills** in the sidebar and confirm `grill-with-docs` appears.
4. Start a new Work conversation, type `@`, and select `grill-with-docs`. Send the
   interview prompt in the next section. Check that it asks only one question.

```text
@skill-creator Set up a reusable, instruction-only skill named grill-with-docs
from the attached SKILL.md. Preserve its one-question-at-a-time interview,
research brief, glossary, and decision-record behavior. Help me install and
enable it in this app, then explain how to select it in a new Work conversation.
```

This uses the documented creator workflow rather than assuming that attaching
a ZIP automatically installs a skill. If the creator or Skills controls are
unavailable, check app updates and workspace permissions; use the fallback below.
For web/mobile distribution, OpenAI documents packaging skills in plugins.
See [OpenAI's skill setup guide](https://learn.chatgpt.com/docs/build-skills).

## Option B: install it for Claude Cowork

1. Open Claude and go to **Customize → Skills**.
2. Click **+**, then **Create skill**, then **Upload a skill**.
3. Select `downloads/grill-with-docs.zip` and complete the upload.
4. Ensure the skill is enabled. Start a Cowork task and ask it to use
   `grill-with-docs`, with the interview prompt below.
5. Confirm it asks a single question and can describe the documents it will maintain.

If upload or creation is missing, your organization's settings or role may
restrict it. Ask the workspace owner about enabling user-created skills. Claude
documents skill use in both chat and Cowork. See
[Anthropic's installation instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

The spoken experience described here is **ChatGPT Voice**. Installing the skill
in Claude does not install ChatGPT Voice; you can conduct the same interview in
Cowork using text or the input features your Claude app provides.

## Start the interview

Describe your rough idea. Attach an approved data dictionary or a small example
if available; an incomplete idea is enough to start. Try this prompt:

```text
Use grill-with-docs to help me design my own research assistant.
I want people to ask questions about my research data and receive answers
grounded in the evidence. I am still figuring out the details.

Ask me ONE question at a time, then wait for my answer. Do not give me a list
of questions. Challenge my assumptions and help me define vague terms.
Keep spoken replies short. Record agreed requirements in a research brief,
definitions in a glossary, and consequential tradeoffs in decision records.
Distinguish my decisions from your suggestions. Start with the most important
question about what I want this assistant to help people do.
```

## Turn on ChatGPT Voice

In the ChatGPT desktop app, choose **Start voice chat**, or **Start new voice
chat** for a new conversation. Allow microphone access and choose a voice if
prompted. Speak naturally and answer the first question. You can interrupt,
clarify, or redirect the discussion. Choose **Stop voice chat** when finished.
Use the live voice feature for the spoken back-and-forth; dictation only turns
speech into prompt text. Availability depends on your account, app rollout, and
workspace settings. [Official ChatGPT Voice instructions](https://learn.chatgpt.com/docs/features/voice).

If you must start a separate voice conversation, carry over the interview prompt
and current brief rather than assuming it knows another conversation's details.
If the assistant starts listing questions, say: **“Pause. Just one question.
Wait until I answer before asking the next one.”**

## Leave with a plan you can build

When the discussion has clarified the idea, ask:

```text
Summarize the plan we agreed on. Give me the research-assistant brief, the
glossary, any significant decision records, and the questions still unresolved.
Label suggestions that I have not accepted. Show me the documents so I can
check them before we begin building.
```

Look for an audience, useful example questions, available evidence, exclusions,
an agreed meaning of a good answer, and a way to check it independently.
The glossary should explain research concepts; decision records should explain
meaningful choices. Review names, field codes, dates, and numbers that may have
been misheard. When file writing is available, save the documents into your
project; otherwise copy the Markdown drafts from chat.

The conversation can feel extraordinary, but the useful result is a plan you
understand and can inspect. Use that plan to guide the next stage:
[build and run the first assistant](01-beginner-guide.md).

## If you cannot install skills yet

Open the [skill source](../skills/grill-with-docs/SKILL.md), copy the instructions
below its opening metadata, and paste them into a conversation. Ask the assistant
to follow them for this session, then send the interview prompt. This reproduces
the interview instructions for that conversation; it is not a persistent skill
installation. You can still try the one-question-at-a-time method.

Installation guidance was checked against the linked official documentation on
2026-09-26. The archive structure was validated locally; installation in attendees'
ChatGPT Work and Claude Cowork accounts has not been tested.
