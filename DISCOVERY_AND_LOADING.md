# bAIble v2 — Discovery & Loading

This contract defines how an AI/agent discovers, loads and applies the public bAIble ecosystem without reducing the ecosystem to a fixed prompt or assuming capabilities its environment does not have.

## Core distinction

`DISCOVERABLE ≠ LOADED ≠ ACTIVE ≠ AUTHORIZED`

- **DISCOVERABLE** — the mechanism/source is known to exist and can be located.
- **LOADED** — its current contract/content has actually been retrieved or supplied.
- **ACTIVE** — its behavior is relevant to the current situation.
- **AUTHORIZED** — the current worker may perform the resulting action within scope and gates.

A mechanism may be discoverable and understood while remaining dormant.
A mechanism may become active without creating new infrastructure.
Knowing or loading a mechanism never grants authority.

## Purpose

The public ecosystem should expose its full reusable capability map to capable agents while loading only what is relevant now.

Use:

`DISCOVER FULL CAPABILITY MAP → CLASSIFY ACCESS → LOAD MINIMUM ORIENTATION → ROUTE BY RELEVANCE → LOAD FULL CONTRACTS → APPLY WITHIN AUTHORITY`

Avoid both failure modes:

`LOAD EVERYTHING BY DEFAULT → CONTEXT INFLATION`

and:

`PRESELECT A SMALL SUBSET → HIDDEN CAPABILITY`

Relevance controls loading priority and activation. It must not erase discoverability.

## 1. Classify access capability

Before claiming that bAIble has been inspected, determine what the current environment can actually access.

Useful classes:

### REPOSITORY_NAVIGATION
The worker can enumerate repository contents, search files and fetch current source files.

Preferred path:
- inspect the repository;
- read the canonical semantic map and machine graph;
- retrieve mechanism contracts as they become relevant.

### LINK_FOLLOWING
The worker can open the repository/entry documents and follow explicit links.

Preferred path:
- use `START_HERE.md`, `llms.txt` and linked canonical documents;
- use the semantic map where supported.

### DIRECT_URL_ONLY
The worker can retrieve only URLs directly supplied or explicitly allowed by the environment.

Preferred path:
- state the limitation;
- use absolute URLs exposed by `llms.txt` or the current entry surface when accessible;
- request the smallest missing bootstrap reference from the human only when the environment genuinely cannot discover it itself.

Do not make the human repeatedly copy individual documents as a substitute for a broken discovery process.

### SINGLE_FILE_OR_ATTACHMENT
The worker can reliably ingest an attached/exported text artifact but cannot navigate the repository.

Preferred path:
- use an explicitly generated, revision-bound context bundle if one exists;
- preserve the source revision and source-file list;
- do not treat the bundle as a second canonical truth.

### NO_EXTERNAL_ACCESS
The worker cannot retrieve repository content.

State that boundary explicitly. Do not pretend to have inspected bAIble.
Work only from content actually supplied in the interaction.

## 2. Minimum orientation

For substantial work, a capable agent should be able to discover at least:

- `SYSTEM_MAP.md` — canonical ecosystem semantic model;
- `AI_VIEW.md` — operational AI navigation;
- `BIBLE.md` — core governance;
- `PUBLIC_PRIVATE_BOUNDARY.md` — publication/privacy boundary;
- `ECOSYSTEM_GRAPH.json` — machine-readable capability/relationship seed;
- `FIRST_RUN.md` — adoption path when a human+AI pair is new to the ecosystem.

`START_HERE.md` and this document route access; they do not replace the canonical contracts above.

## 3. Use the graph as a retrieval map

`ECOSYSTEM_GRAPH.json` is not only a visualization seed. Its resource metadata should let a capable worker move from:

`CURRENT NEED → RELEVANT NODE / RELATION → CANONICAL RESOURCE → LOAD → CHECK`

Examples:

