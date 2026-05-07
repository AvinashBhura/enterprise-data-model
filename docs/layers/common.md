# Layman's Guide — Common Sub-Layer

## What it is in one sentence

The reusable building blocks, value types, codelists, and
classification hierarchies that every layer above uses to construct
its entities.

## Why it matters

Suppose every department that records a money amount invents its own
way: HR stores it as a number with a separate currency field, Finance
as a string like "$1,200.00 USD", Sales as an object with nested
values. Now build a report that sums them all. You can't, without
heroic translation.

Common says: **we all use the same definitions for shared things.**
A money amount is *always* `value + currency_code`. A country is
*always* identified by an ISO code. An address *always* has line, city,
region, postal code, country.

## The Three Categories

### Base Types and Value Types (`base/`)
- **Base Types** are composed onto entities (mixin pattern). Names end
  in `-able`: `Identifiable`, `Lifecycleable`, `Addressable`,
  `Classifiable`. Plus `RoleHolder`, `Temporal`.
- **Value Types** are referenced as attribute ranges. Names end in
  `Type` or are descriptive value records: `AmountType`, `QuantityType`,
  `DocumentType`, `NaturalIdentifier`, `StateTransition`.

### Codelists (`codelists/`)
- **Standards** — external standard codelists (ISO 4217 currency,
  ISO 3166-1 country, ISO 639-1 language, UN/CEFACT units, IANA tz).
- **Types** — type classifiers (OrganizationType, TeamType, RoleType, …).
- **Lifecycles** — per-entity lifecycle state enums.

### Taxonomies (`taxonomies/`)
Hierarchical classifications: OrganizationTypeTaxonomy (BU → Division
→ Department → Team), PositionTypeTaxonomy, AssetTypeTaxonomy,
GeographyTaxonomy, IndustryClassificationTaxonomy, ChartOfAccountsTaxonomy.

## Why Common sits *under* Foundation, not as a peer

Common is construction material — it's not an enterprise concept in
its own right. "A currency code" is not a thing your business *does*
or *has*; it's a way of *describing* things your business has. That's
why Common is nested under Foundation: it's the material Foundation
is built from.

## The Reusability Test

Before placing anything in Common, ask:
*Would another enterprise, with a completely different business, still
need this exact construct?*
- Yes → Common-worthy.
- No → it's instance data, belongs in Domain or master data.

## See also

- Common principles: `docs/architecture/principles.md` (Common section)
- Codelist vs Taxonomy vs Instance Data rule: `docs/architecture/operational_rules.md` (Rule 5)
