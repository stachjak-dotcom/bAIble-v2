# bAIble v2 — First Run

This is the practical onboarding path for a new human + AI pair.

The goal is not to copy somebody else's private ecosystem.

The goal is to use the public bAIble as shared governance, then create **your own private working environment** for your own projects, context, evidence and experiments.

---

## 1. Understand the three layers

### bAIble
Public, reusable governance.

Use it for:
- rules;
- terminology;
- roles;
- verification;
- Reality Check;
- Fact Check;
- handoffs;
- public/private boundaries;
- reusable lessons.

Do **not** use public bAIble as your private project memory.

### FederAItion
A private execution / coordination environment.

Your equivalent may contain:
- projects;
- task/process state;
- agent coordination;
- evidence;
- experiments;
- private lessons;
- approvals;
- runtime tools;
- rAIda / Watchdog implementations.

You do not need to copy another person's private FederAItion repository.

Start with your own private workspace and add runtime machinery only when your work needs it.

### UnAiversed
A contextual relationship layer.

Use it to preserve:
- important entities;
- relationships;
- perspectives;
- uncertainties;
- contradictions;
- decisions;
- evidence references;
- project context.

UnAiversed is not a truth database and not a transcript archive.

It is a map of meaning and relations.

---

## 2. Recommended first setup

Start simple.

You need:

1. access to the public `bAIble-v2` repository;
2. one **private repository** for your own work.

A practical starting name might be:

`my-private-workspace`

You may later split it into separate repositories when real scale or security boundaries require it.

### Recommended private repository structure

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

This is a starter structure, not a law.

Add only what your real work needs.

---

## 3. What belongs where

### Public bAIble

Put here only material that is safe and useful for other people:

- reusable principles;
- generic workflows;
- generalized lessons;
- terminology;
- public examples;
- public templates.

### Your private workspace

Keep here:

- private project details;
- customer/company information;
- personal information;
- credentials and access paths;
- private experiments;
- internal evidence;
- unpublished ideas;
- private agent logs;
- project-specific implementation;
- sensitive context.

Before moving anything from private to public:

`PRIVATE EXPERIENCE → GENERALIZE → DE-SENSITIZE → VERIFY → REALITY CHECK → PUBLIC CANDIDATE`

Never publish private source material merely because the lesson may eventually be public.

---

## 4. Create your first private repository

On GitHub:

1. Create a new repository.
2. Set visibility to **Private**.
3. Give it a name meaningful to you.
4. Add a README.
5. Do not add credentials, tokens or secrets to the repository.
6. Create the starter folders only when you need them.

A first `README.md` may say:

> This is my private working environment for projects that use bAIble v2 governance.
>
> Public reusable governance comes from bAIble v2.
> Private project context, execution evidence, experiments and lessons remain here.

A first `CURRENT.md` should answer:

- What am I currently trying to achieve?
- What project am I working on?
- What is verified?
- What is still uncertain?
- What is the next authorized step?

Keep CURRENT short.

It is a checkpoint, not a diary.

---

## 5. Connect your AI to bAIble

Give your AI access to the public bAIble repository or its contents.

Then use this starter instruction:

> Use bAIble v2 as the public governance framework for our work.
>
> First orient yourself using START_HERE.md, BIBLE.md, PUBLIC_PRIVATE_BOUNDARY.md and the relevant Human/AI view.
>
> Do not treat bAIble as project memory.
>
> Our private repository is our working environment for project context, evidence, experiments, private lessons and implementation.
>
> Before significant work:
> - identify intent;
> - identify role and scope;
> - identify what is known, assumed and unknown;
> - check the public/private boundary;
> - identify what evidence and verification are required.
>
> During work:
> - do not silently guess;
> - do not treat records or context as truth;
> - preserve provenance;
> - distinguish implementation from verification and acceptance;
> - use Fact Check for factual/evidential questions;
> - use Reality Check when our working maps or interpretations may differ;
> - stop or ask for authority before crossing scope or making a material irreversible decision.
>
> When work ends or changes hands, create a reconstructable handoff rather than relying on chat memory.
>
> Start small. Use only the ecosystem mechanisms the real task actually needs.

The AI should then explain the system back to you in its own words before substantial work begins.

If that explanation does not match your understanding, run a Reality Check before continuing.

---

## 6. Your first project

Do not start by building rAIda, Watchdog, a complex task graph or a large semantic graph.

Start with one real problem.

Create:

`projects/my-first-project/`

Record only:

### INTENT
What outcome do you actually want?

### CONTEXT
What does the worker need to know?

### SCOPE
What is included and excluded?

### UNKNOWN
What is not yet known?

### EVIDENCE
What would demonstrate that the work succeeded?

### NEXT STEP
What is the next small authorized action?

Then work through:

`UNDERSTAND → CLASSIFY → PLAN → ACT → VERIFY → ALIGN → LEARN → PERSIST`

or the fuller living loop:

`INTENT → CONTEXT → GROUNDING → RULES → PLAN → ACTION → EVIDENCE → VERIFICATION → ACCEPTANCE → LEARN → PERSIST`

---

## 7. Add ecosystem parts only when needed

### Add UnAiversed-style mapping when:

- relationships become hard to remember;
- multiple perspectives matter;
- contradictions or uncertainty need to remain visible;
- several projects/decisions/evidence items are connected.

### Add rAIda-style coordination when:

- several agents/tasks/tools need coordination;
- scope and gates need active enforcement;
- evidence and verification must be checked systematically.

### Add Watchdog-style continuity when:

- a workflow has several authorized steps;
- the process must safely continue after one task ends;
- stopping, retrying or escalating needs explicit rules.

### Add task graphs when:

- dependencies matter;
- several next steps exist;
- task existence must be separated from authority;
- queue/order alone is no longer enough.

Do not add architecture because it exists in the ecosystem.

Add it because the real workflow demonstrates the need.

---

## 8. First Reality Check

After your first useful piece of work, compare:

### Human map
What do you think the project/system currently means?

### AI map
What does the AI think it means?

Mark differences as:

- aligned;
- missing;
- different importance;
- different relation;
- unresolved;
- intentionally preserved.

A difference is not automatically an error.

Sometimes it exposes a useful perspective.

---

## 9. First lesson

Do not turn one incident directly into a permanent rule.

Use:

`EXPERIENCE → OBSERVATION → CANDIDATE LESSON → TEST / REPEAT → GENERALIZE → REVIEW → INTEGRATE OR REJECT`

Keep private candidates in your private workspace.

Only generalized, de-sensitive, reusable material should become a public candidate.

---

## 10. Minimum safe operating model

A new user does **not** need the entire mature private runtime on day one.

A useful minimum is:

```text
PUBLIC
bAIble v2

PRIVATE
your repository
  ├── CURRENT
  ├── projects
  ├── evidence
  ├── experiments
  ├── lesson candidates
  └── contextual / UnAiversed notes
```

That is enough to start using the ecosystem correctly.

The rest may evolve from real needs.

---

## 11. Signs that onboarding succeeded

You should be able to answer:

- What is bAIble?
- What should stay private?
- Where does my project context live?
- What is the current intent?
- What counts as evidence?
- Who has authority to make the next decision?
- What is Fact Check for?
- What is Reality Check for?
- How would another agent reconstruct the work?
- What should happen if we discover a reusable lesson?

Your AI should be able to answer the same questions without pretending private data is public or treating documentation as truth.

---

## 12. Next step

Choose one real project.

Do one bounded piece of useful work.

Verify it.

Then let the ecosystem grow only where reality demonstrates the need.
