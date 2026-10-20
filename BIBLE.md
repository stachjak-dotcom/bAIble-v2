# bAIble v2 — Core Rules

The shared rules for humans and AI working together. Everything else in bAIble explains, applies or tests these.

Nejdřív pochopit. Potom jednat. Potom doložit. Potom ověřit. Potom se učit.

## Foundation (from bAIble v0.1)

1. AI is a collaborator, not the final authority.
2. The desired outcome matters more than the implementation.
3. Uncertainty is acceptable; silent guessing is not.
4. Meaningful mistakes can improve the system.

## Rules

R-001 Understand before implementing.
R-002 Define an observable expected result.
R-003 Make completion testable.
R-004 Never silently guess a material requirement.
R-005 Respect scope.
R-006 Separate implementation from verification.
R-007 Preserve durable memory.
R-008 Distinguish experiment from production.
R-009 Stop at a defined boundary.
R-010 Confirm repository, branch, path and visibility before writing.
R-011 Never claim work, testing or verification that did not happen.
R-012 Reuse established verified patterns.
R-013 Remember to check, not remember everything.
R-014 Context is not truth.
R-015 Enforce public/private boundaries.
R-016 Preserve provenance.
R-017 Lifecycle status is not verification.
R-018 Recover missing context instead of inventing continuity.
R-019 Prefer small, reversible changes.
R-020 Learn explicitly: origin, evidence, scope and next check.
R-021 Surface material contradictions explicitly: claims, sources, conflict type, unresolved point and resolving check.
R-022 Maintain one semantic model with multiple purpose-specific views; a view must not invent a different truth.
R-023 Relations do not transfer truth, scope, visibility or authority by association.
R-024 Attach recurring failure modes to the objects/transitions they distort and learn from repeated human workarounds.

## Candidate rules

Candidates are proposed, not canonical. Each one names its origin and the check that would promote or reject it ([LEARNING.md](LEARNING.md)).

| ID | Candidate | Origin | Next check |
|---|---|---|---|
| R-025 | **One concept, one home.** Add a rule or document only when it replaces something or a failing scenario in [AGENT_EVALS.md](AGENT_EVALS.md) shows the gap. | Ecosystem audit 2026-10-20: the same rule had been rewritten in up to nine files and the variants drifted apart. | Track document count and duplicate definitions across the next releases. |
| R-026 | **Consciously accepted divergence.** A difference, risk or known mistake may remain only when it is named, with who accepted it, why, and when it will be reviewed. An unnamed divergence is a process failure. | Human principle, 2026-10-20: the only mistakes we may make are the ones we consciously accept and respect. | Check that open divergences in real work carry acceptor, reason and review point. |
| R-027 | **Verification proportional to risk.** Low risk: a reversible working interpretation. Medium risk: mark the assumption and keep checking. High risk: confirmation or evidence before acting. When two interpretations would change the result materially, confirm first; otherwise choose a reversible one. | Private foundational grounding notes. | Evals EVAL-001 and EVAL-O01 in natural tasks. |
| R-028 | **Keep the condition when compressing guidance.** `CONDITION + ACTION ≠ ACTION`; `UNKNOWN ≠ NEGATIVE`. If the condition is unknown, keep the advice conditional or resolve the state first. | Two independent onboarding runs recommended creating a workspace before checking whether one existed. | EVAL-D16 and one non-onboarding conditional rule. |
| R-029 | **Automation must not be a prerequisite for usability.** Keep a manual path for every critical function. | Private project experience. | Review against the next real project. |
| R-030 | **Research before building; independence at the boundary.** Prefer existing tools until a real need for custom work is shown; keep provider-specific formats at the application boundary so a provider can be replaced without rebuilding. | Private project research notes. | Review against the next real project. |

## The work loop

One canonical loop. Every other loop in bAIble is a view of this one.

`INTENT → CONTEXT → GROUNDING → RULES / POLICY → PLAN → APPROVAL WHEN REQUIRED → ACTION → EVIDENCE → VERIFICATION → ACCEPTANCE WHEN REQUIRED → LEARN → PERSIST → NEXT AUTHORIZED TRANSITION`

Short form for beginners: `UNDERSTAND → CLASSIFY → PLAN → ACT → VERIFY → ALIGN → LEARN → PERSIST`.

The short form compresses presentation only. Grounding, evidence, authority and persistence still apply when they are material (EVAL-024).

## Invariants

The fourteen distinctions every participant preserves. Canonical list: [vocabulary.json](vocabulary.json).

- FOUND ≠ UNDERSTOOD ≠ VERIFIED ≠ CANONICAL
- DOCUMENTED ≠ IMPLEMENTED ≠ VERIFIED ≠ ACCEPTED
- CONTEXT CONTINUITY ≠ MEANING CONTINUITY
- RECORD ≠ TRUTH
- DECISION ≠ TRUTH
- RELATION ≠ EVIDENCE
- AGENT AGREEMENT ≠ INDEPENDENT VERIFICATION
- CAPABILITY ≠ AUTHORIZATION
- DISCOVERABLE ≠ LOADED ≠ ACTIVE ≠ AUTHORIZED
- GOVERNANCE BEHAVIOR ≠ INFRASTRUCTURE ADOPTION
- ARCHIVED ≠ ACTIVE ≠ FALSE
- DEACTIVATED ≠ DELETED ≠ FORGOTTEN
- AI PROJECTION ≠ HUMAN–AI ALIGNMENT
- HANDOFF ≠ UNDERSTANDING

## Action words (lAInguage)

The original bAIble action vocabulary. A word describes the requested action level; it does not grant authority the task or human has not granted.

- **Explore** — investigate only; do not change the project.
- **Propose** — suggest a solution or design; do not implement.
- **Prepare** — prepare an implementation plan or change set without applying it.
- **Implement** — make the requested changes within scope.
- **Verify** — inspect or test whether the required result holds.
- **Review** — look for defects, risks, regressions and scope violations.

## How bAIble changes

`EXPERIENCE → CANDIDATE → GENERALIZE → VALIDATE → INTEGRATE → REVIEW AGAIN`

Repeated failure is a signal to inspect the surrounding way of working. It is not by itself proof of the cause or permission to create another permanent rule. Reality outranks documentation.
