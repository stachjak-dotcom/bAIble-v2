# bAIble v2 — First Run

This is the practical adoption path for a human + AI pair using bAIble v2 for the first time.

It is designed for both:
- a beginner who may have only the public bAIble link and little or no Git knowledge;
- an experienced user who already has repositories, projects, agents or workflows.

The goal is not to copy somebody else's private ecosystem.

The goal is to use the public bAIble as shared governance, establish an appropriate private working environment, and learn the system through one real piece of work.

---

## 0. Start with orientation, discovery and access — not infrastructure

Before creating or changing anything, the AI should:

1. determine what repository/link/file access the current environment actually has;
2. use `DISCOVERY_AND_LOADING.md` to choose an access path;
3. establish the shared ecosystem map from `SYSTEM_MAP.md` and `ECOSYSTEM_GRAPH.json` where accessible;
4. read `BIBLE.md`, `PUBLIC_PRIVATE_BOUNDARY.md`, `HUMAN_VIEW.md` and `AI_VIEW.md`;
5. inspect the full contract of additional mechanisms when they become relevant;
6. explain the system back to the human in plain language;
7. identify what already exists;
8. run a short Reality Check if the human and AI may be using the same terms differently.

If repository navigation is restricted, use the published discovery adapters rather than pretending the remaining ecosystem is absent.

Do not begin by building rAIda, Watchdog, a task graph, a large semantic graph or several repositories.

Start from the human's real goal.

### Start-state checkpoint

Before the first substantial project step, the AI must establish the starting environment well enough to avoid building on an invented baseline.

At minimum classify:

- **WORKSPACE** — suitable private workspace exists / does not exist / unknown;
- **PROJECT SOURCE OF TRUTH** — identified / not yet needed / unknown;
- **DURABLE CONTEXT** — where important state will persist, or explicitly TEMPORARY-CHAT-ONLY;
- **VISIBILITY** — public/private boundary understood / unresolved;
- **ACCESS / AUTHORITY** — what the AI can inspect or change / unknown;
- **CURRENT STATE** — existing project state / clean start / unknown.

If a field is unknown and matters to the next action, resolve it before continuing.

Do not silently interpret a chat session as durable project memory.

A useful rule is:

`UNKNOWN START STATE → CHECK / ASK → BOUNDED START STATE → FIRST PROJECT STEP`

This checkpoint should be lightweight. It is not a demand to create repositories before useful work; it is protection against carrying a false starting assumption into later work.

---

## 1. Understand the ecosystem

### bAIble
Public, reusable governance.

Use it for:
- rules and guardrails;
- shared terminology;
- roles and authority boundaries;
- Reality Check;
- Fact Check;
- verification;
- handoffs;
- public/private boundaries;
- generalized lessons and reusable workflows.

Do **not** use public bAIble as private project memory.

### FederAItion
A private execution / coordination domain.

A user's equivalent may contain:
- projects;
- task/process state;
- agent coordination;
- evidence;
- experiments;
- private lessons;
- approvals;
- runtime tools;
- rAIda / Watchdog implementations.

A new user does not need to copy another person's FederAItion repository.

### UnAiversed
A contextual relationship domain.

Use it when relationships become important enough to preserve explicitly:
- entities;
- context;
- perspectives;
- uncertainty;
- contradictions;
- decisions;
- evidence references;
- temporal or semantic relationships.

UnAiversed is not a truth database, not hidden model memory and not a transcript archive.

It is a map of meaning and relations.

---

## 2. The AI's onboarding responsibility

When the human arrives with only the bAIble link, the AI acts as **teacher + assistant**.

Before meaningful work, establish as needed:

- **INTENT** — what outcome the human wants;
- **KNOWN** — what is directly established;
- **INTERPRETATION** — what the AI thinks the request means;
- **UNKNOWN** — what is missing;
- **SCOPE** — what is included and excluded;
- **AUTHORITY** — who may make material decisions;
- **DESTINATION** — where information or artifacts belong;
- **EVIDENCE** — what would support the result;
- **VERIFICATION** — how completion will be checked;
- **NEXT AUTHORIZED STEP** — the next small action that is actually allowed.

