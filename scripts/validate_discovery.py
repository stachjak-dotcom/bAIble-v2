#!/usr/bin/env python3
"""Validate bAIble discovery/resource-routing integrity."""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    required = [
        "DISCOVERY_AND_LOADING.md", "START_HERE.md", "SYSTEM_MAP.md",
        "ECOSYSTEM_GRAPH.json", "AI_VIEW.md", "BIBLE.md",
        "PUBLIC_PRIVATE_BOUNDARY.md", "llms.txt", "AGENTS.md",
        "AI_CONTEXT_MANIFEST.json",
    ]
    for path in required:
        if not (ROOT / path).is_file():
            fail(errors, f"missing required discovery file: {path}")

    try:
        graph = json.loads((ROOT / "ECOSYSTEM_GRAPH.json").read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, f"invalid ECOSYSTEM_GRAPH.json: {exc}")
        graph = {"nodes": [], "view_hints": {}, "routing_hints": {}}

    node_ids = {n.get("id") for n in graph.get("nodes", [])}
    for node in graph.get("nodes", []):
        for resource in node.get("resources", []):
            if not (ROOT / resource).is_file():
                fail(errors, f"node {node.get('id')} references missing resource {resource}")

    for view, refs in graph.get("view_hints", {}).items():
        for ref in refs:
            if ref not in node_ids:
                fail(errors, f"view_hints.{view} references missing node {ref}")

    for route, spec in graph.get("routing_hints", {}).items():
        for ref in spec.get("nodes", []):
            if ref not in node_ids:
                fail(errors, f"routing_hints.{route} references missing node {ref}")
        for resource in spec.get("resources", []):
            if not (ROOT / resource).is_file():
                fail(errors, f"routing_hints.{route} references missing resource {resource}")

    try:
        manifest = json.loads((ROOT / "AI_CONTEXT_MANIFEST.json").read_text(encoding="utf-8"))
        for profile, files in manifest.get("profiles", {}).items():
            seen: set[str] = set()
            for path in files:
                if path in seen:
                    fail(errors, f"manifest profile {profile} duplicates {path}")
                seen.add(path)
                if not (ROOT / path).is_file():
                    fail(errors, f"manifest profile {profile} references missing {path}")
    except Exception as exc:
        fail(errors, f"invalid AI_CONTEXT_MANIFEST.json: {exc}")

    llms = (ROOT / "llms.txt").read_text(encoding="utf-8") if (ROOT / "llms.txt").is_file() else ""
    raw_paths = re.findall(
        r"https://raw\.githubusercontent\.com/stachjak-dotcom/bAIble-v2/main/([^\s)]+)",
        llms,
    )
    for path in raw_paths:
        if not (ROOT / path).is_file():
            fail(errors, f"llms.txt points to missing repository path {path}")

    if errors:
        print("Discovery validation FAILED:", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print("Discovery validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
