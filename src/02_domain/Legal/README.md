# Domain — Legal

Primary steward for **legal stable nouns**: NDAs, licensing agreements,
regulatory obligations, intellectual-property assets.

## Primary Steward
The Chief Legal Officer's office.

## Entities
- `NDA` (Agreement) — Non-disclosure agreement.
- `LicensingAgreement` (Agreement) — Software/IP licensing agreement.
- `RegulatoryObligation` (Entity) — Specific compliance obligation.
- `IntellectualPropertyAsset` (Asset) — Patents, trademarks, copyrights.

## Lifecycle Enums
In `enums/`: NDALifecycleStateEnum, LicenseLifecycleStateEnum,
RegulatoryObligationLifecycleStateEnum, IPAssetLifecycleStateEnum.

## Notes
- Contract lifecycle workflow lives in `03_process/ContractLifecycle/`.
- Cross-references with Procurement (vendor contracts) — Procurement
  is the primary steward for vendor contracts; Legal contributes
  approval and review.
