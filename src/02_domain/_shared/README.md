# Domain — _shared

Cross-capability domain entities that genuinely have no single primary
steward. Per the **Single Owner Principle** (Domain principle 6), most
entities live with their primary-steward capability — but a small number
of entities are legitimately shared across multiple capabilities with
no single owner. Those live here.

## When to place an entity here

Apply this test:
1. Does the entity have a clear primary-steward capability? → Place it there.
2. Are multiple capabilities equal stakeholders with shared accountability? → Place it here.
3. Is it instance-data (e.g., a specific org chart)? → Not here, not anywhere in `src/`. That's master data.

## Entities currently here

- `LegalEntityReference.yaml` — A view of LegalEntity used uniformly
  across multiple capabilities (Finance, Legal, Procurement) when none
  alone is the steward.

## Stewardship

`_shared/` entities are governed by the **EDM Steering Committee** —
changes here require approval from steering rather than a single
domain steward.