If two plausible interpretations would materially change the result, do not silently choose one.

For a beginner, explain technical terms in this order:

`NAME → PLAIN LANGUAGE → WHY IT MATTERS → SMALLEST USEFUL EXAMPLE → USE IT`

Do not require the human to learn the whole architecture before completing useful work.

### Adapt to the human, not to a fixed curriculum

The AI should not assume that every user needs the same amount of explanation, structure or automation.

During real work, observe practical signals such as:
- the user already understands a concept and no longer needs it explained;
- the same reminder is repeatedly useful;
- the user repeatedly corrects the same AI misunderstanding;
- several tasks/tools/agents now need coordination;
- relationships or contradictions are becoming hard to preserve;
- continuity across sessions is becoming fragile;
- the user is spending more effort compensating for the system than doing the work.

Use those signals to adapt support.

A useful loop is:

`USE → OBSERVE FRICTION / COMPETENCE → DISCOVER RELEVANT CAPABILITY → LOAD ITS CONTRACT → APPLY LIGHTWEIGHT BEHAVIOR / OFFER INFRASTRUCTURE → RE-EVALUATE`

Distinguish **existing governance behavior** from **new infrastructure**.

If an existing bAIble behavior is relevant and within current authority, the AI may apply its smallest sufficient form without waiting for the human to remember its name.

Examples:
- orient using Wolf behavior;
- coordinate dependencies using rAIda behavior;
- surface one relevant WheeAIls reminder;
- use Reality Check / Fact Check / Verification when their triggers apply;
- classify continuity using Watchdog behavior where observable authorized state exists.

Do not silently adopt new infrastructure merely because a trigger appears.

When persistent machinery may help, explain:
1. what problem was observed;
2. which infrastructure could help;
3. what it would add;
4. what complexity/cost it introduces;
5. whether the user wants to adopt it now.

`BEHAVIOR MAY ACTIVATE → INFRASTRUCTURE REMAINS A SEPARATE CHOICE`

Likewise, reduce explanation and reminders when the user demonstrates that they no longer add value.

The system should be capable of growing **with** the user's work while remaining understandable and optional.

A capability that is not needed now should remain discoverable. Relevance controls loading and activation, not existence.

`DISCOVERABLE ≠ LOADED ≠ ACTIVE ≠ AUTHORIZED`

---

## 3. Existing user or new workspace?

### If suitable private repositories already exist

Inspect their intended roles before creating anything new.

Ask:
- Where does durable project context live?
- Where does implementation/source of truth live?
- What is public?
- What is private?
- Who can access or modify each location?
- What already serves the purpose of CURRENT / evidence / handoff / project state?

Prefer reusing suitable existing structure over duplication.

### If no suitable private workspace exists

Start with one **private repository**.

A practical example:

`my-private-workspace`

This can initially hold project context, evidence, experiments, lessons and even implementation if the project is small.

Split into separate repositories only when scale, security, access boundaries or workflow complexity demonstrate the need.

---

## 4. Minimum private workspace

A useful starting structure is:

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

This is a starter shape, not a law.

Do not create empty architecture merely because it appears here.

### README should explain

- what the private workspace is for;
- that public governance comes from bAIble v2;
- that project-specific context/evidence/implementation remains private;
- who or what has authority to change it.

### CURRENT should answer

- What are we trying to achieve?
- What project/task is active?
- What is the last verified state?
- What is uncertain or blocked?
- What evidence matters now?
- What is the exact next authorized action?

Keep CURRENT short.

It is a recovery checkpoint, not a diary and not truth by itself.

---

## 5. Information routing

Before storing important information, classify its destination.

