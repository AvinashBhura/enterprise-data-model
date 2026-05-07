# The Dependency Direction Rule (One-Way Gate)

The single most important rule in the EDM:

> **Dependencies flow upward only.**
> Foundation → Common → Domain → Process → Application
> Nothing below imports from anything above it.

## What This Means in Practice

For any LinkML schema file `X.yaml`, the only files it may `import` are:
- Files in its own layer (when same-layer references are needed)
- Files in any layer **below** its own

It MUST NOT import files in any layer above its own.

## Concrete Allowed-Import Matrix

| Layer | May Import From |
|---|---|
| `01_foundation/` | Itself only (never its sub-layer Common from outside) |
| `01_foundation/common/` | linkml + Foundation (e.g., Common can reference Address from Foundation) |
| `02_domain/` | Foundation, Common |
| `03_process/` | Foundation, Common, Domain |
| `04_application/` | Foundation, Common, Domain, Process |

## Why It Matters

This rule is what gives the EDM its **stability gradient**. Foundation
changes are rare and ripple everywhere; Application changes are constant
and ripple nowhere. The one-way arrows are what make this asymmetry
possible.

If even one downward import is allowed, the gradient collapses:
Foundation must change every time anything above it changes.

## How It's Enforced

`tools/check_dependency_direction.py` parses every YAML file's
`imports:` section, classifies each import path by layer, and fails CI
on any downward import.

CI runs on every pull request:
```yaml
# .github/workflows/validate.yml
- name: Check dependency direction (one-way gate)
  run: python tools/check_dependency_direction.py
```

## Common Violations and Fixes

**Violation:** A Foundation file imports from `02_domain/HumanResources/`.
**Fix:** Reverse the relationship. The Domain file should reference the
Foundation entity, not the other way.

**Violation:** A Domain file imports from `04_application/Workday/`.
**Fix:** Move the relevant attribute up to Domain (if vendor-neutral)
or remove it (if Workday-specific). Application classes can reference
Domain; Domain never references Application.

**Violation:** A Process file imports from `04_application/`.
**Fix:** The Process layer must remain vendor-neutral. Application
classes specialize Process classes (via `is_a`), not the reverse.

## What About Same-Layer Imports?

Same-layer imports are allowed and expected. For example:
- `EmployeeRole.yaml` imports `Position.yaml` (both in HR Domain)
- `OnboardingProcessInstance.yaml` imports `OnboardingProcessDefinition.yaml`
  (both in Onboarding process family)
- `ProcessDefinition.yaml` (in `_core/`) imports `ProcessStep.yaml` (also in `_core/`)

What matters is that the import doesn't cross layers in the wrong direction.
