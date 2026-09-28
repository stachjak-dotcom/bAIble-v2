# bAIble v2 — Failure Modes / “Požírači hvězd”

Failure modes live next to the objects they can distort. They are not a detached risk appendix.

## Context Drift
Relevant context is lost, reweighted or replaced, shifting current interpretation.

Protection: provenance, Context Items, explicit unknowns, Reality Check, recovery before action.

## Meaning Drift
A name survives while its original purpose is silently replaced.

Protection: stable reference meaning, provenance, anti-drift tests, explicit refine/supersede links.

## Scope Drift
Work expands beyond authorized intent or boundaries.

Protection: preflight, explicit scope, handoff contracts, human gates, OUT_OF_SCOPE state.

## False Done
A plausible report, partial implementation or passing local test is treated as complete success.

Protection: observable completion criteria, evidence, independent verification where appropriate, explicit acceptance.

## False Continuity
A coherent handoff, persistent chat, familiar identifier or recovered state creates the feeling that the new worker understands the previous work when it has only inherited a record of someone else's interpretation.

Protection: `HANDOFF → RECONSTRUCT → CHECK → CONTINUE`; verify critical state against actual sources; preserve contradictions and missing context.

## Activity Substitution
The system performs visible work that is not the next authorized step toward the human's intent — for example, inventing a convenient task because the required next transition is unknown.

Protection: exact next authorized action, task-to-intent traceability, scope check, STOP/RECOVER/ESCALATE when the next step is not authorized.

Activity ≠ progress toward intent.

## Record ≠ Truth
Stored context, linked nodes or repeated notes are mistaken for factual truth.

Protection: separate record from claim/evidence/verification.

## Decision ≠ Truth
A past decision is treated as timeless fact.

Protection: preserve authority, context, time, assumptions, review/reversal conditions.

## Agent Echo Chamber
Several agents appear to agree because they share the same source or assumption.

Protection: trace provenance and independence of evidence.

## White-Couch Failure
A coherent and attractive interpretation is built on missing evidence.

Protection: explicitly classify hypothesis, missing context and alternative explanation.

## Automation Without Authority
rAIda, Watchdog or another automated layer continues or changes material state without authorization.

Protection: explicit transition contracts, human gates, scoped executors, audit trail.

## User Adaptation Hides Failure
A human learns to compensate for recurring AI failure so the system appears reliable.

Protection: treat recurrence as a signal to inspect the process.

## Capability Discovery Failure
A useful mechanism exists in the public ecosystem, but the current worker cannot find or load its canonical contract and therefore treats the capability as absent, guesses its meaning, or pushes repeated navigation work onto the human.

Protection: classify actual access capability; preserve DISCOVERABLE / LOADED / ACTIVE / AUTHORIZED distinctions; expose semantic resource routing and bounded fallback adapters; never infer absence from retrieval failure.

`CAPABILITY EXISTS ≠ CURRENT WORKER CAN DISCOVER / LOAD IT`

## Memory Inflation
More stored context increases noise, stale assumptions and retrieval ambiguity.

Protection: REMEMBER-TO-CHECK, NOT REMEMBER-EVERYTHING; relevance selection; bounded context activation.

## Semantic Smearing
Observation, interpretation, decision and evidence are merged into one note.

Protection: typed Context Items and explicit relations.

## Yellow Without Explanation
A check reports warning/uncertainty but does not expose the actual contradiction or missing check.

Protection: every material conflict should identify the conflicting claims/sources, conflict type, unresolved point and what would resolve it.
