# bAIble v2 — Onboarding (First Run)

The practical path for a human + AI pair using bAIble for the first time, whether a beginner with only the public link and no Git knowledge, or an experienced user with repositories, agents and workflows.

The goal is not to copy somebody else's private ecosystem. It is to use public bAIble as shared governance, set up an appropriate private working environment, and learn the system through one real piece of work.

## 0. Orientation and access before infrastructure

Before creating or changing anything, the AI should:

1. determine what repository, link or file access the environment actually has ([OPERATING.md](OPERATING.md) §1);
2. establish the shared map from [ECOSYSTEM.md](ECOSYSTEM.md) and the graph where accessible;
3. read [BIBLE.md](BIBLE.md), [BOUNDARY.md](BOUNDARY.md) and the human view in [README.md](README.md);
4. load other contracts when they become relevant;
5. explain the system back to the human in plain language;
6. identify what already exists;
7. run a short Reality Check if human and AI may use the same terms differently.

Do not begin by building rAIda, Watchdog, a task graph, a large semantic graph or several repositories. Start from the human's real goal.

### Start-state checkpoint

Before the first substantial step **or any recommendation to create a repository or workspace**, classify the starting environment. Never recommend "create a private repository" while WORKSPACE is UNKNOWN.

`CHECK EXISTING → CLASSIFY EXISTS / DOES NOT EXIST / UNKNOWN → REUSE IF SUITABLE → CREATE ONLY IF NEEDED`

| Field | Values |
|---|---|
| WORKSPACE | suitable private workspace exists / does not exist / unknown |
| PROJECT SOURCE OF TRUTH | identified / not yet needed / unknown |
| DURABLE CONTEXT | where important state will persist, or TEMPORARY-CHAT-ONLY |
| VISIBILITY | public/private boundary understood / unresolved |
| ACCESS / AUTHORITY | what the AI can inspect or change / unknown |
| CURRENT STATE | existing project state / clean start / unknown |

If an unknown field matters to the next action, resolve it first. A later question does not repair an earlier recommendation that already assumed the unknown. A chat may be used temporarily, but it must not silently become durable project memory.

`UNKNOWN START STATE → CHECK / ASK → BOUNDED START STATE → FIRST PROJECT STEP`

The checkpoint is lightweight. It is not a demand to create repositories before useful work.

## 1. The AI is teacher and assistant

Before meaningful work, establish as needed: **intent**, **known**, **interpretation**, **unknown**, **scope**, **authority**, **destination** (where information belongs), **evidence**, **verification**, **next authorized step**.

If two plausible interpretations would change the result materially, do not silently choose one.

For a beginner, explain terms as `NAME → PLAIN LANGUAGE → WHY IT MATTERS → SMALLEST EXAMPLE → USE IT`. Do not require the whole architecture before useful work. Do not hide important boundaries behind automation.

**New user:** may have only the public link. Classify access, orient from the map, explain plainly, discover what exists, set a safe public/private boundary, create the minimum private workspace only if needed, choose one bounded task, verify it, keep only what matters.

**Experienced user:** inspect the intended roles of existing structures, map them onto bAIble responsibilities, avoid duplicate repositories or mechanisms, find gaps in scope, authority, evidence, verification, continuity or context, and add only what solves a demonstrated problem.

Experience changes the amount of explanation, not the governance boundary.

### Adapt to the human, not to a fixed curriculum

Watch for signals during real work: the user already understands a concept; the same reminder keeps helping; the same misunderstanding keeps being corrected; several tasks, tools or agents now need coordinating; relationships or contradictions are getting hard to keep; continuity across sessions is fragile; the user spends more effort compensating for the system than doing the work.

`USE → OBSERVE FRICTION / COMPETENCE → DISCOVER RELEVANT CAPABILITY → LOAD ITS CONTRACT → APPLY LIGHTWEIGHT BEHAVIOUR / OFFER INFRASTRUCTURE → RE-EVALUATE`

Existing behaviour may activate without the human naming it; new infrastructure stays a separate, explained choice ([OPERATING.md](OPERATING.md) §6). Reduce explanation and reminders when they no longer help. Do not turn observed behaviour into a permanent label for the user.

## 2. Existing structure or new workspace

**If suitable private repositories exist,** inspect their roles before creating anything. Ask where durable context lives, where implementation lives, what is public, what is private, who can change each location, and what already serves as current state, evidence, handoff or project state. Prefer reuse over duplication.

**If none exists,** start with one private repository (for example `my-private-workspace`). It can hold context, evidence, experiments, lessons and even implementation while the project is small. Split only when scale, security, access or workflow complexity shows the need.

```text
my-private-workspace/
├── README.md
├── CURRENT.md
├── projects/
├── context/
├── evidence/
├── experiments/
├── lessons/
│   └── candidates/
├── handoffs/
└── unaiversed/
```

A starter shape, not a law. Do not create empty architecture because it appears here.

- **README** explains what the workspace is for, that public governance comes from bAIble, that project context, evidence and implementation stay private, and who may change it.
- **CURRENT** answers: what are we trying to achieve, what is active, what is the last verified state, what is uncertain or blocked, what evidence matters, what is the exact next authorized action. Keep it short: a recovery checkpoint, not a diary and not truth.

## 3. Where information goes

| Destination | Holds |
|---|---|
| Public bAIble | reusable governance, generic workflows, generalized lessons |
| Private workspace | context, decisions, evidence, experiments, handoffs, private lessons |
| Private project / source of truth | implementation and project-specific authoritative artifacts |
| Secure secret store | credentials, tokens, private keys and secrets |

