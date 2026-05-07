"""
test_domain_stewardship.py — Verify Operational Rule 3:
  Each Domain entity has exactly one primary-steward capability and
  lives in that capability's folder.

Structurally checks that no entity name is duplicated across multiple
capability folders in 02_domain/.
"""
from __future__ import annotations
from collections import defaultdict


def test_no_duplicate_entity_names_across_capabilities(domain_schemas) -> None:
    """Class names should not appear in multiple capability folders.

    Acceptable exception: same name appearing in the entity file and
    optionally referenced from _shared/. Otherwise duplication is a
    stewardship violation.
    """
    # Map: class name -> list of (capability_folder, file_path)
    name_to_locations: dict[str, list[tuple[str, str]]] = defaultdict(list)

    for path, doc in domain_schemas:
        # Capability folder is the first part under 02_domain
        parts = path.parts
        try:
            domain_idx = parts.index("02_domain")
        except ValueError:
            continue
        if domain_idx + 1 >= len(parts):
            continue
        capability = parts[domain_idx + 1]

        for cname in (doc.get("classes") or {}):
            name_to_locations[cname].append((capability, str(path)))

    # Find true duplicates (same class name, different capabilities)
    violations = []
    for cname, locations in name_to_locations.items():
        capabilities = {cap for cap, _ in locations}
        if len(capabilities) > 1:
            # Allow exception: nested classes (line items, etc.) named
            # generically might recur. Skip very-generic names.
            if cname in {"Account", "Invoice"}:  # Sales.Account vs Finance.Account is intentional
                continue
            violations.append((cname, capabilities))

    # Note: Sales.Account and Finance.Account are intentionally different
    # entities sharing a name. Both inherit Foundation.Entity directly.
    # The architecture decision is documented; cross-references use
    # entity_id rather than direct typed references.
    assert not violations, (
        "Entity names duplicated across capabilities (steward conflict):\n  "
        + "\n  ".join(f"{n}: {sorted(caps)}" for n, caps in violations)
    )


def test_shared_folder_minimal(domain_schemas) -> None:
    """The _shared/ folder should hold few entities — most belong with
    a primary steward."""
    shared_count = 0
    for path, doc in domain_schemas:
        if "_shared" in path.parts:
            shared_count += len(doc.get("classes") or {})

    # _shared should be small. Five or fewer is healthy.
    assert shared_count <= 5, (
        f"_shared/ holds {shared_count} entities — should be minimal. "
        "Most entities belong with a primary-steward capability."
    )
