# bAIble v0.1 → v2 — Migration and Fact Check

Status: WORKING AUDIT

This audit checks migration claims against the actual current v2 repository and relevant private implementation evidence before generalizing it into the public bAIble.

## Corrected contradictions

### C-001 — Original role restoration
**Historical problem:** the migration audit claimed v0.1 roles were restored, while the active role file at that time exposed only newer system/coordination roles.

**Current state:** CORRECTED. `AGENT_ROLES.md` now explicitly preserves Human / Product Owner, Architect, Developer, QA, Reviewer and Documentation Agent, while keeping coordination/check mechanisms separate.

### C-002 — lAInguage restoration
**Historical problem:** Explore / Propose / Prepare / Implement / Verify / Review existed in preserved material but was not initially exposed as a canonical active-v2 language document.

**Current state:** CORRECTED. `LANGUAGE.md` is canonical.

### C-003 — Reality Check meaning drift
**Historical problem:** Reality Check had gradually been used as a broad factual/evidential verification mechanism even though its original purpose was comparison of the human and AI working maps.

**Current state:** CORRECTED IN ACTIVE V2.

- **Reality Check (RC)** = alignment / interpretation / context divergence.
- **Fact Check (FC)** = factual and evidential verification.
- `REALITY_CHECK.md` preserves the original reference meaning and anti-drift test.
- `FACT_CHECK.md` preserves the useful verification behavior that had accumulated under the RC name.

This correction itself is retained as a concrete forgetting/context-drift case in `LESSONS_LEARNED.md`.

### C-004 — Runtime still carries the older RC contract
**Observed implementation lag:** the private FederAItion runtime still contains a `realityCheck()` contract that combines semantic/perspective alignment with evidence presence, and Watchdog can report missing evidence as a Reality Check concern.

**Current state:** GOVERNANCE CORRECTED; IMPLEMENTATION ALIGNMENT STILL REQUIRED.

This is not corrected by renaming documentation alone. Runtime behavior and tests must eventually be reviewed against the RC/FC split without weakening their existing evidence and human-gate protections.

## Verified observations from the FederAItion / UnAiversed hunt

- Runtime distinguishes intent, attempted execution, tool result, observation and verification, and blocks claim inflation between these states.
- DONE requires a verified epistemic state in the inspected runtime tests.
- Missing context and differing participant interpretations are explicitly detectable.
- Durable decisions are recorded with context and review conditions rather than treated as timeless truth.
- Lesson candidates preserve evidence, limits and a review-required promotion step.
- Repeated failure was the practical origin of the “frequency is a signal” lesson: recurrence should trigger inspection of the surrounding process rather than endless incident-by-incident compensation.
- Context continuity and meaning continuity are distinct; preserving records does not guarantee preservation of interpretation.
- Historical meaning should be refined, contradicted or superseded with provenance rather than silently rewritten.

## Redundancy candidates

`START_HERE.md`, `AGENT_QUICK_START.md`, `ONBOARDING_FLOW.md`, `NEW_USER_AGENT.md`, `BOOTSTRAP.md`, `REPOSITORY_BOOTSTRAP.md` and `WHEEAILS.md` overlap substantially. Their distinct information should be extracted into canonical onboarding, language, bootstrap, role and template documents rather than copied wholesale.

Private FederAItion currently also contains two substantially overlapping feature-completeness lesson candidates. Treat this as a consolidation signal, not as permission to delete historical evidence.

## Principles

A migration document saying something was “fixed” is not proof that the current repository contains the fix. Repository state is the evidence to check.

A surviving term is also not proof that its original meaning survived.

A record, relationship or repeated occurrence is not automatically truth or verification.

## Next checks

1. compare active v2 navigation with the preserved foundation;
2. identify dead and duplicate routes;
3. perform public/private review;
4. align FederAItion runtime semantics with the restored RC / FC split;
5. run contradiction and meaning-drift scan again after consolidation.