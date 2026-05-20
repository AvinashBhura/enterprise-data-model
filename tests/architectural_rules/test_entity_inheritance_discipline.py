"""
Test: Strict-Foundation inheritance discipline.

Rule: Only Foundation entities inherit directly from Entity. Every Domain,
Process, and Application entity must specialize a Foundation entity (or a
chain ending at one). is_a: Entity is forbidden outside src/01_foundation/.

Rationale: Entity exists purely as a semantic anchor. Domain entities should
declare their kind (Person, Organization, Role, Activity, Agreement, Asset,
Address, Document, Period) so the model has a complete ontology rather than
an escape hatch.
"""

from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC = REPO_ROOT / "src"

LAYERS_REQUIRING_DISCIPLINE = ["02_domain", "03_process", "04_application"]


def _iter_class_definitions(yaml_path: Path):
    """Yield (class_name, class_body) for each class in a YAML schema."""
    with open(yaml_path) as f:
        doc = yaml.safe_load(f) or {}
    classes = doc.get("classes", {}) or {}
    for name, body in classes.items():
        if isinstance(body, dict):
            yield name, body


def test_no_direct_entity_inheritance_outside_foundation():
    """Every class in Domain, Process, and Application must NOT declare is_a: Entity."""
    violations = []

    for layer in LAYERS_REQUIRING_DISCIPLINE:
        layer_root = SRC / layer
        if not layer_root.exists():
            continue
        for yaml_file in layer_root.rglob("*.yaml"):
            for class_name, class_body in _iter_class_definitions(yaml_file):
                is_a = class_body.get("is_a")
                if is_a == "Entity":
                    rel = yaml_file.relative_to(REPO_ROOT)
                    violations.append(f"{rel}: class {class_name} directly inherits from Entity")

    assert not violations, (
        "Strict-Foundation rule violated: only Foundation entities may directly "
        "specialize Entity. Other entities must specialize a more specific "
        "Foundation kind (Person, Organization, Team, Role, Activity, Agreement, "
        "Asset, Address, Document, Period).\n\nViolations:\n  - "
        + "\n  - ".join(violations)
    )


def test_every_non_foundation_class_has_is_a():
    """Every concrete class outside Foundation must declare is_a (or be a mixin)."""
    violations = []

    for layer in LAYERS_REQUIRING_DISCIPLINE:
        layer_root = SRC / layer
        if not layer_root.exists():
            continue
        for yaml_file in layer_root.rglob("*.yaml"):
            for class_name, class_body in _iter_class_definitions(yaml_file):
                # Skip mixins, abstract classes, and value types
                if class_body.get("mixin") is True:
                    continue
                if class_body.get("abstract") is True:
                    continue
                # Value types (no slots/attributes that anchor identity) are skipped
                # if they don't declare is_a — they're construction material.
                if "is_a" not in class_body:
                    # Allow if class is just a structured value type (no entity_id concept)
                    if "_shared" in str(yaml_file):
                        continue
                    rel = yaml_file.relative_to(REPO_ROOT)
                    violations.append(f"{rel}: class {class_name} declares no is_a")

    assert not violations, (
        "Every non-Foundation, non-mixin, non-abstract class must declare is_a.\n\n"
        "Violations:\n  - " + "\n  - ".join(violations)
    )
