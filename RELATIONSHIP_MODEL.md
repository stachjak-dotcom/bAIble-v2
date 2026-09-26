# bAIble v2 — Relationship Model

UnAiversed-style context is useful only when the relation itself is explicit, scoped and inspectable.

## Node classes

Canonical node classes include:

- observation
- claim
- interpretation
- decision
- evidence
- verification
- lesson
- rule-candidate
- rule
- task-context
- role
- mechanism
- system
- risk
- question
- experiment
- source
- milestone

## Relation classes

### Structural
`contains`, `belongsTo`, `represents`, `linksContextTo`

### Operational
`coordinates`, `invokes`, `handsOffTo`, `monitors`, `escalatesTo`, `authorizes`, `blocks`, `requiresHumanDecision`

### Epistemic
`supports`, `contradicts`, `refines`, `supersedes`, `derivedFrom`, `testedBy`, `verifiedBy`, `originatedFrom`, `appliesTo`

### Governance / learning
`constrains`, `protects`, `teaches`, `learnsFrom`, `remembersToCheck`, `exposesRiskTo`

## Relation metadata

A material relation may carry:

- origin,
- scope,
- time/version,
- visibility,
- evidence,
- status,
- limitation,
- next check.

A relation does not transfer truth, authority, visibility or scope by association.

## Contradiction contract

When a check finds a contradiction, report:

- contradiction ID,
- claim A + source A,
- claim B + source B,
- contradiction type,
- affected scope,
- what is unresolved,
- evidence currently available,
- what check or decision would resolve it,
- whether action is blocked.

A generic yellow/warning result without the underlying contradiction is insufficient for material work.
