# bAIble v2 — Ecosystem

The canonical semantic model: what exists, who is responsible for what, and how the parts relate. [ECOSYSTEM_GRAPH.json](ECOSYSTEM_GRAPH.json) is its machine-readable seed; every map or view is drawn over this one model.

## Center

**bAIble + FederAItion + UnAiversed form one coordinated ecosystem.** It is an architectural metaphor for three complementary domains, not a hierarchy and not a religious statement. No domain is the universal source of truth.

`HI + AI ↔ bAIble + FederAItion + UnAiversed`

### Active entities

**HI — Human Intelligence:** intent, values, material decisions, acceptance, intervention gates and responsibility for consequential choices.

**AI — Artificial Intelligence:** bounded interpretation, planning, execution, checking, recording and assistance according to role, scope and evidence.

HI and AI are participants, not components. They jointly create, use, inspect, repair and evolve the ecosystem.

### Three domains

**bAIble** — the shared bible of HI and AI: rules, principles, roles, language, lessons and reusable workflows. Public, evolving, and meant to help new people start. It answers: how should we work, why does a guardrail exist, what vocabulary and roles are shared, how do lessons become reusable, what must remain explicit.

**FederAItion** — the working machinery: checks, sequences, the ability to continue and hand over, runtime state and evidence. It also carries the reminder that human and AI understanding differ, which helps development but can be destructive when unnoticed, and the principle for comparing thinking between us. It holds insights not yet integrated or defined. It answers: what task is active, who or what is authorized, what state the work is in, what was actually executed, what evidence exists, what transition may happen next.

**UnAiversed** — the shared space of understanding. Each participant may look at it, read it and use it differently, but when we solve something we must be able to meet where we need to and recall only what we need; or explore it like a universe. It answers: what is related to what, in which context, from which origin, with what status, and where meanings, claims, decisions or evidence diverge. A place to meet is not a truth store, not hidden model memory and not a transcript archive.

## Operational constellation

| Part | Does | Does not |
|---|---|---|
| Human | intent, material decisions, acceptance, gates | become infallible about facts |
| bAIble | governance, language, roles, lessons, workflows | hold private project memory |
| rAIda | THINK / COORDINATE / REMEMBER-TO-CHECK | inherit human product authority |
| Agent | PREPARE / REASON / EXECUTE / RECORD | act beyond its profile ([OPERATING.md](OPERATING.md)) |
| FederAItion | state, runtime, evidence, durable project context | become public governance |
| UnAiversed | context relationships, maps, perspectives | declare truth |
| Reality Check | ALIGN human and AI working maps | replace Fact Check |
| Fact Check | VERIFY claims against evidence | infer human–AI alignment |
| Verification | test whether the required result holds | equal acceptance |
| Watchdog | CONTINUE / MONITOR / ESCALATE authorized work | invent work |
| Wolf | ORIENT / TEACH / ONBOARD | decide, verify or authorize |
| WheeAIls | surface relevant reminders | become memory or authority |
| Repository | durable memory | prove truth by storing |

No layer silently acquires another layer's authority.

## Roles

Original bAIble v0.1 roles remain explicit execution responsibilities:

- **Human / Product Owner** — intent, product decisions, acceptance and material authority.
- **Architect** — system structure, boundaries and architectural consequences.
- **Developer** — bounded technical changes.
- **QA** — tests the required behaviour and reports actual results.
- **Reviewer** — defects, regressions, security/scope problems and inconsistencies.
- **Documentation Agent** — durable knowledge, provenance, decisions and lessons.

These are responsibilities, not necessarily separate AI instances. "Agent" is a generic execution category: a concrete agent may perform one or several roles only when its authority and scope are explicit. A role describes responsibility; an Agent Profile ([OPERATING.md](OPERATING.md)) describes how one agent may perform it here.

## Levels of the map

| Level | Contains | Answers |
|---|---|---|
| L1 Constellations | bAIble, FederAItion, UnAiversed, HI, AI | what the ecosystem is, who participates, who is responsible |
| L2 Systems | rAIda, Watchdog, Reality Check, Fact Check, Verification, roles, memory, learning, onboarding, context, security, evidence | major systems and responsibility boundaries |
| L3 Mechanisms | preflight, scope checks, evidence chains, handoffs, Context Items, task lifecycle, authorization, public/private boundary, evals, recovery, continuity | how work actually moves |
| L4 Atomic relations | claims, observations, decisions, evidence, sources, states, limitations, next checks, authority edges, contradictions | why one mechanism may or may not change another state |

Zooming from philosophy to operational detail must not change an object's semantic identity.

## One graph, many views

