# bAIble v2 — Work Continuity

Conversation continuity is not reliable work continuity.

The continuity model separates three artifacts with different jobs:

## WORK_STATE

A short, replaceable snapshot of the current operational state.

Recommended fields:
- objective
- current task
- why it matters
- role
- scope / out of scope
- authority / human gates
- authorized sources
- last verified state
- work completed
- current evidence
- decisions
- unknowns
- contradictions
- current plan
- exact next authorized action
- do-not-do
- timestamp / source revision

Update WORK_STATE when a material decision is made, a significant step completes, evidence changes, the plan changes, a contradiction/blocker appears, approval changes, or scope materially changes.

WORK_STATE is not truth. It is a recovery aid whose claims still require appropriate evidence.

## WORK_LOG

An append-only record of significant state changes.

Record meaningful events:
- authorized transition,
- completed material step,
- verification result,
- human approval,
- contradiction discovered/resolved,
- scope change,
- blocker,
- rollback or recovery.

Do not log every click or token. The purpose is reconstructability, not exhaustive surveillance.

## HANDOFF

A handoff is a snapshot used when work moves between sessions, humans, agents, tools or environments.

It references WORK_STATE, relevant WORK_LOG entries and actual evidence. It must preserve uncertainty, scope, authority and the next authorized transition.

A handoff must be treated as a claim about prior work, not as proof of that work.

## Recovery loop

`HANDOFF → RECONSTRUCT → CHECK → CONTINUE`

Forbidden shortcut:

`HANDOFF → BELIEVE → CONTINUE`

## False Continuity protection

A receiving worker may feel oriented after reading a coherent handoff while still inheriting an incorrect, stale or incomplete interpretation.

Before material continuation:
1. reconstruct the claimed current state;
2. check critical facts against actual sources/evidence;
3. surface contradictions and missing context;
4. continue only through an authorized transition.

See HANDOFF.md, CONTEXT_AND_MEMORY.md, VERIFICATION.md and FAILURE_MODES.md.
