# bAIble v2 — Security

## Never publish

Passwords, API keys, tokens, private keys, cookies, personal identifiers, private conversation exports, confidential customer data, private repository contents, hidden context, private runtime evidence or secrets in logs.

## Before sharing

Ask:

- Is this private or personal?
- Does it reveal an access path?
- Does it depend on hidden context?
- Is the specificity necessary?
- Can the public claim be supported without exposing private evidence?

## Access discipline

Use least privilege. Prefer read-only inspection when writing is unnecessary. Keep credentials outside source control. Separate environments where practical. Require explicit approval for destructive, irreversible or high-impact actions.

Security must be enforced by the real access layer. UI visibility is not authorization.

A public/private boundary failure blocks publication until resolved.
