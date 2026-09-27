# WheeAIls — Relevance and Support

WheeAIls are support wheels for humans and AI entering or navigating a complex working environment.

Their job is to surface the **right reminder at the right moment**, not to become a second memory database or authority layer.

## Purpose

- help a beginner orient,
- surface relevant bAIble rules and context,
- remind before common mistakes,
- reduce repeated human prompting,
- point toward the next useful check.

## Boundary

WheeAIls do not:

- decide,
- verify,
- authorize,
- expand scope,
- mutate task state,
- replace Reality Check,
- replace Fact Check,
- replace rAIda,
- replace the human.

## Design principle

If reliable work requires the same manual reminder repeatedly, that repetition is a signal to inspect the surrounding process.

The goal of support wheels is not permanent dependency.

`REMINDER → BETTER ORIENTATION → LEARNING → LESS MANUAL COMPENSATION`

WheeAIls should therefore optimize relevance, not volume.


## Adaptive relevance

WheeAIls should be selected from the current situation, not from a fixed checklist.

Useful signals may include:
- the same mistake or omission recurring;
- a concept being new to the user;
- a known failure mode becoming relevant;
- a public/private, authority, scope, evidence or verification boundary approaching;
- the user repeatedly supplying the same manual reminder;
- the user clearly no longer needing a reminder.

A reminder should answer:

- **Why now?**
- **What risk or friction does it address?**
- **What is the smallest useful reminder?**

Do not surface every potentially relevant rule.

Prefer:

`SIGNAL → ONE RELEVANT REMINDER → ACTION / CHECK → OBSERVE`

over:

`CONTEXT → MANY REMINDERS → COGNITIVE LOAD`

## Growth boundary

WheeAIls may suggest that a stronger mechanism could help, but they do not activate it.

Examples:
- repeated context loss may justify offering durable WORK_STATE;
- complex relationships may justify offering UnAiversed-style mapping;
- coordination friction may justify offering rAIda-style coordination;
- observable multi-step continuity may justify offering Watchdog-style monitoring.

The user or appropriate authority decides whether to adopt the added mechanism.

Support should be removable. If a reminder no longer improves work, stop surfacing it.
