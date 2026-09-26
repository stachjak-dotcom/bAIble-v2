# bAIble v0.1 → v2 — Migration and Fact Check

Status: WORKING AUDIT

This audit checks migration claims against the actual current v2 repository.

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

## Verified observations

- v0.1 foundation is preserved as a bridge rather than copied wholesale.
- Public/private separation is explicitly treated as a v2 evolution.
- rAIda, Watchdog and contextual-layer concepts are later extensions, not original v0.1 foundation.
- The quotations in `SONG_TWO.md` are documented as historical v0.1 material.
- `WHEEAILS.md` contains the original six-word action vocabulary.

## Redundancy candidates

`START_HERE.md`, `AGENT_QUICK_START.md`, `ONBOARDING_FLOW.md`, `NEW_USER_AGENT.md`, `BOOTSTRAP.md`, `REPOSITORY_BOOTSTRAP.md` and `WHEEAILS.md` overlap substantially. Their distinct information should be extracted into canonical onboarding, language, bootstrap, role and template documents rather than copied wholesale.

## Principles

A migration document saying something was “fixed” is not proof that the current repository contains the fix. Repository state is the evidence to check.

A surviving term is also not proof that its original meaning survived.

## Next checks

1. compare active v2 navigation with the preserved foundation;
2. identify dead and duplicate routes;
3. perform public/private review;
4. inspect FederAItion and UnAiversed for concepts absent from v2;
5. run contradiction and meaning-drift scan again after consolidation.
