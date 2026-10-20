# bAIble v2 — Public / Private Boundary and Security

A hard publication boundary. A boundary failure blocks publication until it is resolved.

## Public material

Reusable principles, generic workflows, abstract architecture, terminology, generalized lessons, templates, synthetic examples and public references.

## Never publish

Passwords, API keys, tokens, private keys, cookies, personal identifiers, private conversations or exports, private repository contents, customer or confidential data, proprietary implementation details, internal access paths, private run evidence and run identifiers, names of private projects, hidden context, sensitive experiments, or secrets in logs.

## Before publishing

1. remove identifying details;
2. remove secrets and access paths;
3. remove unnecessary project-specific implementation detail;
4. rewrite the lesson so it stands alone;
5. check that a public reader understands it without the private source;
6. keep uncertainty and limitations;
7. do a final privacy review: Is this private or personal? Does it reveal an access path? Does it depend on hidden context? Is the specificity necessary? Can the public claim stand without exposing private evidence?

If a claim depends on inaccessible private evidence, keep it private or present it clearly as a generalized lesson; never pretend the evidence is public. Public bAIble is not a backup of the private runtime. `scripts/validate_discovery.py` checks the repository for private run identifiers and listed private project names.

## Access discipline

Least privilege. Prefer read-only inspection when writing is unnecessary. Keep credentials outside source control. Separate environments where practical. Require explicit approval for destructive, irreversible or high-impact actions.

Security is enforced by the real access layer. UI visibility is not authorization.
