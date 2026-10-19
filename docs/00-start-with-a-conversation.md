# Begin with TMAG-LLM-grill-skill and a conversation

My first step was to open the ChatGPT app and talk through what I wanted to build.
I used a planning interview and ChatGPT's voice mode to have the conversation.
This guide uses my **TMAG-LLM-grill-skill** (`tmag-llm-grill-skill`) to help
you define your own research assistant. The instruction that made the conversation
work was simple:
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

A skill is a reusable set of instructions. This skill helps market research and
market intelligence professionals turn research questions, data, and methodological
judgment into a testable specification. It assumes research expertise, without
requiring programming or machine-learning expertise.

The [complete skill](../skills/tmag-llm-grill-skill/SKILL.md) is self-contained:
it requires no other skills, particular provider, paid service, or example project.
One focused question and one decision per turn is its default. It inspects available
source material, challenges assumptions, distinguishes proposals from agreements,
and records the plan as decisions become clear.

Relevant branches cover surveys, listings and observational records, interviews
and open-ended responses, reports, and multiple studies or waves. It separates
reproducible calculations from retrieved examples and asks how answers will be
checked independently. It does not prescribe this tutorial's technical stack.

## Get the skill

Download [tmag-llm-grill-skill.zip](../downloads/tmag-llm-grill-skill.zip). On GitHub, open
that file and choose **Download raw file**. Or download and extract the whole
repository; the ZIP is in `downloads/` and its readable source is in
`skills/tmag-llm-grill-skill/SKILL.md`.

The skill contains instructions only: no API keys, executable scripts, connector
requirements, or other skill dependencies. You do not need Python or the research
app's API key to conduct this planning interview. You do need access to the chosen
ChatGPT or Claude features through your own account.

## Option A: set it up in ChatGPT Work

Use the **ChatGPT desktop app** for this walkthrough. Standalone skill support
differs from plugin distribution and from ordinary file attachments.

1. Open a Work conversation. Attach `skills/tmag-llm-grill-skill/SKILL.md` from your
   extracted repository (or paste its contents).
2. Select `@skill-creator` and send the setup prompt below.
3. Review the generated skill and complete the installation/enable step offered
   by the app. Open **Skills** in the sidebar and confirm `tmag-llm-grill-skill` appears.
4. Start a new Work conversation, type `@`, and select `tmag-llm-grill-skill`. Send the
   interview prompt in the next section. Check that it asks only one question.

```text
@skill-creator Set up a reusable, instruction-only skill named tmag-llm-grill-skill
from the attached SKILL.md. Preserve its one-question-at-a-time interview,
research brief, data and methods, assistant specification, evaluation plan,
glossary, and selective decision-record behavior. Preserve the supplied
instructions and metadata. Help me install and enable it in this app, then
explain how to select it in a new Work conversation.
```

