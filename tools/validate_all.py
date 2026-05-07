#!/usr/bin/env python3
"""
validate_all.py — Validate every LinkML schema in src/ parses cleanly
and has required top-level metadata.

Returns non-zero exit code on any error.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml


REQUIRED_TOP_LEVEL = ("id", "name")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    src = root / "src"

    errors: list[tuple[Path, str]] = []
    counts = {"schemas": 0, "classes": 0, "enums": 0, "types": 0}
    by_layer: dict[str, dict[str, int]] = {}

    for path in sorted(src.rglob("*.yaml")):
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            errors.append((path, f"YAML parse error: {exc}"))
            continue

        if not isinstance(doc, dict):
            errors.append((path, "schema is not a YAML mapping"))
            continue

        for required in REQUIRED_TOP_LEVEL:
            if required not in doc:
                errors.append((path, f"missing required top-level key: {required!r}"))

        # Stats
        layer = path.relative_to(src).parts[0]
        layer_stats = by_layer.setdefault(
            layer, {"files": 0, "classes": 0, "enums": 0, "types": 0}
        )
        layer_stats["files"] += 1
        n_classes = len(doc.get("classes", {}) or {})
        n_enums = len(doc.get("enums", {}) or {})
        n_types = len(doc.get("types", {}) or {})
        layer_stats["classes"] += n_classes
        layer_stats["enums"] += n_enums
        layer_stats["types"] += n_types
        counts["schemas"] += 1
        counts["classes"] += n_classes
        counts["enums"] += n_enums
        counts["types"] += n_types

    # Report
    print(
        f"Validated {counts['schemas']} schemas: "
        f"{counts['classes']} classes, {counts['enums']} enums, {counts['types']} types."
    )
    print()
    for layer, stats in sorted(by_layer.items()):
        print(
            f"  {layer:<25} {stats['files']:>4} files, "
            f"{stats['classes']:>4} classes, "
            f"{stats['enums']:>4} enums, "
            f"{stats['types']:>2} types"
        )

    if errors:
        print()
        print(f"ERRORS ({len(errors)}):")
        for path, msg in errors:
            print(f"  {path.relative_to(root)}: {msg}")
        return 1

    print()
    print("All schemas validated cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
