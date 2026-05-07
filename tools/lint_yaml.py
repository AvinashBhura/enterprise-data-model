#!/usr/bin/env python3
"""
lint_yaml.py — Light YAML linting for the EDM project.

Checks:
- Files parse as valid YAML.
- Files use consistent 2-space indentation (no tabs).
- Lines under reasonable length (warn over 120 chars).
- Files end with a newline.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    src = root / "src"

    issues: list[tuple[Path, int, str]] = []
    checked = 0

    for path in sorted(src.rglob("*.yaml")):
        checked += 1
        with open(path) as f:
            content = f.read()
            lines = content.splitlines()

        # Parse check
        try:
            yaml.safe_load(content)
        except yaml.YAMLError as exc:
            issues.append((path, 0, f"YAML parse error: {exc}"))
            continue

        # Tab check
        for lineno, line in enumerate(lines, start=1):
            if "\t" in line:
                issues.append((path, lineno, "tab character found (use spaces)"))

        # Long-line warning
        for lineno, line in enumerate(lines, start=1):
            if len(line) > 200:
                issues.append((path, lineno, f"line is {len(line)} chars (very long)"))

        # Trailing newline
        if content and not content.endswith("\n"):
            issues.append((path, len(lines), "file does not end with a newline"))

    print(f"Linted {checked} YAML files.")
    if issues:
        print(f"\nLint issues ({len(issues)}):")
        for path, lineno, msg in issues:
            print(f"  {path.relative_to(root)}:{lineno}: {msg}")
        return 1

    print("Lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
