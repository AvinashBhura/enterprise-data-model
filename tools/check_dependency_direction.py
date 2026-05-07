#!/usr/bin/env python3
"""
check_dependency_direction.py — Enforce the One-Way Gate rule.

Dependencies must flow upward only:
  Foundation → Common → Domain → Process → Application
A schema must never import from a layer above its own.

Returns non-zero exit code on violation.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml


# Layer order (lower index = lower in the stack)
LAYER_ORDER = ["01_foundation", "02_domain", "03_process", "04_application"]
# Common is treated as part of Foundation for dependency purposes
# (since it's nested inside it).


def layer_index(path_parts: tuple[str, ...]) -> int:
    """Return the layer index for a path's first component."""
    if not path_parts:
        return -1
    first = path_parts[0]
    if first in LAYER_ORDER:
        return LAYER_ORDER.index(first)
    return -1


def resolve_import(importer: Path, imp: str, src_root: Path) -> Path | None:
    """Resolve a LinkML import string to an absolute path under src_root.

    Imports starting with linkml: or anything not pointing under src/ are
    ignored (they're external, not internal cross-layer references).
    """
    if imp.startswith("linkml:"):
        return None
    if imp.startswith("http://") or imp.startswith("https://"):
        return None
    # Relative path (the most common form in this project)
    candidate = (importer.parent / imp).resolve()
    # LinkML imports often omit the .yaml extension
    if not candidate.suffix:
        candidate = candidate.with_suffix(".yaml")
    try:
        candidate.relative_to(src_root)
        return candidate
    except ValueError:
        return None


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    src = root / "src"

    violations: list[tuple[Path, Path, str]] = []
    checked = 0

    for path in sorted(src.rglob("*.yaml")):
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
        except yaml.YAMLError:
            continue

        if not isinstance(doc, dict):
            continue

        importer_layer = layer_index(path.relative_to(src).parts)

        imports = doc.get("imports") or []
        for imp in imports:
            if not isinstance(imp, str):
                continue
            target = resolve_import(path, imp, src)
            if target is None:
                continue
            checked += 1
            target_layer = layer_index(target.relative_to(src).parts)
            # A higher-numbered (above) layer being imported by a
            # lower-numbered (below) one is a violation.
            if target_layer > importer_layer:
                violations.append(
                    (
                        path.relative_to(root),
                        target.relative_to(root),
                        f"layer {LAYER_ORDER[importer_layer]} imports from "
                        f"layer {LAYER_ORDER[target_layer]} (downward arrow forbidden)",
                    )
                )

    print(f"Checked {checked} cross-layer imports.")
    if violations:
        print(f"\nVIOLATIONS ({len(violations)}):")
        for importer, target, msg in violations:
            print(f"  {importer}")
            print(f"    imports {target}")
            print(f"    -> {msg}")
        print()
        print("Dependency direction check FAILED.")
        return 1

    print("Dependency direction check passed: all imports flow upward only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
