# Domain — Sales

Primary steward for **customer-facing stable nouns**: customer accounts,
opportunities, quotes, orders.

## Primary Steward
The Chief Revenue Officer's office.

## Entities
- `CustomerContactRole` (Role) — A Person acting as contact at a customer Organization.
- `Account` (Entity) — A customer account (the company-level relationship).
- `Opportunity` (Entity) — A sales pursuit.
- `Quote` (Agreement) — Pre-order pricing proposal.
- `Order` (Agreement) — Confirmed customer purchase commitment.
- `OrderLine` (Entity) — Line item on an Order.

## Lifecycle Enums
In `enums/`: AccountLifecycleStateEnum, OpportunityLifecycleStateEnum,
QuoteLifecycleStateEnum, OrderLifecycleStateEnum.

## Notes
- Sales `Account` is distinct from Finance `Account`. Both inherit
  Foundation's `Entity` directly; cross-references use `entity_id`.
- Order fulfillment workflow lives in `03_process/OrderFulfillment/`.
