# bAIble v2 — Integration Audit

Status: ACTIVE / EVIDENCE-BASED CONSOLIDATION

This audit checks whether the living v2 captures the useful public foundation, the generalized FederAItion lessons and the UnAiversed relationship model without copying private implementation history into public governance.

## Coverage

### Preserved and active
- core rules and language,
- original roles,
- Reality Check / Fact Check split,
- verification,
- provenance,
- public/private boundary,
- context and memory,
- Context Item contract,
- handoff,
- experiments,
- lessons,
- onboarding,
- Wolf,
- WheeAIls,
- rAIda / Watchdog public contracts,
- Human and AI views,
- failure modes,
- relationship model,
- coordination protocol,
- meaningful milestones,
- agent evals.

## Important contradictions / open alignment work

### C-001 — Reality Check / Fact Check runtime alignment
Public v2 defines RC as map/meaning alignment and FC as factual/evidential checking.

FederAItion runtime now implements the split explicitly: Fact Check evaluates evidence separately before Reality Check performs context/meaning/perspective alignment.

Status: RESOLVED IN PRIVATE RUNTIME. Runtime `36352479421` and smoke `36352479449` passed after the alignment change.

### C-002 — UnAiversed naming / representation split
FederAItion still preserves both historical spellings, but their roles are now explicit.

- `unAIversed/` = canonical active graph/runtime implementation.
- `unAiversed/` = historical/session evidence retained for provenance and meaning recovery.

Status: RESOLVED WITHOUT DESTRUCTIVE MERGE. Historical evidence remains distinguishable from the active implementation.

### C-003 — Old migration documents can outlive current structure
Migration documents are useful evidence, but the current README/navigation must remain authoritative for the living public path.

Status: CONTROLLED BY CURRENT NAVIGATION + SELF-AUDIT.

### C-004 — Historical lexicographic queue dispatcher
The earlier dispatcher selected the lexicographically last ambient queue file and could execute the wrong task.

The current active path is graph-only: queue is transport/projection, historical ambient queue files were removed, direct queue tasks are blocked by default, and Watchdog continuation derives from the persisted process graph.

Status: RESOLVED. Current graph-only runtime and smoke passed in `36352014399` and `36352014421`.

### C-005 — Named verifier role registry
The historical runtime required inline `roleRequirements` because `rAIda verifier` was not registered.

The role is now built in with the same explicit preparation requirements as the verifier tasks already exercised.

Status: RESOLVED IN PRIVATE RUNTIME. Regression passed in `36352479421` / `36352479449`.

## Epistemic rule

A successful repository/runtime test does not prove editorial completeness. Editorial completeness comes from source inventory, contradiction scan, coverage review and human acceptance.

## Current release posture

The current v2 is a living baseline: strong enough to use, explicit about remaining implementation alignment, and designed to improve through evidence rather than pretending to be finished forever.

## Current bounded runtime evidence

The dedicated rAIda integration-support task `zzzz-baible-v2-integration-verify-001` completed successfully in GitHub Actions run `36248402719` and recorded a passing runtime-test evidence artifact. This verifies the exercised runtime path only; it does not prove editorial completeness of bAIble v2.


## Latest bounded verification

The human-authorized task `BAIBLE-V2-LIVING-BASELINE-001` completed successfully in GitHub Actions run `36250143075`; evidence was recorded as `orchestrator/evidence/BAIBLE-V2-LIVING-BASELINE-001-36250143075.json` with `result: passed` and `nextTask: null`.

The companion smoke-test run `36250143030` also completed successfully, including runtime tests, Watchdog CLI checks, queue contract checks and UnAiversed validation.

Boundary: this verifies the exercised runtime path. It does not convert documentation completeness or semantic consistency into a runtime fact.
