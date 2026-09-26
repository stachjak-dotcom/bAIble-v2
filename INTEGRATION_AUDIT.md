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

### C-001 — Reality Check runtime semantics lag governance
Public v2 now defines RC as map alignment and FC as factual/evidential checking. FederAItion runtime historically combined some evidence checks under Reality Check.

Status: GOVERNANCE CORRECTED; RUNTIME ALIGNMENT STILL REQUIRES A SEPARATE IMPLEMENTATION CHANGE AND TEST.

### C-002 — UnAiversed naming / representation split
FederAItion currently contains both `unAiversed/` and `unAIversed/` paths with related but different material.

One line represents the human/AI map and session-history direction; the other contains the graph-record implementation, JSON-LD relation model and rAIda bridge.

Status: NOT SILENTLY RESOLVED. Public v2 generalizes both as one UnAiversed concept and records the semantic model. Private cleanup should preserve evidence before any rename or merge.

### C-003 — Old migration documents can outlive current structure
Migration documents are useful evidence, but the current README/navigation must remain authoritative for the living public path.

Status: CONTROLLED BY CURRENT NAVIGATION + SELF-AUDIT.

### C-004 — Current push dispatcher selects the lexicographically last queue file
During the bounded bAIble-v2 verification request, a newly added queue task was not executed because the push workflow selects `readdirSync(...).sort().pop()`. A legacy lowercase filename sorted after the intended uppercase task and was executed instead.

Status: OBSERVED AND REPRODUCED. The intended task was later explicitly made last in the current ordering and successfully executed. The dispatcher selection rule remains a private runtime design issue to fix separately.

### C-005 — Named verifier role was not defined in the runtime role registry
The first intended task run reached the correct queue item but failed preflight because `rAIda verifier` had no built-in role requirements. Supplying explicit `roleRequirements` preserved the bounded verifier role without modifying runtime role definitions.

Status: OBSERVED; BOUNDED TASK CORRECTED. General role-registration design remains private runtime work.

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