This uses the documented creator workflow rather than assuming that attaching
a ZIP automatically installs a skill. If the creator or Skills controls are
unavailable, check app updates and workspace permissions; use the fallback below.
For web/mobile distribution, OpenAI documents packaging skills in plugins.
See [OpenAI's skill setup guide](https://learn.chatgpt.com/docs/build-skills).

## Option B: install it for Claude Cowork

1. Open Claude and go to **Customize → Skills**.
2. Click **+**, then **Create skill**, then **Upload a skill**.
3. Select `downloads/tmag-llm-grill-skill.zip` and complete the upload.
4. Ensure the skill is enabled. Start a Cowork task and ask it to use
   `tmag-llm-grill-skill`, with the interview prompt below.
5. Confirm it asks a single question and can describe the documents it will maintain.

If upload or creation is missing, your organization's settings or role may
restrict it. Ask the workspace owner about enabling user-created skills. Claude
documents skill use in both chat and Cowork. See
[Anthropic's installation instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Claude Code and plan mode

To use `tmag-llm-grill-skill` in the **Claude Code command line interface
(CLI)**, put the extracted `tmag-llm-grill-skill` folder in your
project's `.claude/skills/` directory (or `~/.claude/skills/` for all projects),
start `claude`, and ask it to use `tmag-llm-grill-skill` with the interview prompt
below. In the Claude app, the skill takes the few extra setup steps above.

**Alternative in the Claude app: use `/plan` mode.** Type `/plan` (or switch
to plan mode), then send the interview prompt below. In plan mode, Claude asks
clarifying questions and proposes a plan before changing anything, so it can
serve as a built-in substitute for this design conversation with no skill to
install. Still ask for **one question at a time**, and ask it to include the
research brief, data and methods, assistant specification, evaluation plan,
glossary, and any warranted decision records in its final plan. To follow the
specific methodology in this skill, supply its instructions using the fallback
below; plan mode alone does not include them.

The spoken experience described here is **ChatGPT Voice**. Installing the skill
in Claude does not install ChatGPT Voice; you can conduct the same interview in
Cowork using text or the input features your Claude app provides.

## Start the interview

Describe your rough idea. Attach an approved data dictionary or a small example
if available; an incomplete idea is enough to start. Try this prompt:

```text
Use tmag-llm-grill-skill to help me design my own research assistant.
I want people to ask questions about my research data and receive answers
grounded in the evidence. I am still figuring out the details.

Ask me ONE question at a time, then wait for my answer. Do not give me a list
of questions. Challenge my assumptions and help me define vague terms.
Keep spoken replies short. Document the research brief, data and methods,
assistant specification, evaluation plan, and glossary as decisions become clear.
Create decision records only when warranted. Distinguish agreed decisions from
proposals, observations, unverified assumptions, and open or deferred questions.
Do not choose technology or begin implementation before we have reviewed the
specification. Start with the next unresolved question about the research use,
using any context I have already provided.
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
Summarize the plan we agreed on. Show me the Research Assistant Brief, Data
and Methods, Assistant Specification, Evaluation Plan, CONTEXT glossary, and
any warranted decision records. Identify unresolved questions, their next
actions, and which ones block implementation. Label suggestions I have not
accepted. Ask me to confirm that the specification reflects our shared
understanding before we begin building.
```

The skill's default outputs are:

| Document | What to review |
|---|---|
| `docs/Research Assistant Brief.md` | Audience, decisions supported, first-version outcomes, questions, scope, exclusions, and constraints |
| `docs/Data and Methods.md` | Sources, units, populations, weights, bases, missingness, duplicates, comparability, permissions, and limitations as relevant |
| `docs/Assistant Specification.md` | Question-to-data/method/evidence/test mapping, answer behavior, outputs, justified technical choices, and blockers |
| `docs/Evaluation Plan.md` | Independent references, test cases, scoring criteria, approved acceptance thresholds, and evaluation ownership |
| `CONTEXT.md` | A glossary of canonical terms and distinctions |
| `docs/adr/NNNN-descriptive-title.md` | A decision record only for a consequential choice with genuine alternatives |

These are files the interview will create for your project, not existing files
in this tutorial. The skill adapts to an existing documentation structure.
Statements should be labeled **Agreed**, **Proposed**, **Observed**, **Unverified**,
or **Open/Deferred** as appropriate. Review field codes, dates, numbers, and any
consequential decision that could have been misheard. If file writing is
unavailable, obtain copyable Markdown in chat; do not assume it has been saved.

A finished specification does not mean the assistant has passed evaluation.
Review the documents before implementation. Scoping allows inspection and
documentation; data uploads, paid batch processing, and deployment require their
own authorization.

The conversation can feel extraordinary, but the useful result is a plan you
understand and can inspect. Use that plan to guide the next stage:
[build and run the first assistant](01-beginner-guide.md).

## If you cannot install skills yet

Open the [skill source](../skills/tmag-llm-grill-skill/SKILL.md), copy the instructions
below its opening metadata, and paste them into a conversation. Ask the assistant
to follow them for this session, then send the interview prompt. This reproduces
the interview instructions for that conversation; it is not a persistent skill
installation. You can still try the one-question-at-a-time method.

Installation guidance was checked against the linked official documentation on
2026-10-19 for ChatGPT skill setup and Claude skill upload. The archive structure
was validated locally; installation in attendees'
ChatGPT Work and Claude Cowork accounts has not been tested.
