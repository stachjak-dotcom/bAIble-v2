# bAIble v2 — Context Item Contract

A Context Item is a durable, addressable piece of context. It is not automatically true.

## Minimum contract

- `id` — stable identifier.
- `type` — observation, claim, interpretation, decision, evidence, lesson, rule-candidate or task-context.
- `origin` — human, agent, tool, repository, external source or derived, with an addressable reference.
- `scope` — workspace/task/domain where relevant.
- `status` — OBSERVED, CANDIDATE, TESTED, CONFIRMED, REJECTED or UNCERTAIN.
- `visibility` — PUBLIC, PRIVATE or RESTRICTED.
- `observation` — what was directly observed, when applicable.
- `claim` — the proposition being considered.
- `interpretation` — reasoning separated from observation.
- `sources` — provenance references.
- `evidence` — supporting artifacts or checks.
- `relations` — explicit links to other context items.
- `time/version` — temporal validity or source revision when relevant.
- `limitations` — known boundaries.
- `nextCheck` — the next required verification, if any.

## Relation semantics

`supports`, `contradicts`, `refines`, `supersedes`, `derivedFrom`, `dependsOn`, `testedBy`, `verifiedBy`, `originatedFrom`, `appliesTo`.

## Epistemic rule

Lifecycle status is not proof. `CONFIRMED` must still have evidence appropriate to the claim. A relationship is also not proof merely because it exists.

## Scope rule

Do not expand a Context Item's scope merely because another item is related to it. Relations explain connection; they do not silently transfer authority, visibility or truth.