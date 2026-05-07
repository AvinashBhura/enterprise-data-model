# Domain — Facilities

Primary steward for **physical-space stable nouns**: buildings, floors,
rooms, real-estate leases.

## Primary Steward
The Head of Real Estate / Workplace.

## Entities
- `Building` (Asset) — A physical building owned or leased by the enterprise.
- `Floor` (Asset) — A floor within a Building.
- `Room` (Asset) — A specific room (office, conference room, lab).
- `Lease` (Agreement) — A real-estate or equipment lease agreement.

## Lifecycle Enums
In `enums/`: BuildingLifecycleStateEnum, LeaseLifecycleStateEnum.

## Notes
- Buildings have Addresses (via Asset's Addressable mixin).
- Conference room booking and similar workflows are not in this Domain;
  they belong in operational systems (Application layer).
