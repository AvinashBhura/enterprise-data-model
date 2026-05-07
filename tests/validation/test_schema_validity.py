"""
test_schema_validity.py — Each schema parses, has metadata, has at
least one definition.
"""
from __future__ import annotations


REQUIRED_TOP_LEVEL = ("id", "name")


def test_every_schema_has_required_metadata(all_schemas) -> None:
    """Every schema file should have id and name."""
    missing = []
    for path, doc in all_schemas:
        for key in REQUIRED_TOP_LEVEL:
            if key not in doc:
                missing.append(f"{path.name} missing {key}")
    assert not missing, "Schemas missing metadata:\n  " + "\n  ".join(missing)


def test_every_schema_defines_something(all_schemas) -> None:
    """Every schema should define at least one class, enum, or type."""
    empty = []
    for path, doc in all_schemas:
        if not (doc.get("classes") or doc.get("enums") or doc.get("types")):
            empty.append(path.name)
    # Permit empty schemas if explicitly used as collectors / forwarders
    # — but we don't have any of those by design, so flag all.
    assert not empty, "Empty schemas (no class/enum/type):\n  " + "\n  ".join(empty)


def test_layer_distribution_balanced(all_schemas) -> None:
    """Each of the four layers should have non-trivial content."""
    layer_counts = {}
    for path, _doc in all_schemas:
        for layer in ("01_foundation", "02_domain", "03_process", "04_application"):
            if layer in path.parts:
                layer_counts[layer] = layer_counts.get(layer, 0) + 1
                break

    for layer in ("01_foundation", "02_domain", "03_process", "04_application"):
        assert layer_counts.get(layer, 0) >= 5, (
            f"Layer {layer} has too few schemas ({layer_counts.get(layer, 0)})"
        )
