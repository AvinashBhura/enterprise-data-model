# Pattern — Natural Keys and Surrogates

## The principle

Every Entity carries a **surrogate identifier** (`entity_id`, a UUID)
that never changes. **Natural identifiers** (business keys) are
optional and may be multiple, each scoped to an issuing scheme. The
**placement of natural keys depends on whether they are
enterprise-issued or vendor-issued**.

## The surrogate (entity_id)

Defined on `Foundation.Entity` and inherited by every concept:

```yaml
Entity:
  attributes:
    entity_id:
      identifier: true
      range: uuid
      required: true
```

Properties:
- Globally unique (UUID v4).
- System-generated at creation; never changes.
- Stable across systems, reorganizations, integrations, vendor migrations.
- The join key for cross-system queries.

The surrogate is what makes integration possible. Different systems
will represent the same Person with different vendor IDs — but the
single Person.entity_id ties them together.

## The natural identifiers

Defined on `Common.Identifiable`:

```yaml
Identifiable:
  mixin: true
  attributes:
    natural_identifiers:
      range: NaturalIdentifier
      multivalued: true

NaturalIdentifier:
  attributes:
    value: { range: string, required: true }
    scheme: { range: string, required: true }
    issuer: { range: string }
    issued_at: { range: date }
    valid_from: { range: date }
    valid_to: { range: date }
```

A single entity may carry zero, one, or many natural identifiers,
each tagged by the scheme that issued it.

## The placement rule (Operational Rule 2)

> **Enterprise-native** natural keys live on canonical entities via
> `Identifiable.natural_identifiers`.
> **System-of-record vendor** natural keys live ONLY on Application-
> layer subclasses.

**Examples**:

| Identifier | Placement |
|---|---|
| Acme employee_number "E10847" | EmployeeRole.natural_identifiers (enterprise-issued) |
| Workday Worker ID "WD-998234" | WorkdayEmployeeRole.workday_worker_id (vendor-issued) |
| Okta User ID "00u3j2nKLuZcq5z7B3a8" | OktaUser.okta_user_id (vendor-issued) |
| ISO country code "US" | Address.country (codelist value) |
| Tax ID | LegalEntity.tax_identifier or natural_identifier (depending on use) |

## Why this distinction matters

If you put `workday_worker_id` directly on the canonical EmployeeRole:
- When you migrate from Workday, every EmployeeRole record needs
  schema surgery.
- Domain becomes coupled to vendor presence.
- Multiple vendors can't coexist (which Workday ID is "the" one?).

If `workday_worker_id` lives on `WorkdayEmployeeRole` only:
- Migrate to a new HRIS by retiring `WorkdayEmployeeRole` records and
  creating new `NewHRISEmployeeRole` records. Canonical EmployeeRole
  unchanged.
- Multiple vendor projections can coexist freely.
- Domain stays vendor-neutral.

## Querying across systems

To find "the same Person across all systems":
```
Person where entity_id = X
WorkdayPerson where entity_id = X (inherits all Person fields)
SalesforceContact where entity_id = X (held_by_person points back)
OktaUser where entity_id = X (held_by_person points back)
```

The surrogate `entity_id` is the universal join key. Application
projections inherit it from the canonical entity (via `is_a`) and
add their vendor-specific natural keys.

## Anti-patterns

- Using a natural key as the primary identifier (employee_number can be
  reissued; UUID can't).
- Storing vendor IDs on canonical entities.
- Storing identifiers as bare strings without a scheme tag.
