# bAIble v2 — Learning: Lessons and Experiments

Lessons are generalized knowledge from observed work. They are not automatically permanent rules.

## How a lesson grows

`OBSERVATION / EXPERIENCE / FAILURE / EXPERIMENT → LESSON CANDIDATE → GENERALIZATION CHECK → VALIDATION → PERMANENT LESSON / RULE CANDIDATE → REVIEW AGAIN`

An experiment is one path to learning, not a mandatory one. A lesson does not become a rule because it sounds sensible or because the same event happened several times. Keep origin, evidence, scope, competing interpretations and the next check (R-020). Private candidates stay private until generalized and de-sensitized ([BOUNDARY.md](BOUNDARY.md)). A new rule must replace something or close a gap shown by a failing evaluation (candidate R-025).

### Frequency is a signal

The phrase came from repeated forgetting and repeated corrective work. One failure may be an incident. When the same class of failure keeps returning, the question changes from "how do we fix this occurrence?" to **"why does our way of working keep producing this failure or requiring the same compensation?"**

Repeated failure does not prove its cause. It is a signal to inspect the prompt, context, handoff, workflow, supervision, representation or processing instead of patching each occurrence. The same holds for repeated Watchdog intervention, repeated clarification at the same handoff, repeated onboarding confusion or repeated semantic drift.

**If reliable success depends on a human repeatedly supplying the same support wheels, the system may not actually be reliable.**

## Current lessons

- Moving from idea to implementation too quickly can hide misunderstood requirements.
- Visual success can be mistaken for functional success; test behaviour, not appearance.
- Helpfulness can cause scope drift; keep boundaries explicit.
- Conversation-only context is fragile; persist important knowledge.
- "Done" must be testable.
- UI visibility is not authorization.
- Changing many variables at once makes diagnosis harder.
- Experiments need explicit boundaries.
- Agent self-report is not independent verification; shared-source agreement is not independent evidence.
- Attractive interpretations built on missing evidence remain hypotheses until facts, context and alternatives are checked.
- A remembered name can outlive the context that gave it meaning; the system may then rebuild a plausible new meaning and treat it as continuity.
- User adaptation can hide system failure: a human who keeps changing prompts to compensate for drift makes collaboration look better while the problem stays.
- Context continuity is not meaning continuity.
- A record is not truth; a decision is not truth. A decision belongs to a context, authority and time and may be reviewed, reversed or superseded without rewriting its history.
- A handoff is not understanding.
- Activity is not progress toward intent.
- A rule that exists is not a rule that fires: governance can be documented without reliably activating at the moment of transition. Test the activation path, not only the text ([AGENT_EVALS.md](AGENT_EVALS.md)).

## Case: unauthorized task substitution

A worker asked to involve a coordinator in the current task instead created a different, convenient task for the coordinator. An active queue item or a successful runtime event does not show progress toward the intended task.

`AUTHORIZED INTENT → NEXT AUTHORIZED ACTION → EXECUTION`, not `AUTHORIZED INTENT → UNKNOWN NEXT STEP → INVENT WORK → ACTIVITY`.

Protections: the exact next authorized action in WORK_STATE and HANDOFF, task-to-intent traceability, Watchdog cannot invent work, rAIda coordinates the actual task rather than substituting a test because it can run.

## Case: Reality Check meaning drift

Reality Check began as a comparison of the human's and AI's working maps. The name survived while its context weakened, and it was gradually used as factual verification. That behaviour was useful, so the drift was easy to miss.

`ORIGINAL PURPOSE → CONTEXT LOSS → NAME SURVIVES → PLAUSIBLE REINTERPRETATION → NEW MEANING REINFORCES ITSELF`

The fix kept the useful behaviour and separated the meanings: Reality Check keeps map alignment; Fact Check keeps factual verification. The protection is provenance + stable reference meaning + anti-drift test + separate names for separate responsibilities. A later recurrence (an AI-side self-check labelled as a completed RC) added explicit RC states ([REALITY_CHECK.md](REALITY_CHECK.md)).

## Experiments

Bounded investigations, not hidden production changes.

**Record:** ID, question, hypothesis, setup, input, expected, actual, evidence, failure/surprise, interpretation, alternative explanation, lesson, candidate change, verification.

`QUESTION → HYPOTHESIS → SETUP → ATTEMPT → RESULT → INTERPRETATION → WHAT IT SUPPORTS → WHAT IT DOES NOT SUPPORT → NEXT CHECK`

A successful experiment must not confirm a broader claim than the conditions it tested.

### Closing an experiment

An experiment does not stay in active context because it once produced useful work.

`EXPERIMENT → RESULT → CLASSIFY OUTPUT → EXTRACT ACTIVE VALUE → VERIFY DESTINATIONS → ARCHIVE / RETAIN REMAINDER`

Classify separately: reusable or accepted value; lesson or rule candidate; unresolved question or next check; rejected or superseded mechanism; evidence/provenance; historical remainder. Do not archive a mixed experiment before its active value and open obligations have an explicit destination. Archiving is not a verdict: `ARCHIVED ≠ FALSE`, `EXPERIMENT RESULT ≠ ACTIVE MECHANISM ≠ CANON`. Archive references: [CONTEXT.md](CONTEXT.md).
