# bAIble v2 — Provenance

Every important claim, decision, lesson and relationship should retain enough origin information to inspect where it came from and how it changed.

## Source classes

- PUBLIC-SOURCE
- PROJECT-SOURCE
- EXPERIMENT
- GENERALIZED-LESSON
- HUMAN-INPUT
- AGENT-INTERPRETATION
- TOOL-OBSERVATION
- DERIVED
- PRIVATE

## Minimal record

- Claim / item
- Type
- Status
- Source class
- Source / addressable reference
- Evidence
- Scope
- Time/version
- Limitations
- Last verified
- Next check

Never cite a private source as public. Never imply access to a source that the current worker cannot access.

Preserve refinement, contradiction and supersession rather than rewriting history to fit a newer interpretation.

Provenance supports verification but does not itself prove truth.


## Disposition and archival provenance

When important material is moved, superseded, extracted from a mixed experiment, or archived, preserve enough disposition provenance to reconstruct the transition.

A minimal disposition record should identify, as applicable:
- source location and revision;
- classification of the source material;
- active value extracted;
- destination of extracted value;
- unresolved items or next checks preserved elsewhere;
- remainder disposition;
- archive/historical reference;
- verification that the intended destination/archive exists and matches the transition claim.

This does not require a new repository, manifest format or lifecycle field for every object. Reuse existing provenance, relations and durable records where they are sufficient.

`PRESERVED HISTORY ≠ ACTIVE CONTEXT`

`MOVED / ARCHIVED ≠ VERIFIED FALSE`
