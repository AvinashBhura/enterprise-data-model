"""
test_codelist_vs_taxonomy_placement.py — Verify Operational Rule 5:
  Codelists hold flat enums (no hierarchy);
  Taxonomies hold hierarchical classifications;
  Instance data lives in Domain, not Common.
"""
from __future__ import annotations


def test_codelist_files_contain_only_enums(foundation_schemas) -> None:
    """Files under common/codelists/ should contain only enums (and
    possibly minimal type definitions), no business classes."""
    violations = []
    for path, doc in foundation_schemas:
        if "codelists" not in path.parts:
            continue
        classes = doc.get("classes") or {}
        if classes:
            # Check whether any of the classes look like business entities
            for cname, cdef in classes.items():
                if not isinstance(cdef, dict):
                    continue
                # Allow small wrapper classes used to package enums; flag
                # anything inheriting from a business Entity.
                if cdef.get("is_a") in {"Entity", "Person", "Organization"}:
                    violations.append(f"{path.name}::{cname}")

    assert not violations, (
        "Codelist files contain business classes (should hold only enums):\n  "
        + "\n  ".join(violations)
    )


def test_taxonomy_files_present(foundation_schemas) -> None:
    """The taxonomies/ folder should contain non-empty schema files."""
    taxonomy_files = [
        (p, d) for p, d in foundation_schemas if "taxonomies" in p.parts
    ]
    assert len(taxonomy_files) > 0, "No taxonomy files found in common/taxonomies/"


def test_no_specific_instance_data_in_taxonomies(foundation_schemas) -> None:
    """Taxonomy files should hold abstract category hierarchies, not
    specific Acme-or-similar instance data. Heuristic check: the word
    'Acme' shouldn't appear in any taxonomy file."""
    violations = []
    for path, doc in foundation_schemas:
        if "taxonomies" not in path.parts:
            continue
        # Re-read file to check for instance-marker strings
        with open(path) as f:
            content = f.read().lower()
        for marker in ["acme", "specific division", "our department"]:
            if marker in content:
                violations.append(f"{path.name} contains '{marker}'")

    assert not violations, (
        "Taxonomy files should not contain enterprise-specific instance data:\n  "
        + "\n  ".join(violations)
    )