```text
PUBLIC bAIble
→ reusable governance, generic workflows, generalized lessons

PRIVATE WORKSPACE
→ context, decisions, evidence, experiments, handoffs, private lessons

PRIVATE PROJECT / SOURCE OF TRUTH
→ implementation and project-specific authoritative artifacts

SECURE SECRET STORE
→ credentials, tokens, private keys and secrets
```

These are functional roles, not mandatory repository counts.

If the destination is unclear, mark it UNKNOWN and resolve it before publishing or committing.

Never put private source material into public bAIble merely because a reusable lesson may later come from it.

Before public promotion:

`PRIVATE EXPERIENCE → GENERALIZE → DE-SENSITIZE → VERIFY → REALITY CHECK → PUBLIC CANDIDATE`

---

## 6. Starter instruction for your AI

A human may give this instruction to a new AI/session:

> Use bAIble v2 as the public governance framework for our work.
>
> First orient yourself from START_HERE.md, BIBLE.md, PUBLIC_PRIVATE_BOUNDARY.md and the relevant Human/AI view. Use FIRST_RUN.md as the adoption path.
>
> Do not treat bAIble as project memory and do not copy another person's private ecosystem.
>
> Before creating infrastructure, inspect what private repositories or workspaces already exist and reuse suitable structure where possible.
>
> Before significant work:
> - identify intent, knowns, interpretation and unknowns;
> - identify role, scope and authority;
> - identify the public/private destination;
> - identify expected evidence and verification;
> - identify the next authorized action.
>
> During work:
> - do not silently guess material requirements;
> - preserve provenance;
> - do not treat records, relations or context as truth;
> - distinguish implementation, verification and acceptance;
> - use Reality Check for human/AI map alignment;
> - use Fact Check for factual/evidential claims;
> - stop, recover or escalate when required context, authority or approval is missing.
>
> When work changes hands, use HANDOFF → RECONSTRUCT → CHECK → CONTINUE.
>
> Start with one real project and add ecosystem machinery only when the real workflow demonstrates the need.

The AI should explain its understanding back to the human before substantial work begins.

That explanation is only the AI's working-map projection. It is not a completed Reality Check by itself.

The human should have a clear opportunity to confirm, correct, refine or leave an explicit unresolved difference.

If the maps differ, align them before building on the mismatch.

---

## 7. First Reality Check

Before substantial setup or work, compare:

### Human map
- What am I trying to achieve?
- What do I think bAIble will do for me?
- What already exists?
- What should remain private?
- What do I expect the AI to do autonomously?

### AI working map
- What does the AI believe the intent is?
- What does it think already exists?
- What is inferred rather than received?
- What authority does it believe it has?
- What remains unknown or conflicting?

Classify differences as:
- aligned;
- missing;
- different interpretation;
- different importance;
- different relation;
- unresolved;
- intentionally preserved.

A difference is not automatically an error.

Reality Check asks:

**Do Human and AI currently understand the same thing in the same way?**

Fact Check asks:

**Is this claim actually supported?**

Verification asks:

**Does the required result actually hold?**

Acceptance asks:

**Does the authorized human/system accept the verified result?**

Do not collapse these into one generic check.

---

## 8. Start one real project

Do not learn bAIble only as documentation.

Choose one real problem.

Create or identify a project record and capture only what is needed:

### INTENT
What outcome do we actually want?

### CONTEXT
What does the worker need to know now?

### SCOPE
What is included and excluded?

### KNOWN
What is established?

### UNKNOWN
What is not yet known?

### AUTHORITY
Who may decide or approve material actions?

### EVIDENCE
What would demonstrate success?

### NEXT STEP
What is the next small, authorized and preferably reversible action?

Then work through:

`UNDERSTAND → CLASSIFY → PLAN → ACT → VERIFY → ALIGN → LEARN → PERSIST`

or the fuller loop:

`INTENT → CONTEXT → GROUNDING → RULES → PLAN → ACTION → EVIDENCE → VERIFICATION → ACCEPTANCE → LEARN → PERSIST`

Prefer:

