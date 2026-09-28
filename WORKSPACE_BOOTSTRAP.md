# bAIble v2 — Conditional Workspace Bootstrap

This contract is **not a universal onboarding step**.

Load or apply it only after the start-state checkpoint establishes:

`WORKSPACE = DOES_NOT_EXIST`

and durable project state is actually needed.

If WORKSPACE is `UNKNOWN`, return to discovery/start-state classification.  
If a suitable workspace `EXISTS`, inspect and reuse it before creating anything new.

## Entry condition

All of the following should hold:

- a real project/task has been identified;
- durable context is useful or required;
- no suitable existing private workspace is available;
- the public/private boundary is understood enough for setup;
- the human has authority to create or choose the destination.

`UNKNOWN → ASK / CHECK`

`EXISTS → INSPECT / REUSE`

`DOES_NOT_EXIST + DURABLE NEED → BOOTSTRAP CANDIDATE`

## Smallest useful bootstrap

When the entry condition holds, one private repository/workspace is usually sufficient to begin.

A practical example name is:

`my-private-workspace`

A small starter shape may be:

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

This is a starter shape, not a law. Do not create empty directories or mechanisms merely because they appear here.

## README should explain

- what the private workspace is for;
- that public governance comes from bAIble v2;
- that project-specific context/evidence/implementation remains private;
- who or what has authority to change it.

## CURRENT should answer

- What are we trying to achieve?
- What project/task is active?
- What is the last verified state?
- What is uncertain or blocked?
- What evidence matters now?
- What is the exact next authorized action?

Keep CURRENT short. It is a recovery checkpoint, not truth by itself.

## Growth rule

Do not reproduce another user's private ecosystem.

Start with the smallest workspace that solves the demonstrated continuity/privacy need. Split repositories or add durable rAIda/Watchdog/graph infrastructure only when scale, security, access boundaries or workflow complexity justify it.

## Verification

After bootstrap, verify:
- the destination exists;
- visibility is correct;
- the human/agent authority is correct;
- CURRENT/README express the intended role;
- no private material was written to public bAIble;
- the next authorized project step is explicit.

`BOOTSTRAPPED ≠ PROJECT VERIFIED`