`ONE CANONICAL GRAPH → MULTIPLE PURPOSE-SPECIFIC VIEWS`

A view may prioritize different information but must not create different facts, authority or provenance. Views include the Human view ([README.md](README.md)), the AI view ([OPERATING.md](OPERATING.md)), the Universe view, Human and Agent journeys, the AI Discovery / Capability view, Builder architecture, Operational flow, Verification, Context / Memory, Failure, Onboarding and Live system.

The AI Discovery / Capability view answers which capabilities exist, which canonical resource defines each, what signals make it relevant, what is loaded versus merely discoverable, what the environment cannot retrieve, and what authority is still required. It supports `NEED → NODE / RELATION → RESOURCE → LOAD CONTRACT → ACTIVATE IF RELEVANT → CHECK AUTHORITY`, never `SHORT AI LIST → EVERYTHING ELSE DISAPPEARS`.

**Geometry.** Do not render the ecosystem as a simple mind-map tree. The three domains are overlapping, gravitationally bound galaxies; an object may belong to several contexts and a relation may matter as much as the nodes it connects.

**Relations are first-class.** Do not draw anonymous lines when the relationship matters. Predicates, relation metadata and the contradiction contract are defined in [CONTEXT.md](CONTEXT.md) and [vocabulary.json](vocabulary.json). A relation is explicit rather than inferred from proximity, and it is not true merely because it exists.

**Failure anomalies sit where they distort.** In a spatial view failure modes may appear as local anomalies rather than normal nodes, placed at what they deform: Context Drift near AI ↔ UnAiversed ↔ task context; Meaning Drift near language and named mechanisms; Scope Drift near intent ↔ rAIda ↔ execution; False Done near execution ↔ evidence ↔ verification; False Continuity near handoffs; Activity Substitution near intent ↔ next authorized action; Memory Inflation near context activation; Automation Without Authority near rAIda, Watchdog and task transitions; Record ≠ Truth near repository, Context Items and UnAiversed; Decision ≠ Truth near decisions over time; User Adaptation Hides Failure near the human ↔ AI loop. Full list: [FAILURE_MODES.md](FAILURE_MODES.md).

**Visual epistemics.** A viewer distinguishes at least observation, claim, interpretation, decision, rule, lesson, evidence, verification, mechanism, role, system, risk, question and experiment. Storage, repetition or visual prominence must never promote an item to truth.

**History** appears only where it explains current structure or protects meaning, such as why rAIda, Watchdog, Reality Check and Fact Check are separate. Routine chronology stays in [history/](history/).

**Design principle.** The map must show not only what exists, but why it exists, what it relates to, what may trust it, who may act on it, and what happens when it fails. That is the difference between a decorative mind map and UnAiversed.

## Glossary

| Term | Meaning | Status |
|---|---|---|
| bAIble | Shared public governance, language, guardrails, verification discipline and generalized learning | Established |
| FederAItion | Private operational layer: orchestration, durable evidence, implementation state, project context | Implemented project layer |
| UnAiversed | Shared space of understanding and relations; supports many views; not truth | Concept + implementation |
| HI / AI | Human Intelligence / Artificial Intelligence as participants | Established |
| rAIda | THINK / COORDINATE / REMEMBER-TO-CHECK | Implemented in FederAItion; public contract here |
| Watchdog | CONTINUE / MONITOR / ESCALATE within authorized boundaries | Implemented in FederAItion; public contract here |
| Wolf | ORIENT / TEACH / ONBOARD persona | Established concept |
| WheeAIls | Support wheels that surface relevant reminders without authority | Established concept |
| Reality Check (RC) | Compare human and AI working maps and expose divergence | Restored original meaning |
| Fact Check (FC) | Check claims, facts, assumptions and evidence | Split from former RC use |
| Verification | Check whether the required result actually holds | Established |
| Handoff | Structured transfer of task context, authority, evidence and next state | Established |
| Context Item | Addressable context with provenance, scope, status, relations, visibility and next check | Established v2 contract |
| Provenance | Origin, source and status trail of information | Established |
| Gray data | Unresolved input that must not automatically become fact, requirement or conclusion | Evolving |
| Semantic continuity | Preservation of meaning across time, context loss, handoffs or representation changes | Evolving |
| Human View / AI View | Navigation over the same graph for humans / for agents | Established |
| Canonical graph | The shared semantic relationship model; not itself automatic truth | Established |
| Failure mode / požírač hvězd | Recurring process distortion attached to what it affects | See FAILURE_MODES |

Names are not dependencies. Implementations may use different names. A surviving name, record or relation does not prove semantic continuity.
