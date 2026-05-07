#!/usr/bin/env python3
"""
generate_json_schema.py — Generate JSON Schema artifacts from EDM
LinkML schemas.

Walks src/ and emits one .json file per LinkML schema that defines
classes (skips pure enum/codelist files which are imported into the
schemas that use them).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    src = root / "src"
    out = root / "generated" / "json_schema"
    out.mkdir(parents=True, exist_ok=True)

    count = 0
    errors = 0

    for path in sorted(src.rglob("*.yaml")):
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        if not doc.get("classes"):
            continue  # skip pure enum / type files

        rel = path.relative_to(src).with_suffix(".json")
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)

        try:
            subprocess.run(
                ["gen-json-schema", str(path)],
                stdout=open(target, "w"),
                stderr=subprocess.PIPE,
                check=True,
            )
            count += 1
        except FileNotFoundError:
            print("ERROR: gen-json-schema not found. Install LinkML: pip install linkml")
            return 2
        except subprocess.CalledProcessError as exc:
            print(f"FAILED: {path.relative_to(root)}: {exc.stderr.decode()[:200]}")
            errors += 1

    print(f"Generated {count} JSON Schema files in {out.relative_to(root)}/")
    if errors:
        print(f"({errors} errors)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
