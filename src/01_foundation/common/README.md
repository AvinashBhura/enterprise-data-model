# Common Sub-Layer

The Common sub-layer holds the **reusable construction material** used
to build entities in Foundation and all layers above. It is nested
inside Foundation because it supports Foundation, it is not a peer.

## Principles

| # | Principle | Caption |
|---|---|---|
| 1 | Non-Ambiguity | **The One-Meaning Principle** — a value means the same thing wherever it appears |
| 2 | Reusability | **The Shared-Shelf Principle** — built once, pulled down by many |
| 3 | External Mapping | **The Rosetta Principle** — speaks fluent Schema.org, SKOS, and ISO |
| 4 | Supportive, Not Substantive | **The Scaffolding Principle** — holds up the building; isn't the building |
| 5 | Non-Overlap | **The Clean-Contract Principle** — no two base types claim the same attribute |

## Directory Structure

```
common/
├── base/                    # base types + value types (construction material)
│   ├── Identifiable.yaml    # base type — natural keys & audit timestamps
│   ├── Lifecycleable.yaml   # base type — lifecycle state and history
│   ├── Addressable.yaml     # base type — can hold addresses
│   ├── RoleHolder.yaml      # base type — can hold roles
│   ├── Classifiable.yaml    # base type — can be classified via taxonomies
│   ├── Temporal.yaml        # base type — bitemporal validity
│   ├── StateTransition.yaml # value type — state transition record
│   ├── NaturalIdentifier.yaml # value type — structured natural key
│   ├── AmountType.yaml      # value type — money (value + currency)
│   ├── QuantityType.yaml    # value type — quantity (value + unit)
│   └── DocumentType.yaml    # value type — document reference
│
├── codelists/               # flat, closed vocabularies
│   ├── standards/           # external standard codelists
│   │   ├── CurrencyCode.yaml       # ISO 4217
│   │   ├── CountryCode.yaml        # ISO 3166-1 alpha-2
│   │   ├── LanguageCode.yaml       # ISO 639-1
│   │   ├── UnitOfMeasureCode.yaml  # UN/CEFACT
│   │   └── TimeZoneCode.yaml       # IANA tz database
│   ├── types/               # type classifiers
│   │   ├── OrganizationTypeEnum.yaml
│   │   ├── TeamTypeEnum.yaml
│   │   ├── RoleTypeEnum.yaml
│   │   ├── EmploymentTypeEnum.yaml
│   │   ├── AgreementTypeEnum.yaml
│   │   ├── AssetTypeEnum.yaml
│   │   ├── AddressTypeEnum.yaml
│   │   └── ActivityTypeEnum.yaml
│   └── lifecycles/          # per-entity lifecycle state enums
│       ├── PersonLifecycleStateEnum.yaml
│       ├── OrganizationLifecycleStateEnum.yaml
│       ├── TeamLifecycleStateEnum.yaml
│       ├── RoleLifecycleStateEnum.yaml
│       ├── AgreementLifecycleStateEnum.yaml
│       ├── AssetLifecycleStateEnum.yaml
│       ├── ActivityLifecycleStateEnum.yaml
│       └── AddressLifecycleStateEnum.yaml
│
└── taxonomies/              # abstract hierarchical classifications
    ├── OrganizationTypeTaxonomy.yaml   # BU → Division → Department → ...
    ├── PositionTypeTaxonomy.yaml       # Job family hierarchy
    ├── AssetTypeTaxonomy.yaml          # Physical → Equipment → ...
    ├── GeographyTaxonomy.yaml          # Region → Country → State → City
    ├── IndustryClassificationTaxonomy.yaml  # NAICS/GICS/ISIC/SIC
    └── ChartOfAccountsTaxonomy.yaml    # Assets → Current Assets → ...
```

## Base Types vs Value Types

Both live in `base/`, distinguished by naming convention:
- **Base Types** — composed onto entities via mixin semantics. Names end in
  `-able` (Identifiable, Lifecycleable, Addressable, Classifiable).
  Exception: `RoleHolder`, `Temporal`.
- **Value Types** — referenced as attribute ranges, not composed. Names
  end in `Type` (AmountType, QuantityType, DocumentType) or are
  self-descriptive value records (StateTransition, NaturalIdentifier).

## Codelist vs Taxonomy vs Instance Data Rule

- **Codelists** — flat, closed vocabularies. No hierarchy. Example:
  `CurrencyCodeEnum` (USD, EUR, GBP, ...).
- **Taxonomies** — abstract hierarchical classifications (the category
  hierarchy, not specific instances). Example: `OrganizationTypeTaxonomy`
  declares that BusinessUnit can contain Division which can contain
  Department.
- **Instance Data** — specific records like "Acme's Engineering Division" —
  belong in the Domain layer, never in Common.

### The Reusability Test

Before placing anything in Common, ask: **would another enterprise, with a
completely different business, still need this exact construct?** If yes,
it's Common-worthy. If it's specific to this enterprise, it belongs in
Domain or master data.

## Non-Overlap Rule

Base types own disjoint attribute sets:
- `Identifiable` → natural keys, audit timestamps
- `Lifecycleable` → lifecycle state, state history
- `Addressable` → addresses
- `RoleHolder` → roles
- `Classifiable` → classifications
- `Temporal` → bitemporal validity

A base type never duplicates an attribute owned by another base type.
Composition is additive only.