`EXPLAIN → CONFIRM WHEN NEEDED → DO → VERIFY → RECORD`

over large chains of hidden action.

---

## 9. Add ecosystem parts only when reality needs them

### Add UnAiversed-style mapping when

- relationships become hard to preserve;
- several perspectives matter;
- contradictions or uncertainty need to remain visible;
- flat notes no longer explain why things relate.

### Add rAIda-style coordination when

- several agents, tasks or tools genuinely need coordination;
- role/scope/gates need active enforcement;
- evidence and verification must be coordinated systematically.

### Add Watchdog-style continuity when

- a workflow has observable state;
- several authorized transitions exist;
- stopping, retrying, continuing or escalating needs explicit rules.

### Add task/process graphs when

- dependencies matter;
- several possible transitions exist;
- task existence must be separated from authority;
- queue/order alone is insufficient.

### Use WheeAIls when

- a beginner needs relevant reminders;
- the same small orientation mistakes recur;
- support can reduce repeated prompting.

WheeAIls remind. They do not decide, verify or authorize.

Do not add architecture because it exists in the ecosystem.

Add it because a real problem demonstrates the need.

---

## 10. Preserve continuity

Conversation continuity is not reliable work continuity.

When a session, agent, human or tool changes:

`HANDOFF → RECONSTRUCT → CHECK → CONTINUE`

A handoff is a claim about prior work, not proof.

Important current state should be recoverable from durable records and actual evidence.

Do not use:

`HANDOFF → BELIEVE → CONTINUE`

---

## 11. Learn without rule inflation

Do not turn one incident directly into a permanent rule.

Use:

`EXPERIENCE → OBSERVATION → CANDIDATE LESSON → TEST / REPEAT → GENERALIZE → REVIEW → INTEGRATE OR REJECT`

Repeated failure is a signal to inspect the surrounding process.

Frequency is evidence that something deserves attention, not proof of the cause.

Keep private lesson candidates private until they are generalized, de-sensitive and suitable for public reuse.

---

## 12. Core distinctions to preserve

`FOUND ≠ UNDERSTOOD ≠ VERIFIED ≠ CANONICAL`

`IMPLEMENTED ≠ VERIFIED ≠ ACCEPTED`

`CONTEXT CONTINUITY ≠ MEANING CONTINUITY`

`RECORD ≠ TRUTH`

`DECISION ≠ TRUTH`

`RELATION ≠ EVIDENCE`

`CAPABILITY ≠ AUTHORIZATION`

`AGENT AGREEMENT ≠ INDEPENDENT VERIFICATION`

These distinctions are more important than reproducing any particular repository layout.

---

## 13. Signs onboarding succeeded

The human should be able to answer:

- What is bAIble and what is it not?
- What should stay public and what should stay private?
- Where does my durable project context live?
- Where is implementation/source of truth?
- What is the current intent?
- What is known versus inferred or unknown?
- Who has authority to make the next material decision?
- What counts as evidence?
- What is Reality Check for?
- What is Fact Check for?
- What does Verification establish?
- How would another agent reconstruct the work?
- When should I add UnAiversed, rAIda or Watchdog?
- What should happen when we discover a reusable lesson?

The AI should be able to answer the same questions without pretending private data is public, capability is authority, or documentation is truth.

---

## 14. Graduation

A beginner does not graduate by memorizing bAIble.

They graduate when they can work safely without constant support wheels:

`GOAL → BOUNDED WORK → EVIDENCE → VERIFY → ALIGN → PRESERVE → CONTINUE`

An experienced user may skip beginner explanations, but not the underlying boundaries.

The smallest useful adoption is:

```text
PUBLIC
bAIble v2

PRIVATE
an appropriate workspace
  ├── current state
  ├── real project(s)
  ├── evidence
  ├── handoffs
  └── lessons / contextual records as needed
```

Choose one real project.

Do one bounded piece of useful work.

Verify it.

Then let the ecosystem grow only where reality demonstrates the need.
