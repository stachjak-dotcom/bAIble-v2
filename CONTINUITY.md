# bAIble v2 — Work Continuity and Handoff

Conversation continuity is not reliable work continuity. Three artifacts keep work recoverable, each with its own job.

## WORK_STATE

A short, replaceable snapshot of the current operational state.

Fields: objective, current task, why it matters, role, scope / out of scope, authority / human gates, authorized sources, last verified state, work completed, current evidence, decisions, unknowns, contradictions, current plan, exact next authorized action, do-not-do, timestamp / source revision.

Update it when a material decision is made, a significant step completes, evidence changes, the plan changes, a contradiction or blocker appears, approval changes or scope changes materially.

WORK_STATE is a recovery aid, not truth; its claims still need evidence. It does not have to keep full reasoning or every loaded contract: when complexity resolves, keep only what safe continuation needs (last verified state, material evidence and provenance, open contradictions or blockers, authority and gates, the exact next authorized action). Do not create WORK_STATE for a task that needs no durable continuity.

## WORK_LOG

An append-only record of significant state changes: authorized transitions, completed material steps, verification results, human approvals, contradictions found or resolved, scope changes, blockers, rollbacks and recoveries. Not every click or token: the purpose is reconstruction, not surveillance.

## HANDOFF

A durable transfer between sessions, humans, agents, tools or environments. It references WORK_STATE, the relevant WORK_LOG entries and the actual evidence.

**Role and authority:** from role, to role, authority boundary, approval still required.

**Contract:** task ID, intent, current state, scope / out of scope, dependencies, authorized sources, verified sources, applicable rules, known facts / observations, interpretations / assumptions, unknowns / missing context, conflicts, work completed, actual evidence, verification result, expected output, expected evidence, open questions, risks / limitations, next authorized transition, recovery / rollback notes where relevant.

**Rules:**

1. Preserve scope and authority.
2. Preserve uncertainty, missing context and contradictions.
3. Distinguish completed work from proposed next work.
4. Link claims to evidence where practical.
5. Never imply access, action, test, verification or certainty that did not occur.
6. Do not convert a lifecycle state into an epistemic claim.
7. The receiving worker should not need hidden conversation to continue a bounded task.

A handoff is not a conversational "good luck". It is a claim about prior work, not proof of it.

## Recovery

`HANDOFF → RECONSTRUCT → CHECK → CONTINUE`, never `HANDOFF → BELIEVE → CONTINUE`.

A receiving worker may feel oriented after a coherent handoff while inheriting a wrong, stale or incomplete interpretation (failure mode False Continuity). Before material continuation:

1. reconstruct the claimed current state;
2. check critical facts against actual sources and evidence;
3. surface contradictions and missing context;
4. continue only through an authorized transition.
