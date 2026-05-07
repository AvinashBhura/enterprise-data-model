#!/usr/bin/env python3
"""
generate_sql_ddl.py — Generate SQL DDL from EDM LinkML schemas.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    src = root / "src"
    out = root / "generated" / "sql"
    out.mkdir(parents=True, exist_ok=True)

    count = 0
    errors = 0

    for path in sorted(src.rglob("*.yaml")):
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict) or not doc.get("classes"):
            continue

        rel = path.relative_to(src).with_suffix(".sql")
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)

        try:
            subprocess.run(
                ["gen-sqltables", str(path)],
                stdout=open(target, "w"),
                stderr=subprocess.PIPE,
                check=True,
            )
            count += 1
        except FileNotFoundError:
            print("ERROR: gen-sqltables not found. Install LinkML: pip install linkml")
            return 2
        except subprocess.CalledProcessError as exc:
            print(f"FAILED: {path.relative_to(root)}: {exc.stderr.decode()[:200]}")
            errors += 1

    print(f"Generated {count} SQL DDL files in {out.relative_to(root)}/")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
