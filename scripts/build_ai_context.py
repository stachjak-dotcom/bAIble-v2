#!/usr/bin/env python3
"""Generate a revision-bound single-file bAIble AI context bundle.

The output is a transport artifact, not a canonical source. Edit source files,
not the generated bundle.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "AI_CONTEXT_MANIFEST.json"


def git_revision() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "UNKNOWN"


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def selected_files(manifest: dict, profile: str) -> list[str]:
    core = manifest["profiles"]["core"]
    if profile == "core":
        return core
    if profile == "full":
        return core + manifest["profiles"].get("reference", [])
    raise ValueError(f"Unsupported profile: {profile}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=["core", "full"], default="core")
    parser.add_argument("--output", default="dist/BAIBLE_AI_CONTEXT.md")
    args = parser.parse_args()

    manifest = load_manifest()
    files = selected_files(manifest, args.profile)

    missing = [p for p in files if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit("Missing source files: " + ", ".join(missing))

    revision = git_revision()
    generated_at = datetime.now(timezone.utc).isoformat()
    out = ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)

    parts = [
        "# bAIble v2 — Generated AI Context Bundle",
        "",
        "> GENERATED TRANSPORT ARTIFACT — DO NOT EDIT AS A CANONICAL SOURCE.",
        "> Canonical meaning remains in the source files listed below.",
        "",
        f"- profile: {args.profile}",
        f"- source revision: {revision}",
        f"- generated at: {generated_at}",
        "- manifest: AI_CONTEXT_MANIFEST.json",
        "",
        "Core distinction:",
        "",
        "DISCOVERABLE != LOADED != ACTIVE != AUTHORIZED",
        "",
        "## Included source files",
        "",
    ]
    parts.extend(f"- {p}" for p in files)
    parts.extend(["", "---", ""])

    for path in files:
        text = (ROOT / path).read_text(encoding="utf-8").rstrip()
        parts.extend([
            f"# SOURCE: {path}",
            "",
            text,
            "",
            "---",
            "",
        ])

    out.write_text("\n".join(parts), encoding="utf-8")
    print(out.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
