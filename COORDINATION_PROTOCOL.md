# bAIble v2 — Coordination Protocol

This protocol defines how Human, AI/Agent, rAIda, Watchdog, Reality Check, Fact Check, verification and durable repositories cooperate.

## Phase 1 — Orient
Human intent is identified. AI establishes role, scope, authority, source boundaries and expected evidence.

## Phase 2 — Recover context
Load only context relevant to the task. Mark missing, stale, conflicting and private material explicitly.

## Phase 3 — Align meaning
Use Reality Check when there is a risk that Human and AI are solving different problems.

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
Plan the smallest sufficient, reversible sequence. Identify gates, evidence and stop conditions.

## Phase 6 — Approve where required
Human approval is required for defined material decisions, scope expansion, destructive action, sensitive public/private transitions and other explicit intervention gates.

## Phase 7 — Execute
Agent performs bounded work. rAIda coordinates task state and checks. Watchdog monitors observable continuity.

## Phase 8 — Record evidence
Record what actually happened, where, by whom/what, with which source/commit/run/test and what remains unverified.

## Phase 9 — Verify
Verification checks whether the expected result actually holds.

## Phase 10 — Accept / correct
Verification does not automatically equal human acceptance. Failed verification returns to correction and re-verification.

## Phase 11 — Learn
Observed recurrence or surprise becomes a candidate lesson, not an automatic permanent rule.

## Phase 12 — Persist
Persist only what is useful for future recovery, governance, evidence or learning. Preserve provenance.

## Coordination invariant

No layer silently acquires another layer's authority.

## Continuation invariant

`DONE → next task` is allowed only when the next task is explicit and authorized.

## Epistemic invariant

A lifecycle status must not be used as substitute for verification.
