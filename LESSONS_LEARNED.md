# bAIble v2 — Lessons

Lessons are generalized knowledge extracted from observed work. They are not automatically permanent rules.

## Current lessons

- Moving from idea to implementation too quickly can hide misunderstood requirements.
- Visual success can be mistaken for functional success; test behavior, not appearance alone.
- Helpfulness can cause scope drift; keep boundaries explicit.
- Conversation-only context is fragile; persist important knowledge.
- “Done” must be testable.
- UI visibility is not authorization.
- Changing many variables at once makes diagnosis harder.
- Experiments need explicit boundaries.
- Agent self-report is not independent verification.
- Shared-source agent agreement is not independent evidence.
- Attractive interpretations built on missing evidence remain hypotheses until relevant facts, context and alternatives are checked.
- A remembered **name** can survive after the context that gave it meaning has been lost. The system may then reconstruct a plausible new meaning from the current context and treat that reconstruction as continuity.
- User adaptation can hide system failure: if a human repeatedly changes how they prompt in order to compensate for AI drift, apparent collaboration may improve while the underlying continuity problem remains.
- Context continuity is not meaning continuity. The same files, terms, task and history can remain available while their interpretation silently changes.
- A record is not truth. Stored, linked, repeated or named information still requires the evidence, scope and interpretation appropriate to the claim being made.
- A decision is not truth. A decision belongs to a context, authority and time; it may later be reviewed, reversed, refined or superseded without rewriting its history.

## Frequency is a signal

The original practical meaning of **frequency is a signal** came from repeated forgetting and repeated corrective work.

One failure may be an incident. When the same class of failure keeps returning, the useful question changes from:

> “How do we fix this occurrence?”

to:

> **“Why does our way of working keep producing this failure or requiring the same compensation?”**

Repeated failure does not prove its cause. It is a signal to inspect the design of the prompt, context, handoff, workflow, supervision, representation or processing rather than endlessly patching each occurrence.

A related warning is repeated human compensation:

> **If reliable success depends on a human repeatedly supplying the same support wheels, the system may not actually be reliable.**

The same idea applies beyond forgetting. Repeated Watchdog intervention, repeated clarification at the same handoff, repeated onboarding confusion or repeated semantic drift can all signal that the surrounding process deserves redesign.

Frequency therefore means **attention and investigation**, not automatic promotion to a rule.

## Case study — Reality Check meaning drift

Reality Check originally existed to compare the human's and AI's current working / mental maps so divergence in understanding could be exposed.

Over time, the name survived while the surrounding context weakened. The mechanism was gradually reinterpreted as factual/evidential verification. That new behavior was useful, so the drift was easy to miss: the mechanism still appeared coherent and productive.

The failure pattern was:

`ORIGINAL PURPOSE → CONTEXT LOSS → NAME SURVIVES → PLAUSIBLE REINTERPRETATION → NEW MEANING REINFORCES ITSELF`

The correction was not to discard the useful later behavior. It was to separate the meanings:

- **Reality Check (RC)** keeps the original map-alignment purpose.
- **Fact Check (FC)** keeps the factual/evidential verification behavior.

The protection is therefore not just a definition. It is **provenance + stable reference meaning + anti-drift test + separate names for separate responsibilities**.

This case is a concrete example of forgetting, context drift and meaning drift occurring even while terminology appears stable.

## Promotion rule

Useful learning may originate from an observation, experience, failure, research result or experiment.

`OBSERVATION / EXPERIENCE / FAILURE / EXPERIMENT → LESSON CANDIDATE → GENERALIZATION CHECK → VALIDATION → PERMANENT LESSON / RULE CANDIDATE`

An experiment is one path to learning, not a mandatory path for every lesson.

A lesson does not become a rule merely because it sounds sensible or because the same event occurred repeatedly. Preserve origin, evidence, scope, competing interpretations and the next check.