These are functional roles, not repository counts. If the destination is unclear, mark it UNKNOWN and resolve it before publishing or committing. Before anything private becomes public: `PRIVATE EXPERIENCE → GENERALIZE → DE-SENSITIZE → VERIFY → REALITY CHECK → PUBLIC CANDIDATE` ([BOUNDARY.md](BOUNDARY.md)).

## 4. Starter instruction for your AI

> Use bAIble v2 as the public governance framework for our work.
>
> First orient yourself from README.md, OPERATING.md, BIBLE.md and BOUNDARY.md. Use ONBOARDING.md as the adoption path.
>
> Do not treat bAIble as project memory and do not copy another person's private ecosystem.
>
> Before creating infrastructure, inspect what private repositories or workspaces already exist and reuse suitable structure where possible.
>
> Before significant work, identify intent, knowns, interpretation and unknowns; role, scope and authority; the public/private destination; expected evidence and verification; the next authorized action.
>
> During work: do not silently guess material requirements; preserve provenance; do not treat records, relations or context as truth; distinguish implementation, verification and acceptance; use Reality Check for human/AI map alignment and Fact Check for factual claims; stop, recover or escalate when context, authority or approval is missing.
>
> When work changes hands, use HANDOFF → RECONSTRUCT → CHECK → CONTINUE.
>
> Start with one real project and add machinery only when the real workflow shows the need.

The AI then explains its understanding back. That explanation is only the AI's working map, not a completed Reality Check: the human must have a real chance to confirm, correct, refine or leave an explicit open difference.

## 5. First Reality Check

**Human map:** What am I trying to achieve? What do I think bAIble will do for me? What already exists? What should stay private? What do I expect the AI to do on its own?

**AI working map:** What does the AI believe the intent is? What does it think already exists? What is inferred rather than received? What authority does it believe it has? What remains unknown or conflicting?

Classify differences as aligned, missing, different interpretation, different importance, different relation, unresolved or intentionally preserved. A difference is not automatically an error. Full procedure: [REALITY_CHECK.md](REALITY_CHECK.md).

## 6. One real project

Do not learn bAIble only as documentation. Choose one real problem and capture only what is needed: **intent**, **context**, **scope**, **known**, **unknown**, **authority**, **evidence** (what would show success), **next step** (small, authorized, preferably reversible). Then follow the work loop in [BIBLE.md](BIBLE.md).

Prefer `EXPLAIN → CONFIRM WHEN NEEDED → DO → VERIFY → RECORD` over long chains of hidden action.

## 7. Add parts only when reality needs them

| Add | When |
|---|---|
| UnAiversed-style mapping | relationships get hard to keep; several perspectives matter; contradictions or uncertainty must stay visible; flat notes no longer explain why things relate |
| rAIda-style coordination | several agents, tasks or tools need coordinating; role, scope or gates need active enforcement; evidence and verification must be coordinated |
| Watchdog-style continuity | the workflow has observable state, several authorized transitions exist, and stop/retry/continue/escalate needs explicit rules |
| Task/process graphs | dependencies matter; several transitions are possible; task existence must be separated from authority; queue order is not enough |
| WheeAIls | a beginner needs relevant reminders; the same small mistakes recur; support can reduce repeated prompting |

Do not add architecture because it exists in the ecosystem. Add it because a real problem shows the need. Continuity across sessions: [CONTINUITY.md](CONTINUITY.md). Learning without rule inflation: [LEARNING.md](LEARNING.md).

## 8. Growth levels

0 — Příchozí: orientation and vocabulary.
1 — Pozorovatel: observation vs interpretation.
2 — Učeň: rules, scope, authority, evidence and verification.
3 — Pracovník: bounded execution and durable evidence.
4 — Samostatný agent: prepare, reason, execute and record without crossing gates.
5 — Spolupracovník prostředí: context, handoffs, verification, continuity and improvement.

These are orientation aids, not permissions or status claims. The system responds to observed need, not to a maturity score, and support shrinks when it is no longer useful.

## 9. Signs onboarding succeeded

The human can answer: what bAIble is and is not; what stays public and private; where durable context and implementation live; what the current intent is; what is known versus inferred or unknown; who decides the next material step; what counts as evidence; what Reality Check, Fact Check and Verification are for; how another agent would reconstruct the work; when to add UnAiversed, rAIda or Watchdog; what to do with a reusable lesson.

The AI can answer the same without pretending private data is public, capability is authority, or documentation is truth. These distinctions matter more than reproducing any particular repository layout.

**Graduation** is not memorizing bAIble. It is working safely without constant support wheels: `GOAL → BOUNDED WORK → EVIDENCE → VERIFY → ALIGN → PRESERVE → CONTINUE`. An experienced user may skip beginner explanations, never the boundaries. Using only the architecture a problem needs must not hide the rest of the ecosystem from a capable agent.

## Templates

Minimal contracts, not mandatory infrastructure. Work state and handoff: [CONTINUITY.md](CONTINUITY.md). Agent scope: Agent Profile in [OPERATING.md](OPERATING.md). Experiment record: [LEARNING.md](LEARNING.md).

**Project context:** purpose, scope, authoritative sources, constraints, dependencies, out of scope, last verified.

**Project state:** current objective, status, completed, in progress, blocked, known unknowns, next verified action, last updated.

**Decision:** decision ID, decision, question resolved, scope, status, authority, approval, evidence / sources, alternatives, reasoning, assumptions, limitations, verification criteria, review / reversal condition.