- orientation uncertainty → Wolf → `WOLF_ONBOARDING.md`;
- human/AI meaning divergence → Reality Check → `REALITY_CHECK.md`;
- material factual/evidential claim → Fact Check → `FACT_CHECK.md`;
- coordination complexity → rAIda → `RUNTIME_AND_WATCHDOG.md` + `COORDINATION_PROTOCOL.md`;
- recurring human compensation → WheeAIls + Failure Modes → `WHEEAILS.md` + `FAILURE_MODES.md`;
- relationship/context complexity → UnAiversed view → `ECOSYSTEM_MAP.md` + `RELATIONSHIP_MODEL.md` + `CONTEXT_ITEM.md`;
- continuity/handoff → `WORK_CONTINUITY.md` + `HANDOFF.md`;
- completion claim → `VERIFICATION.md`.

Do not infer the full contract from a node label alone.

`FOUND MECHANISM ≠ UNDERSTOOD MECHANISM`

## 4. Contract loading

When a mechanism becomes materially relevant:

1. locate its canonical resource;
2. load the current source where the environment allows;
3. record or retain enough source/revision identity to detect staleness;
4. distinguish what was actually loaded from what is merely known to exist;
5. apply the smallest sufficient behavior;
6. check scope/authority before consequential action.

If a referenced source is unavailable, mark the contract as not loaded or stale rather than filling it from plausibility.

## 5. Adapters are not canonical truth

The repository may expose multiple discovery adapters, for example:

- `README.md` — human/browser entry;
- `llms.txt` — LLM-friendly absolute-link index;
- `AGENTS.md` — agent-instruction entry for environments that support it;
- future generated single-file bundles.

These adapters exist to make canonical sources reachable.

They must not silently redefine:
- mechanism meaning,
- scope,
- authority,
- verification state,
- public/private boundaries.

`ADAPTER → LOCATE CANONICAL SOURCE`

not:

`ADAPTER → BECOME SECOND BIBLE`

## 6. Behavior versus infrastructure

Discovery may reveal that a mechanism is relevant.

That permits the smallest existing governance behavior within current authority; it does not automatically authorize infrastructure adoption.

Examples:

- load and apply rAIda coordination behavior without creating a runtime;
- use Wolf orientation without creating a Wolf service;
- use Watchdog-style continuity classification without autonomous monitoring;
- use UnAiversed-style relationship reasoning without creating a permanent graph.

Durable repositories, schedulers, autonomous continuation, persistent agents or other machinery remain separate architectural choices.

## 7. Progressive discovery

A worker should not need to preload every file.

Start with orientation and the semantic map, then traverse as work changes.

A useful loop is:

`ORIENT → DISCOVER → LOAD RELEVANT CONTRACT → WORK → OBSERVE NEW TRIGGER → DISCOVER / LOAD MORE`

This allows a simple task to remain simple while preserving access to the full ecosystem for capable agents.

## 8. Provenance and version integrity

For material use, retain enough information to answer:

- which repository/source was used;
- which path/document was loaded;
- which revision/time was relevant when known;
- whether content was direct source or an adapter/bundle;
- what could not be retrieved;
- what may now be stale.

A generated bundle must identify its source revision and should be regenerated from canonical sources rather than edited as an independent copy.

## 9. Failure handling

### Broken reference
Report the missing/broken resource and use an alternate published adapter/path if available.

### Partial repository access
Bound the claim:
- “I can read these documents”
not
- “I have inspected the full repository.”

### Retrieval limitation
Do not convert a tool limitation into a claim that the mechanism is absent.

### Human compensation
If reliable onboarding repeatedly requires the human to paste the same links or remind the agent what exists, treat the recurrence as a process/discovery failure candidate.

### Context inflation
Do not respond to discovery problems by loading the entire ecosystem on every task.

## 10. Public/private boundary

Public discovery may expose public contracts and public repository structure.

It must not expose or require:
- private FederAItion contents,
- private UnAiversed project state,
- credentials,
- private run evidence,
- hidden conversations,
- project-specific confidential data.

Knowing that a private domain exists is not access to it.

## 11. Verification

Successful discovery means more than opening a repository URL.

For the relevant scope, verify that the worker can:
- locate the capability map;
- find the canonical contract for an applicable mechanism;
- distinguish loaded from merely discoverable content;
- keep dormant mechanisms discoverable;
- avoid treating loading as authorization;
- use fallback access without repeated human navigation;
- avoid unnecessary full-context loading.

See `AGENT_EVALS.md` and `experiments/AI_DISCOVERY_001.md`.

## Design principle

**Expose the whole ecosystem; activate and load by relevance; act only within authority.**
