"""
test_natural_key_placement.py — Verify Operational Rule 2:
  Vendor system natural keys live ONLY on Application-layer subclasses.

This test scans canonical (non-Application) entities for slots whose
names look like vendor system identifiers (workday_*, sf_*, snow_*,
sap_*, okta_*).
"""
from __future__ import annotations

VENDOR_KEY_PREFIXES = (
    "workday_",
    "sf_",
    "snow_",
    "sap_",
    "okta_",
    "salesforce_",
    "servicenow_",
)


def _collect_attribute_names(class_def: dict) -> list[str]:
    return list((class_def.get("attributes") or {}).keys())


def test_vendor_keys_not_on_canonical_entities(
    foundation_schemas, domain_schemas, process_schemas
) -> None:
    """No canonical (non-Application) entity should declare attributes
    starting with a known vendor key prefix."""
    violations = []
    for path, doc in foundation_schemas + domain_schemas + process_schemas:
        for class_name, class_def in (doc.get("classes") or {}).items():
            if not isinstance(class_def, dict):
                continue
            for attr_name in _collect_attribute_names(class_def):
                if attr_name.startswith(VENDOR_KEY_PREFIXES):
                    violations.append(
                        f"{path.name}::{class_name}.{attr_name} "
                        f"(vendor-prefix attribute on canonical entity)"
                    )
    assert not violations, (
        "Vendor-system natural keys must live only on Application-layer "
        f"subclasses. Violations:\n  - " + "\n  - ".join(violations)
    )


def test_vendor_keys_present_on_application_entities(application_schemas) -> None:
    """At least one Application-layer entity should carry a vendor-key
    attribute (sanity check that the vendor-folders pattern is in use)."""
    found_any = False
    for _path, doc in application_schemas:
        for class_def in (doc.get("classes") or {}).values():
            if not isinstance(class_def, dict):
                continue
            for attr_name in _collect_attribute_names(class_def):
                if attr_name.startswith(VENDOR_KEY_PREFIXES):
                    found_any = True
                    break
            if found_any:
                break
        if found_any:
            break
    assert found_any, "No Application-layer entities carry vendor-key attributes"
