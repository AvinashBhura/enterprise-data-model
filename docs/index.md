# EDM Documentation

This documentation explains the Enterprise Data Model in depth — its
architecture, principles, layers, entities, and the modeling patterns
that hold it together.

## Start Here

- **New to the EDM?** Read [`architecture/overview.md`](architecture/overview.md) — five layers in plain language.
- **Need a principle reference?** [`architecture/principles.md`](architecture/principles.md) lists all 27 principles with captions.
- **Need an operational rule?** [`architecture/operational_rules.md`](architecture/operational_rules.md).
- **Looking up an entity?** [`entities/`](entities/) has per-entity deep dives.
- **Modeling something new?** [`patterns/`](patterns/) has reusable patterns.

## Documentation Map

```
docs/
├── architecture/
│   ├── overview.md              # The five layers, in plain language
│   ├── principles.md            # All 27 principles with captions
│   ├── operational_rules.md     # 5 architectural rules
│   ├── dependency_direction.md  # The One-Way Gate rule
│   └── glossary.md              # Definitions of every concept
│
├── layers/
│   ├── foundation.md            # Layman guide — Foundation layer
│   ├── common.md                # Layman guide — Common sub-layer
│   ├── domain.md                # Layman guide — Domain layer
│   ├── process.md               # Layman guide — Process layer
│   └── application.md           # Layman guide — Application layer
│
├── entities/                    # Per-entity deep dives
│   ├── entity.md
│   ├── person.md
│   ├── organization.md
│   ├── team.md
│   ├── activity.md
│   ├── role.md
│   ├── agreement.md
│   ├── asset.md
│   └── address.md
│
├── patterns/
│   ├── role_based_relationships.md
│   ├── lifecycle_modeling.md
│   ├── natural_keys_and_surrogates.md
│   ├── bitemporal_modeling.md
│   ├── union_ranges.md
│   └── process_versioning.md
│
├── capability_examples/
│   ├── employee_onboarding.md   # Full trace example, prose form
│   ├── order_fulfillment.md
│   ├── vendor_onboarding.md
│   └── incident_resolution.md
│
├── governance/
│   ├── stewardship.md
│   ├── versioning_policy.md
│   ├── change_management.md
│   └── deprecation_policy.md
│
├── integration/
│   ├── mapping_to_application.md
│   ├── bidirectional_mapping_contract.md
│   ├── external_standards.md
│   └── id_strategy.md
│
└── generators/
    ├── json_schema.md
    ├── sql_ddl.md
    ├── python_classes.md
    ├── shacl.md
    ├── owl.md
    └── graphql.md
```
