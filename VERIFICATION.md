# bAIble v2 — Verification

Verification asks: does the required result actually hold?

Record the requirement, expected result, actual evidence, method, scope, source/commit/run, result and unresolved concerns.

## Ladders

Three ladders, each for a different question. Canonical definitions: [vocabulary.json](vocabulary.json). Never skip or collapse adjacent steps.

| Question | Ladder |
|---|---|
| How strong is this evidence? | statement → observation → artifact → test → independent verification → acceptance |
| Does a capability really exist for us? (a tool, service, integration) | DOCUMENTED → AVAILABLE → DISPATCHED → OBSERVED → VERIFIED → ACCEPTED |
| How far is something we build? | DESIGNED → BUILT → TESTED → VERIFIED → INTEGRATED → ACCEPTED |

For a capability, DOCUMENTED means an authoritative source says it exists; AVAILABLE means it is exposed to this account, environment or repository; DISPATCHED means the requested action actually started; OBSERVED means output was actually produced. Before building on a capability, name the exact claim, its current step, the evidence for it, the smallest test that would move it up, what a pass would and would not prove, and the stop condition.

## Distinctions

Unit test ≠ production end-to-end. Simulation ≠ live execution. Agent report ≠ independent verification. Documentation ≠ implementation. Implementation ≠ verification. Verification ≠ human acceptance.

A runtime test proves only the behaviour it exercised. A successful run does not prove editorial completeness, and a local coordination trace does not prove that external execution, verification or acceptance occurred.
