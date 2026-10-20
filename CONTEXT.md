# bAIble v2 — Context, Relations and Provenance

How durable context is kept, addressed, related and traced, so that UnAiversed-style maps stay inspectable and never become a truth store.

REMEMBER-TO-CHECK, NOT REMEMBER-EVERYTHING.

## Context is not truth

Durable memory exists to keep enough context, provenance and recovery points to continue disciplined work. It does not replace checking relevance, evidence or current meaning.

Old context may be correct but irrelevant, stale, incomplete, superseded, contradictory, private or out of scope. A stored record is not automatically true; a relationship is not proof; a remembered term is not proof that its original meaning survived.

Forbidden for material decisions: `OLD MEMORY → NEW ASSUMPTION → ACTION`. Prefer `CONTEXT → CHECK RELEVANCE → GROUND → DECIDE → ACT`.

**Keep the chain of trust visible.** `USER_INPUT → RECORD → INTERPRETATION → CONFIRMATION / EVIDENCE → DECISION → LESSON / PATTERN`. What the human actually said must never be silently rewritten as the AI's interpretation, and an interpretation must never later be presented as the human's own words. Grammatically understood is not understood in meaning, and understood in meaning is not understood in intent. The higher the impact of an interpretation, the stronger the confirmation it needs (candidate R-027).

**Context continuity is not meaning continuity.** Keeping the same files, identifiers, terms or task history does not guarantee the same interpretation later. When meaning matters, keep or recover: what was actually received or observed, what was inferred, what the term or decision meant in its original context, what changed, what remains uncertain, what needs checking now.

**Missing context** is never completed from plausibility: `MISSING_CONTEXT → RECOVER / ASK / CHECK → CONTINUE`. Unknown, missing, stale or conflicting context stays visible until resolved or deliberately bounded.

**Durable history** is not rewritten to fit a newer interpretation. Add a new observation, interpretation, decision or relation that refines, contradicts or supersedes the earlier one, with provenance.

## Context Item

A durable, addressable piece of context. It is not automatically true. Allowed values: [vocabulary.json](vocabulary.json) (`context_item`).

| Field | Content |
|---|---|
| `id` | stable identifier |
| `type` | observation, claim, interpretation, decision, evidence, lesson, rule-candidate or task-context |
| `origin` | human, agent, tool, repository, external source or derived, with an addressable reference |
| `scope` | workspace, task or domain |
| `status` | OBSERVED, CANDIDATE, TESTED, CONFIRMED, REJECTED or UNCERTAIN |
| `visibility` | PUBLIC, PRIVATE or RESTRICTED |
| `observation` | what was directly observed |
| `claim` | the proposition being considered |
| `interpretation` | reasoning kept apart from observation |
| `sources` | provenance references |
| `evidence` | supporting artifacts or checks |
| `relations` | explicit links to other items |
| `time/version` | temporal validity or source revision |
| `limitations` | known boundaries |
| `nextCheck` | the next required verification |

Lifecycle status is not proof: `CONFIRMED` still needs evidence appropriate to the claim. Do not widen an item's scope because another item is related to it.

## Relations

A relation is useful only when it is explicit, scoped and inspectable. Node classes and predicates are listed once in [vocabulary.json](vocabulary.json):

- **participation** — participatesIn, createsWith
- **structural** — contains, belongsTo, represents, linksContextTo, preserves
- **operational** — coordinates, invokes, observes, handsOffTo, monitors, escalatesTo, authorizes, blocks, requiresHumanDecision, comparesMapsOf, surfacesRelevant
- **epistemic** — supports, contradicts, refines, supersedes, derivedFrom, originatedFrom, appliesTo, dependsOn, testedBy, verifiedBy, verifies, producesEvidenceFor
- **governance / learning** — constrains, protects, teaches, learnsFrom, remembersToCheck, exposesRiskTo

A material relation may carry origin, scope, time/version, visibility, evidence, status, confidence where useful, limitation and next check. A relation does not transfer truth, authority, visibility or scope by association (R-023).

## Contradictions

When a check finds a material contradiction, record:

- contradiction ID;
- claim A + source A, claim B + source B;
- contradiction type and affected scope;
- what is unresolved and the evidence currently available;
- what check or decision would resolve it;
- whether action is blocked.

A generic yellow or warning result without the underlying contradiction is not enough for material work (R-021; failure mode Yellow Without Explanation).

## Provenance

Every important claim, decision, lesson and relation keeps enough origin information to see where it came from and how it changed. Provenance supports verification; it does not prove truth.

**Source classes:** PUBLIC-SOURCE, PROJECT-SOURCE, EXPERIMENT, GENERALIZED-LESSON, HUMAN-INPUT, AGENT-INTERPRETATION, TOOL-OBSERVATION, DERIVED, PRIVATE.

**Minimal record:** claim or item, type, status, source class, addressable source reference, evidence, scope, time/version, limitations, last verified, next check.

Never cite a private source as public. Never imply access to a source the current worker cannot access. Keep refinement, contradiction and supersession instead of rewriting history.

### Moving and archiving

When important material is moved, superseded, extracted from a mixed experiment or archived, keep enough to reconstruct the move: source location and revision, classification, active value extracted and where it went, unresolved items preserved elsewhere, what happened to the remainder, the archive reference, and a check that the destination exists and matches the claim.

**Archive references** use a link pinned to a commit (for example a GitHub permalink `…/blob/<commit-sha>/<path>`), so the reference survives later changes in the archive. No new repository, manifest format or lifecycle field is needed for every object.

`PRESERVED HISTORY ≠ ACTIVE CONTEXT` · `ARCHIVED ≠ ACTIVE ≠ FALSE`
