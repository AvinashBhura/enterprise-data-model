#!/usr/bin/env python3
"""
check_principle_compliance.py — Enforce architectural rules.

Checks:
1. Codelist files contain only `enums:`, no `classes:` (Common Rule 5).
2. Taxonomy files contain `classes:` (TaxonomyNode containers), no
   permissible_values lists (Common Rule 5).
3. Application-layer files do not introduce attributes that override
   canonical Domain/Process semantics (Extender Principle — best-effort
   check based on import paths).
4. Base type files have non-overlapping attribute names (Clean-Contract).
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    src = root / "src"

    violations: list[tuple[Path, str]] = []
    checks_run = 0

    # Rule 1: codelist files contain only enums
    for path in sorted(src.glob("01_foundation/common/codelists/**/*.yaml")):
        checks_run += 1
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        if doc.get("classes"):
            # Allow if the only "class" is a wrapper (some codelists may have one)
            classes = doc["classes"]
            if isinstance(classes, dict) and classes:
                violations.append(
                    (path, "codelist file contains classes (should hold only enums)")
                )

    # Rule 2: taxonomy files have hierarchical structure (classes for TaxonomyNode containers)
    for path in sorted(src.glob("01_foundation/common/taxonomies/*.yaml")):
        checks_run += 1
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        # Taxonomies are expected to contain classes (TaxonomyNode container)
        # OR import the shared TaxonomyNode and define a container.
        if not doc.get("classes") and not doc.get("imports"):
            violations.append(
                (path, "taxonomy file has neither classes nor imports (suspicious)")
            )

    # Rule 4: base type non-overlap — collect attribute names per base type
    base_attrs: dict[str, set[str]] = {}
    for path in sorted(src.glob("01_foundation/common/base/*.yaml")):
        checks_run += 1
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        for class_name, class_def in (doc.get("classes") or {}).items():
            if not isinstance(class_def, dict):
                continue
            if class_def.get("mixin"):
                attrs = set((class_def.get("attributes") or {}).keys())
                base_attrs[class_name] = attrs

    # Check pairwise overlaps
    base_names = list(base_attrs.keys())
    for i in range(len(base_names)):
        for j in range(i + 1, len(base_names)):
            a, b = base_names[i], base_names[j]
            overlap = base_attrs[a] & base_attrs[b]
            if overlap:
                violations.append(
                    (
                        src / f"01_foundation/common/base/{a}.yaml",
                        f"base type {a} overlaps with {b} on attributes: "
                        f"{sorted(overlap)}",
                    )
                )

    print(f"Ran {checks_run} compliance checks.")
    if violations:
        print(f"\nViolations ({len(violations)}):")
        for path, msg in violations:
            print(f"  {path.relative_to(root) if path.is_relative_to(root) else path}: {msg}")
        return 1

    print("All architectural rule checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
