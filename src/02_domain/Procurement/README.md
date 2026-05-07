# Domain — Procurement

Primary steward for **vendor and supplier-side stable nouns**: vendor
engagements, vendor contracts, purchase requisitions, purchase orders.

## Primary Steward
The Chief Procurement Officer's office.

## Entities
- `VendorRole` (Role) — A Person OR Organization engaged as a vendor.
- `VendorContract` (Agreement) — Master agreement with a supplier.
- `PurchaseOrder` (Agreement) — Specific purchase commitment.
- `PurchaseRequisition` (Entity) — Pre-PO request for goods/services.

## Lifecycle Enums
In `enums/`: VendorLifecycleStateEnum, VendorContractLifecycleStateEnum,
PurchaseOrderLifecycleStateEnum, RequisitionLifecycleStateEnum.

## Notes
- VendorRole uses a union range on `held_by` since vendors can be
  Persons (independent consultants) or Organizations (vendor companies).
- Purchase approval workflow lives in `03_process/PurchaseApproval/`.
