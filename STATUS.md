# bAIble v2 — Status

What is built, tested and verified, what remains open, and the self-audit before any release. Columns follow the ladder for work we build ([VERIFICATION.md](VERIFICATION.md)): DESIGNED → BUILT → TESTED → VERIFIED → INTEGRATED.

| Area | Designed | Built | Tested | Verified | Integrated |
|---|---|---|---|---|---|
| Core governance | yes | yes | documentation audit | current repo inspected | yes |
| Human View (README) | yes | yes | navigation/self-audit | links inspected | yes |
| AI View (OPERATING) | yes | yes | activation/discovery eval scenarios defined | repo presence inspected; cross-agent behavior still under evaluation | yes |
| AI discovery/loading layer | yes | yes — discovery contract, adapters, graph routing, bundle tooling and CI | repository integrity CI passed; EXP-AI-DISCOVERY-001 defined | structurally verified; NOT YET cross-agent behavior verified | yes |
| Reality Check contract | yes | yes | anti-drift test defined | current public meaning inspected | yes |
| Fact Check contract | yes | yes | outcome model defined | current public meaning inspected | yes |
| Context Item / relations | yes | yes | private prototype tests exist | public contract + private evidence partially verified | yes |
| rAIda public contract | yes | private runtime built | dedicated private run passed | bounded runtime behavior verified for the exercised path; editorial work not covered | yes |
| Watchdog public contract | yes | private runtime built | live tests exist | bounded continuity behavior verified | yes |
| WheeAIls | yes | public relevance contract built | activation/relevance evals defined | concept + behavior contract; cross-agent verification pending | yes |
| Wolf | yes | public onboarding/activation contract built | clean-chat behavioral observation + evals defined | bounded observation only; systematic cross-agent verification pending | yes |
| RC / FC runtime alignment | yes | private runtime aligned | private runtime + smoke | bounded behavior verified | yes |
| UnAiversed private naming consolidation | concept defined | active + historical paths explicitly separated | private cleanup verified by repository inspection | canonical active path is unAIversed; unAiversed retained as history | yes |
| Local process contracts / rule stack | yes | private runtime built | multi-stage bounded + live tests | versioning/discovery/locked authority path verified | yes |
| Task/process graph | yes | private runtime built | live graph projection + continuation | graph-only active dispatch verified | yes |
| Failure / recovery | yes | private runtime built | live fail→retry→recovery chain | original failure preserved; recovered process verified | yes |
| Reconstructable handoff | yes | private runtime built | restart/reconstruction tests | graph/evidence/rule drift forces reconstruct | yes |
| Perspective divergence | yes | private runtime built + UnAiversed object model | runtime + UnAiversed tests | preserved/nonblocking vs blocking divergence verified | yes |
| Semantic reconstruction audit | yes | private runtime built | integration coverage audit | current source inventory covered with explicit open issues | yes |
| Real project pilot | bounded pilot defined | private viewer build executor | private run + smoke | real viewer branch build passed through graph/rAIda/evidence path | yes |

## Release claim

The current `main` repository is a **usable living v2 baseline**. Capability-aware discovery/loading is now integrated into the public baseline; its repository structure and generation path are verified, while systematic cross-agent behavior remains under evaluation.

**Ecosystem baseline status: COMPLETE (2026-09-27).**

It is not claimed to be immutable, universally validated, or to make individual applications/projects complete. "Complete" here means the core ecosystem layers are present, integrated and exercised; deployment hardening and future evolution remain ongoing.

The strongest accurate claim is:

**Public governance, navigation, context/relationship model and coordination boundaries are integrated; the previously recorded RC/FC, queue-dispatch, verifier-role and private UnAiversed path ambiguities are now explicitly resolved in the current private runtime baseline. Remaining gaps are deployment hardening and future evolution, not missing core ecosystem layers.**

A dedicated bounded rAIda task `BAIBLE-V2-LIVING-BASELINE-001` completed successfully in a private GitHub Actions run. The companion smoke-test run also completed successfully, including the runtime suite, Watchdog CLI smoke checks, queue contract smoke check and UnAiversed validation. This is runtime evidence only; it is not proof that every editorial or semantic claim in the public repository is correct.

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

A real project pilot built the private real-project viewer branch through this graph/rAIda/evidence path; the companion smoke run passed (private runs recorded in FederAItion).

This evidence supports the baseline-complete claim within the exercised scope. It does not prove browser rendering, building identity, project completion, universal correctness or future compatibility.

## Consolidation — 2026-10-20

An ecosystem audit found the same rules rewritten in up to nine files with drifting variants. The repository was consolidated from 50 documents to 20 active ones plus [history/](history/); [vocabulary.json](vocabulary.json) became the single home for closed vocabularies, and the validator now checks the graph, documents and publication boundary against it. Old-to-new file map: [history/README.md](history/README.md).

## Open questions

These stay visible rather than being invented away:

- Does documented governance actually activate at the moment of transition in fresh agents, without the human naming it? (activation recall/precision and human compensation rate, [AGENT_EVALS.md](AGENT_EVALS.md) M03–M04; not yet measured systematically)
- Full production implementation of a canonical UnAiversed graph and viewer.
- How much relationship metadata should become machine-enforced schema versus documented contract.
- The exact interface for the Human and AI views.
- How reminders are selected automatically across different agent environments.
- How a generated single-file context bundle is distributed without becoming a second truth store.
- Which checks need independent evidence in each project domain.
- How living public releases are versioned without history taking over the main navigation.

## Self-audit before a release

Automated by `scripts/validate_discovery.py`: referenced files exist; graph resources, routing hints and llms.txt links resolve; graph predicates, node types and failure-mode coverage match [vocabulary.json](vocabulary.json); blocker lists use only canonical states; every active document is in the manifest; no case-only path collisions; no private run identifiers or listed private project names.

Checked by a person or reviewing agent:

- purpose and scope are clear; a beginner can start without private context;
- Human and AI views stay understandable; the full capability map stays discoverable while mechanisms are dormant;
- adapters point to canonical sources instead of becoming duplicate truth stores;
- principles are distinguishable from examples and culture;
- facts, observations, interpretations, hypotheses, decisions, evidence and unknowns stay distinguishable;
- Reality Check, Fact Check, Verification and Acceptance are not collapsed;
- human authority stays visible; rAIda, Watchdog, Wolf and WheeAIls do not acquire authority;
- evidence and verification are distinct from self-report; implementation claims have accessible evidence;
- contradictions show the actual claims and sources, not a yellow status;
- provenance is preserved; relations do not transfer truth, scope, authority or visibility;
- restricted-access agents have a bounded fallback without repeated manual navigation;
- generalized lessons do not expose private origins; sensitive identifiers and credentials are absent;
- optional architecture exists only where real need justifies it; history does not override current navigation;
- a concept has one home (candidate R-025); runtime or test success is not presented as editorial completeness.

A failed item triggers investigation. It is not by itself proof that the underlying idea is wrong.
