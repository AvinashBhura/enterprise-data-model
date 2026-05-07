"""
test_process_binding_immutability.py — Verify Operational Rule 4:
  ProcessInstance.definition is set at creation and never changes.

Structurally, this rule is enforced by:
- ProcessInstance.definition being required
- ProcessInstance.migrated_to_instance / migrated_from_instance slots
  existing, so migration is modeled as a new instance (not a binding mutation)
"""
from __future__ import annotations


def test_process_instance_has_required_definition(process_schemas) -> None:
    """The base ProcessInstance class should have `definition` as a
    required slot."""
    found = False
    for path, doc in process_schemas:
        if path.name != "ProcessInstance.yaml":
            continue
        classes = doc.get("classes") or {}
        pi = classes.get("ProcessInstance")
        assert pi is not None, "ProcessInstance class not found"
        attrs = pi.get("attributes") or {}
        defn = attrs.get("definition")
        assert defn is not None, "ProcessInstance.definition slot missing"
        assert defn.get("required") is True, (
            "ProcessInstance.definition should be required (Frozen-Contract principle)"
        )
        found = True
        break
    assert found, "ProcessInstance.yaml not found in process_schemas"


def test_process_instance_supports_migration_pattern(process_schemas) -> None:
    """ProcessInstance should expose migration-tracking slots
    (migrated_to_instance / migrated_from_instance) so binding
    immutability can be enforced via the new-instance pattern."""
    for path, doc in process_schemas:
        if path.name != "ProcessInstance.yaml":
            continue
        pi = (doc.get("classes") or {}).get("ProcessInstance") or {}
        attrs = pi.get("attributes") or {}
        assert "migrated_to_instance" in attrs, (
            "ProcessInstance should expose migrated_to_instance for migration tracking"
        )
        assert "migrated_from_instance" in attrs, (
            "ProcessInstance should expose migrated_from_instance"
        )
        return
    raise AssertionError("ProcessInstance.yaml not found")
