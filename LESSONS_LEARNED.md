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

OBSERVATION → LESSON CANDIDATE → GENERALIZATION CHECK → VALIDATION → PERMANENT LESSON / RULE CANDIDATE.

A lesson does not become a rule merely because it sounds sensible.