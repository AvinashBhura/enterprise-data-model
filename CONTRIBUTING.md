# Contributing to the Enterprise Data Model

Thank you for contributing. This document describes how to propose and
submit changes to the EDM.

## The Golden Rules

1. **Dependency direction flows upward only.** Never add an import that
   would make a lower layer depend on a higher one.
2. **Respect the stability tier of each layer.** Foundation changes are
   rare and require architecture review. Domain changes require domain-
   steward approval. Process and Application changes can move faster.
3. **No upstream pollution from Application.** Vendor-specific fields
   belong in the Application layer only.

## Proposing Changes

### For Foundation changes

Foundation changes ripple across every layer. They require:

1. Open an Issue describing the change and its justification against the
   seven Foundation principles.
2. Architecture review by the EDM steering committee.
3. Formal deprecation of any removed slot over at least two release cycles.
4. Major version bump for breaking changes.

### For Common changes

Common changes affect multiple downstream consumers. They require:

1. Demonstrate the change passes the Reusability Test (would another
   enterprise need this?).
2. Verify the change does not violate the Clean-Contract (non-overlap)
   rule for base types.
3. Review by at least two domain stewards.

### For Domain changes

1. Primary-steward approval for the capability.
2. Ensure the change respects Inheritance-only extension from Foundation.
3. Lifecycle enums and type enums are per-entity; add new ones in the
   appropriate `enums/` sub-folder, not in Common.

### For Process and Application changes

More latitude — these layers are designed for volatility. Still:

- Process definitions must be versioned.
- Application classes must carry their source-system binding and
  never mutate Domain semantics.

## Pull Request Checklist

- [ ] Schema validates (`python tools/validate_all.py` passes).
- [ ] Dependency-direction check passes (`python tools/check_dependency_direction.py`).
- [ ] Architectural-rule tests pass (`pytest tests/architectural_rules/`).
- [ ] New entities have inline `description:` on both class and every slot.
- [ ] New enums use SCREAMING_SNAKE_CASE for values.
- [ ] New lifecycle enums are scoped per-entity and live in the appropriate folder.
- [ ] README updated in any modified directory.
- [ ] CHANGELOG entry added under "Unreleased".

## Naming Conventions

- **Entity classes**: `PascalCase`, singular noun (`Person`, `EmployeeRole`).
- **Slot names**: `snake_case` (`hire_date`, `employing_organization`).
- **Enum classes**: `PascalCase` ending in `Enum` (`RoleTypeEnum`).
- **Enum values**: `SCREAMING_SNAKE_CASE` (`EMPLOYEE`, `FULL_TIME`).
- **Files**: match the primary class they define (`Person.yaml`, `EmployeeRole.yaml`).
- **Application subclasses**: prefix with vendor (`WorkdayEmployeeRole`,
  `SalesforceContact`).

## Review Cadence

- Architecture review meetings: monthly.
- Domain-steward office hours: weekly per capability.
- Release cadence: minor releases every 6 weeks, major releases planned.
