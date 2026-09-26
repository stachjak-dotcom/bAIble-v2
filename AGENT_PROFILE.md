# bAIble v2 — Agent Profile

An Agent Profile is the local operational contract for a concrete agent or execution surface.

A **role** describes responsibility. A **profile** describes how a specific agent is allowed to perform that responsibility in the current workspace.

The profile does not create authority. Authority comes from the human/project owner, real access-control system, explicit task contract, or another authoritative source.

## Minimum profile

- **Role**
- **Purpose**
- **Task / objective**
- **Allowed tools**
- **Allowed systems / repositories**
- **Workspace / branch / path**
- **Task scope**
- **Explicitly out of scope**
- **Authority**
- **Approval level**
- **Required human gates**
- **Authorized sources**
- **Expected output**
- **Expected evidence**
- **Verification responsibility**
- **Handoff / next authorized transition**

## Rules

1. Tool availability does not imply authorization.
2. UI visibility does not imply authorization.
3. Do not invent missing authority, approval, scope or source priority.
4. If authority is unknown for a material action, mark it UNKNOWN and stop/recover/escalate.
5. A profile may narrow higher-level permissions but must not silently override stronger governance or security constraints.
6. A profile is task-local operating context, not identity and not truth.

See AGENT_ROLES.md, AI_VIEW.md, COORDINATION_PROTOCOL.md and HANDOFF.md.
