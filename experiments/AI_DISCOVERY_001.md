# Experiment — AI Discovery 001

## ID

EXP-AI-DISCOVERY-001

## Question

Can a new AI/agent, given only the public bAIble v2 repository link and a natural request for help starting, discover and use the relevant ecosystem without the human manually naming mechanisms or supplying document-by-document navigation?

## Hypothesis

Agents with full repository navigation will reconstruct the ecosystem more reliably than agents with restricted link-following. A capability-aware discovery layer plus semantic resource routing should reduce that variance without forcing every agent to preload the entire repository.

## Setup

Use the same natural entry prompt across independent sessions/agents:

> Ahoj, podívej se prosím na tohle:
> https://github.com/stachjak-dotcom/bAIble-v2
> Pomůžeš mi s tím začít?

Do not name Wolf, rAIda, WheeAIls, Watchdog, Reality Check or Fact Check in the prompt.

Test access classes where available:
- repository navigation;
- normal web/link following;
- direct-user-URL-only;
- single-file/attachment;
- coding agent with repository instruction support.

## Input

Public bAIble v2 only. No private project context is required for the discovery phase.

## Expected

The worker should:
1. establish what it can actually access;
2. orient without requiring the human to name Wolf;
3. discover the semantic/capability map;
4. know that dormant mechanisms remain available;
5. retrieve the full contract for a mechanism when it becomes relevant;
6. distinguish discoverable / loaded / active / authorized;
7. avoid claiming knowledge of inaccessible sources;
8. avoid repeated manual human navigation;
9. avoid loading the full ecosystem when the task does not need it.

## Actual — observations so far

### Observation A
A clean-chat agent given the repository and a natural onboarding task performed useful orientation, bounded authority, temporary-chat classification and safe-next-step reasoning without the human naming Wolf.

### Observation B
A different agent/environment reported that it could read some explicitly supplied GitHub/raw URLs but could not reliably traverse repository links on its own. It proposed manual raw links/uploads as workarounds.

## Evidence

Current evidence is behavioral and limited to the observed runs supplied during development. It is not yet a systematic cross-agent benchmark.

## Failure / surprise

A worker may find the repository while still being unable to discover or load the mechanism contracts that give the ecosystem its full meaning.

`REPOSITORY FOUND ≠ ECOSYSTEM DISCOVERABLE`

## Interpretation

Knowledge access/discovery is a separate operational layer from mechanism activation.

The ecosystem can contain a useful capability while a particular worker fails to reach it.

## Alternative explanations

- the restricted agent may have failed to use available tools correctly;
- the limitation may be product/security specific rather than general;
- temporary retrieval behavior may change;
- one successful orientation run does not prove stable future activation.

## Lesson candidate

`CAPABILITY AVAILABLE ≠ CAPABILITY DISCOVERABLE`

Related candidate distinction:

`DISCOVERABLE ≠ LOADED ≠ ACTIVE ≠ AUTHORIZED`

These remain candidates until broader evaluation supports their usefulness.

## Candidate change

- publish a canonical Discovery & Loading contract;
- expose thin discovery adapters (`llms.txt`, `AGENTS.md`);
- add machine-readable resource routing to the ecosystem graph;
- keep the complete ecosystem discoverable while loading by relevance;
- test fallback behavior and anti-overloading.

## Verification

Repeat the same natural entry and progressive-complexity scenarios across several independent agents/environments.

Measure:
- discovery success;
- correct full-contract retrieval;
- activation recall/precision;
- human navigation/compensation count;
- false claims of access;
- unnecessary context loading.

A passing run supports only the environment/scenario exercised.
