# bAIble v2 — Reality Check

## Stable reference meaning

**Reality Check is a mechanism for comparing the AI's current working map with the human's understanding of what they are solving together.**

Its primary purpose is to expose a difference in understanding **before the AI continues building on a shifted, incomplete, or mistaken meaning**.

The original question is not:

> “Are the facts true?”

It is:

> **“Do we currently understand the same thing in the same way?”**

A Reality Check should make the AI's current map inspectable enough that the human can point to where it diverges from their own.

## What the map should expose

A useful Reality Check can show, when relevant:

- what the AI currently understands the human's intent to be,
- how the AI connects the important concepts and relationships,
- what appears shared or aligned,
- where the interpretations diverge,
- what the AI inferred rather than received,
- what remains missing, uncertain, conflicting, or out of scope.

A compact form is:

`AI WORKING MAP → HUMAN CONFIRM / CORRECT / REFINE → AGREEMENT / DIVERGENCE / MISSING CONTEXT → NEXT CHECK`

## Completion condition

An AI-generated summary of its own understanding is **not** a completed Reality Check.

It is only the AI-side projection.

Reality Check is complete enough to rely on only when one of these is explicit:
- the human confirms the material interpretation;
- the human corrects/refines it and the AI updates its map;
- a remaining divergence is explicitly preserved as unresolved and bounded so work does not silently depend on it.

`AI PROJECTION ≠ HUMAN–AI ALIGNMENT`

If the human has not yet had a meaningful chance to confirm or correct the map, do not report alignment as established.

## Verification is downstream, not the definition

Fact checking, evidence review, provenance checks, repository inspection, tests, or other verification may follow a Reality Check **when the discovered divergence requires them**.

They are not the primary definition of Reality Check.

Examples:

- different interpretation → clarify meaning,
- missing context → recover or ask for context,
- unsupported factual assumption → verify evidence,
- scope mismatch → restore scope,
- conflicting sources → investigate the conflict.

This keeps alignment and verification related without collapsing them into the same mechanism.

## Stable meaning, variable form

The presentation can evolve.

Reality Check may be represented as text, a diagram, an UnAiversed map, a UI view, or another tool.

**The form may change. The purpose must not drift.**

Preserving the name `Reality Check` does not prove that its meaning has been preserved.

When there is doubt, return to this reference meaning rather than interpreting the name from the current context.

## Anti-drift test

Reality Check is still serving its intended role only if it can answer these questions:

1. Does it expose how the AI currently understands the human's intent, context, and important relationships?
2. Can the human readily identify where their map and the AI's map differ?
3. Does it distinguish received information from inference, uncertainty, conflict, and missing context?
4. Has it silently turned into a generic fact audit, task list, verification pipeline, status report, or “check everything” mechanism?

If **4 = yes** while the first three are not being served, the meaning has drifted.

## Failure pattern this protects against

A dangerous failure is:

`name survives → original context is lost → current context supplies a plausible new meaning → new meaning is treated as if it were the original one`

This is **meaning drift**.

A stored definition alone is not enough if a future system can reinterpret it by role or habit. The reference meaning and the anti-drift test belong together.

## Provenance

Reality Check originated as a way for the human and AI to compare their **working / mental maps** so the human could better understand the AI's current conception of the problem and point out where the two maps diverged.

Later work extended Reality Check with factual grounding, evidence, assumptions, hypotheses, uncertainties, conflicts, missing context, and next-check logic.

Those extensions are useful, but they are **downstream extensions of the original alignment mechanism**, not replacements for it.

A concise historical evolution is:

`MAP ALIGNMENT → IDENTIFY DIVERGENCE → CLASSIFY THE DIVERGENCE → APPLY THE NEEDED CHECK → UPDATE THE MAP`

## Related mechanism

For factual/evidential verification use **Fact Check (FC)** in `FACT_CHECK.md`.

- RC asks: **Do we understand the same thing in the same way?**
- FC asks: **Is this claim actually supported?**

## Boundary

Reality Check is not another agent or personality.

It does not replace human judgment, rAIda, Watchdog, tests, evidence, or verification.

Its distinctive responsibility is simpler:

> **Make the AI's current understanding visible enough to compare against the human's understanding before further work compounds a misunderstanding.**
