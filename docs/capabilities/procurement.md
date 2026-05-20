# Capability: Procurement

**Description**: The enterprise's ability to identify, contract with, and
purchase from external suppliers of goods and services.

**Primary Steward**: Chief Procurement Officer

**Maturity**: Established

## Data Domains Consumed

- `src/02_domain/Procurement/Sourcing/Vendor/` — VendorRole, VendorContract
- `src/02_domain/Procurement/Purchasing/PurchaseOrder/` — PurchaseOrder, PurchaseOrderLine
- `src/02_domain/Procurement/Purchasing/PurchaseRequisition/` — PurchaseRequisition, RequisitionLine
- `src/02_domain/Finance/AccountsPayable/Invoice/` — Invoice (AP invoice from vendor)

## Processes Used

- `src/03_process/PurchaseApproval/` — Purchase approval workflow

## Related Capabilities

- Financial Accounting (downstream — AP)
- Legal Contracts (upstream — vendor agreements)
