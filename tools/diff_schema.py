#!/usr/bin/env python3
"""
diff_schema.py — Show structural changes between two schema versions.

Usage:
  python tools/diff_schema.py <old_dir> <new_dir>

Compares two `src/` trees by file, listing added/removed/changed
classes, enums, and attributes.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml


def index_schemas(src_dir: Path) -> dict[str, dict]:
    """Build a map of relative-path -> parsed schema."""
    out = {}
    for path in src_dir.rglob("*.yaml"):
        rel = str(path.relative_to(src_dir))
        try:
            with open(path) as f:
                out[rel] = yaml.safe_load(f) or {}
        except yaml.YAMLError:
            out[rel] = {}
    return out


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: diff_schema.py <old_dir> <new_dir>")
        return 2

    old_root, new_root = Path(sys.argv[1]), Path(sys.argv[2])
    old_idx = index_schemas(old_root)
    new_idx = index_schemas(new_root)

    added = sorted(set(new_idx) - set(old_idx))
    removed = sorted(set(old_idx) - set(new_idx))
    common = sorted(set(old_idx) & set(new_idx))

    if added:
        print(f"\nAdded files ({len(added)}):")
        for f in added:
            print(f"  + {f}")

    if removed:
        print(f"\nRemoved files ({len(removed)}):")
        for f in removed:
            print(f"  - {f}")

    print("\nChanged files:")
    for rel in common:
        old_doc = old_idx[rel]
        new_doc = new_idx[rel]
        old_classes = set((old_doc.get("classes") or {}).keys())
        new_classes = set((new_doc.get("classes") or {}).keys())
        old_enums = set((old_doc.get("enums") or {}).keys())
        new_enums = set((new_doc.get("enums") or {}).keys())

        added_cls = new_classes - old_classes
        removed_cls = old_classes - new_classes
        added_en = new_enums - old_enums
        removed_en = old_enums - new_enums

        if added_cls or removed_cls or added_en or removed_en:
            print(f"  ~ {rel}")
            for c in sorted(added_cls):
                print(f"      +class {c}")
            for c in sorted(removed_cls):
                print(f"      -class {c}")
            for e in sorted(added_en):
                print(f"      +enum {e}")
            for e in sorted(removed_en):
                print(f"      -enum {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
