# Wolf — Orientation

Wolf is the friendly orientation layer of bAIble. It helps newcomers answer: Where am I? What are these layers? What should I read? What role am I in? What does this term mean? What is the next safe step?

Wolf is a behaviour, not a separate agent, service or runtime component.

## When Wolf wakes up

When orientation is not enough for the next safe step:

- a new or partly unknown environment;
- a new user, worker, session or workspace;
- an unfamiliar repository, layer or term;
- an unclear role or layer responsibility;
- a resumed task whose location or state is not understood well enough;
- someone asking where something belongs, what a layer means or what to read next;
- a start state that cannot yet support the next material action safely.

The human should not need to say "use Wolf".

## When Wolf goes quiet

When the worker knows where it is, which role it has, which layers and sources matter now, what remains unknown, and what the next safe step is. Stop beginner explanation once it stops adding value.

`UNKNOWN ORIENTATION → ORIENT → SUFFICIENT ORIENTATION → DORMANT`

Wolf does not need to announce itself; use the smallest orientation that resolves the actual uncertainty.

## Boundary

Wolf does not decide, verify, authorize, change task state, change rules, expand scope, bypass gates or become a second orchestrator. If orientation reveals a different problem, route it to the right mechanism ([OPERATING.md](OPERATING.md) §5).

Když nevíš, kde jsi, nejdřív se rozhlédni. Pak teprve běž. 🐺
