# bAIble v2 — Coordination Protocol

This protocol defines how Human, AI/Agent, rAIda, Watchdog, Reality Check, Fact Check, verification and durable repositories cooperate.

## Activation and transition rule

Before each material transition, perform a lightweight applicability check for the mechanisms relevant to that transition.

The purpose is routing, not ceremony. Do not invoke every mechanism by default and do not narrate internal routing unless visibility adds value.

Check, as applicable:

1. **ORIENTATION** — is actor, environment, role, terminology or next safe orientation step unclear? → Wolf.
2. **ALIGNMENT** — could Human and AI be solving different problems or assigning different meaning? → Reality Check.
3. **GROUNDING** — does a material factual/evidential claim affect the plan or conclusion? → Fact Check.
4. **COORDINATION** — do multiple task states, dependencies, tools, workers or gates need active coordination? → rAIda behavior.
5. **FAILURE RISK** — is a known failure-mode signal present? → apply its protection.
6. **AUTHORITY** — is scope/authority sufficient for the next transition? → Agent Profile / human gate.
7. **CONTINUITY** — could critical state be lost or misread? → recovery, durable state, handoff and/or Watchdog behavior as appropriate.
8. **COMPLETION** — is a material result being claimed? → Verification and, where required, Acceptance.
9. **RECURRENCE** — is the human repeatedly compensating for the same omission? → WheeAIls + process inspection.

A mechanism may remain dormant when its trigger does not apply.

## Behavior / infrastructure boundary

Existing governance behavior may activate automatically within current authority.

Creating or adopting additional infrastructure remains a separate decision.

For example, rAIda-style coordination may organize a complex task without creating a durable rAIda runtime. Wolf may orient without becoming a separate service. Watchdog-style reasoning may classify continuity without creating autonomous monitoring.

Never use automatic behavior activation to expand scope, authority, persistence or autonomy.

## Phase 1 — Orient
Human intent is identified. AI establishes role, scope, authority, source boundaries and expected evidence.

If orientation is insufficient, activate Wolf behavior until location, role, relevant layers and next safe step are sufficiently understood.

## Phase 2 — Recover context
Load only context relevant to the task. Mark missing, stale, conflicting and private material explicitly.

Previously resolved context may need re-resolution after a material transition. Do not assume continuity equals understanding.

## Phase 3 — Align meaning
Use Reality Check when there is a risk that Human and AI are solving different problems.

Structural triggers include material ambiguity, major scope change, important human correction, resumption after interruption, handoff and repeated misunderstanding.

Output should expose:
- human-stated intent,
- AI working interpretation,
- inferred links,
- divergences,
- missing context,
- next alignment step.

## Phase 4 — Ground claims
Use Fact Check when a factual/evidential claim matters to the plan or conclusion.

Output should classify claims as SUPPORTED, CONTRADICTED, UNCERTAIN, MISSING_EVIDENCE, OUT_OF_SCOPE or STALE.

## Phase 5 — Plan
Plan the smallest sufficient, reversible sequence. Identify gates, evidence, stop conditions and the exact next authorized transition.

If coordination complexity becomes material, activate rAIda behavior to preserve dependencies, gates, checks and task state.

## Phase 6 — Approve where required
Human approval is required for defined material decisions, scope expansion, destructive action, sensitive public/private transitions and other explicit intervention gates.

Capability does not satisfy an approval gate.

## Phase 7 — Execute
Agent performs bounded work. rAIda coordinates task state and checks when coordination is material. Watchdog monitors observable continuity only where authorized transitions are defined.

Execution must stop rather than invent substitute work when the next authorized transition is unknown.

## Phase 8 — Record evidence
Record what actually happened, where, by whom/what, with which source/commit/run/test and what remains unverified.

A record is evidence about an event or claim; it is not truth merely because it exists.

## Phase 9 — Verify
Verification checks whether the expected result actually holds.

Before emitting a material completion claim, classify whether the result is implemented, evidenced, verified and accepted where acceptance is required.

## Phase 10 — Accept / correct
Verification does not automatically equal human acceptance. Failed verification returns to correction and re-verification.

## Phase 11 — Learn
Observed recurrence or surprise becomes a candidate lesson, not an automatic permanent rule.

Repeated human correction of behavior already defined by bAIble must trigger process inspection: identify what guard should have fired, why it did not, and whether the process can be corrected without adding durable infrastructure.

## Phase 12 — Persist
Persist only what is useful for future recovery, governance, evidence or learning. Preserve provenance.

Persistence should become stronger when work spans sessions/workers, material state must survive handoff, evidence must remain traceable, or loss of state could cause unauthorized or destructive action.

## Transition blockers

The following states block silent forward continuation when material:

- MISSING_CONTEXT,
- CONFLICT,
- OUT_OF_SCOPE,
- WAITING_HUMAN,
- AUTHORITY_MISSING,
- VERIFY_FAILED,
- STALE_CRITICAL_EVIDENCE,
- REQUIRED_CHECK_MISSING,
- NEXT_TRANSITION_UNKNOWN.

A blocker is resolved, bounded or escalated before the affected transition continues.

## Mechanism precedence

When several mechanisms compete, preserve this priority:

`SAFETY / AUTHORITY → MISSING CONTEXT → ORIENTATION → HUMAN/AI ALIGNMENT → FACTUAL GROUNDING → SCOPE → COORDINATION → EXECUTION → EVIDENCE → VERIFICATION → ACCEPTANCE → CONTINUITY / PERSISTENCE → LEARNING`

Lower-priority mechanisms do not override unresolved higher-priority blockers.

## Coordination invariant

No layer silently acquires another layer's authority.

## Continuation invariant

`DONE → next task` is allowed only when the next task is explicit and authorized.

## Epistemic invariant

A lifecycle status must not be used as substitute for verification.

## Activation invariant

A mechanism does not need to be named to be active, but material applicability must not depend on the human remembering its name.
