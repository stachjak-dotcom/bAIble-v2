# bAIble v0.1 → v2 — Migration and Fact Check

Status: WORKING AUDIT

This audit checks migration claims against the actual current v2 repository.

## Explicit contradictions

### C-001 — Role restoration is incomplete
**Claim:** the migration audit says v0.1 roles were restored explicitly in `AGENT_ROLES.md`.

**Current evidence:** the active v2 file defines Human, bAIble, rAIda, Agent, Reality Check, Fact Check, Watchdog, UnAiversed, WheeAIls and Wolf, but does not separately define the original v0.1 roles Human / Product Owner, Architect, Developer, QA, Reviewer and Documentation Agent.

**Classification:** CONTRADICTED / INCOMPLETE.

**Resolution:** restore the original roles explicitly while keeping newer coordination/check mechanisms separate.

### C-002 — lAInguage restoration is incomplete in the active path
**Claim:** Explore / Propose / Prepare / Implement / Verify / Review is restored in v2.

**Current evidence:** it exists in preserved foundation/pre-v2 material, but the active v2 path had no dedicated canonical language document.

**Classification:** PARTIALLY VERIFIED / INCOMPLETE.

**Resolution:** `LANGUAGE.md` now makes it canonical.

### C-003 — Reality Check meaning drift
**Claim:** Reality Check was being used as a general verification mechanism.

**Current evidence:** provenance review restored its original purpose as comparison of the human and AI working maps. Factual/evidential verification that had accumulated under the same name has been split into `FACT_CHECK.md`.

**Classification:** MEANING DRIFT IDENTIFIED / CORRECTED IN ACTIVE V2.

**Resolution:** RC = alignment / interpretation / context divergence. FC = factual and evidential verification. Historical wording is not treated as proof of the original meaning.

## Verified observations

- v0.1 foundation is preserved as a bridge rather than copied wholesale.
- Public/private separation is explicitly treated as a v2 evolution.
- rAIda, Watchdog and contextual-layer concepts are later extensions, not original v0.1 foundation.
- The quotations in `SONG_TWO.md` are documented as historical v0.1 material.
- `WHEEAILS.md` contains the original six-word action vocabulary.

## Redundancy candidates

`START_HERE.md`, `AGENT_QUICK_START.md`, `ONBOARDING_FLOW.md`, `NEW_USER_AGENT.md`, `BOOTSTRAP.md`, `REPOSITORY_BOOTSTRAP.md` and `WHEEAILS.md` overlap substantially. Their distinct information should be extracted into canonical onboarding, language, bootstrap, role and template documents rather than copied wholesale.

## Principle

A migration document saying something was “fixed” is not proof that the current repository contains the fix. Repository state is the evidence to check.

A surviving term is also not proof that its original meaning survived.

## Next checks

1. verify original role definitions against v0.1;
2. compare active v2 navigation with the preserved foundation;
3. identify dead and duplicate routes;
4. perform public/private review;
5. decide what remains history rather than migrating it.