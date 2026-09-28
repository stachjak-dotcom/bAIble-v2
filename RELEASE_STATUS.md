# bAIble v2 — Release Status

Status model:

- **DESIGNED** — concept/contract is explicitly defined.
- **BUILT** — artifact or implementation exists.
- **TESTED** — relevant test/evaluation has actually run.
- **VERIFIED** — evidence supports the claimed behavior within scope.
- **INTEGRATED** — connected into the canonical navigation/working model.

| Area | Designed | Built | Tested | Verified | Integrated |
|---|---|---|---|---|---|
| Core governance | yes | yes | documentation audit | current repo inspected | yes |
| Human View | yes | yes | navigation/self-audit | links inspected | yes |
| AI View | yes | yes | activation/discovery eval scenarios defined | repo presence inspected; cross-agent behavior still under evaluation | yes |
| AI discovery/loading layer | yes | yes — discovery contract, adapters, graph routing, bundle tooling and CI | repository integrity CI passed; EXP-AI-DISCOVERY-001 defined | structurally verified; NOT YET cross-agent behavior verified | yes |
| Reality Check contract | yes | yes | anti-drift test defined | current public meaning inspected | yes |
| Fact Check contract | yes | yes | outcome model defined | current public meaning inspected | yes |
| Context Item / relations | yes | yes | private prototype tests exist | public contract + private evidence partially verified | yes |
| rAIda public contract | yes | private runtime built | dedicated run 36248402719 passed | bounded runtime behavior verified for the exercised path; editorial work not covered | yes |
| Watchdog public contract | yes | private runtime built | live tests exist | bounded continuity behavior verified | yes |
| WheeAIls | yes | public relevance contract built | activation/relevance evals defined | concept + behavior contract; cross-agent verification pending | yes |
| Wolf | yes | public onboarding/activation contract built | clean-chat behavioral observation + evals defined | bounded observation only; systematic cross-agent verification pending | yes |
| RC / FC runtime alignment | yes | private runtime aligned | runtime 36352479421 + smoke 36352479449 | bounded behavior verified | yes |
| UnAiversed private naming consolidation | concept defined | active + historical paths explicitly separated | private cleanup verified by repository inspection | canonical active path is unAIversed; unAiversed retained as history | yes |
| Local process contracts / rule stack | yes | private runtime built | multi-stage bounded + live tests | versioning/discovery/locked authority path verified | yes |
| Task/process graph | yes | private runtime built | live graph projection + continuation | graph-only active dispatch verified | yes |
| Failure / recovery | yes | private runtime built | live fail→retry→recovery chain | original failure preserved; recovered process verified | yes |
| Reconstructable handoff | yes | private runtime built | restart/reconstruction tests | graph/evidence/rule drift forces reconstruct | yes |
| Perspective divergence | yes | private runtime built + UnAiversed object model | runtime + UnAiversed tests | preserved/nonblocking vs blocking divergence verified | yes |
| Semantic reconstruction audit | yes | private runtime built | integration coverage audit | current source inventory covered with explicit open issues | yes |
| Real project pilot | bounded pilot defined | Siemensova viewer build executor | run 36352692292 + smoke 36352692276 | real viewer branch build passed through graph/rAIda/evidence path | yes |

## Release claim

The current `main` repository is a **usable living v2 baseline**. Capability-aware discovery/loading is now integrated into the public baseline; its repository structure and generation path are verified, while systematic cross-agent behavior remains under evaluation.

**Ecosystem baseline status: COMPLETE (2026-09-27).**

It is not claimed to be immutable, universally validated, or to make individual applications/projects complete. "Complete" here means the core ecosystem layers are present, integrated and exercised; deployment hardening and future evolution remain ongoing.

The strongest accurate claim is:

**Public governance, navigation, context/relationship model and coordination boundaries are integrated; the previously recorded RC/FC, queue-dispatch, verifier-role and private UnAiversed path ambiguities are now explicitly resolved in the current private runtime baseline. Remaining gaps are deployment hardening and future evolution, not missing core ecosystem layers.**

A dedicated bounded rAIda task `BAIBLE-V2-LIVING-BASELINE-001` completed successfully in GitHub Actions run `36250143075`. The companion smoke-test run `36250143030` also completed successfully, including the runtime suite, Watchdog CLI smoke checks, queue contract smoke check and UnAiversed validation. This is runtime evidence only; it is not proof that every editorial or semantic claim in the public repository is correct.


## Ecosystem baseline completion evidence

The private FederAItion runtime now exercises the public governance boundaries through:
- scoped/versioned local contracts;
- authority/trust/provenance checks;
- graph-only task authority;
- Watchdog continuation;
- bounded recovery;
- reconstructable handoff;
- perspective divergence;
- semantic reconstruction coverage;
- separate Fact Check and Reality Check.

A real project pilot built the Siemensova/Cesium viewer branch through this graph/rAIda/evidence path in run `36352692292`; companion smoke `36352692276` passed.

This evidence supports the baseline-complete claim within the exercised scope. It does not prove browser rendering, building identity, project completion, universal correctness or future compatibility.
