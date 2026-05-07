# Application — SAP

Vendor-specific projections for **SAP** (ERP — finance + procurement).

## Bidirectional Mapping

| Canonical | SAP | Notes |
|---|---|---|
| `Procurement.VendorRole` | `SAPVendor` | SAP Vendor master |
| `Finance.Invoice` | `SAPInvoice` | SAP AP invoice document |
| `Procurement.PurchaseOrder` | `SAPPurchaseOrder` | SAP PO document |
| `Finance.Account` | `SAPAccount` | SAP G/L account |

## Vendor-Specific Identifiers

- `sap_vendor_number` — SAP vendor master record key (LIFNR)
- `sap_invoice_doc_number` — SAP document number
- `sap_po_number` — SAP purchase order number
- `sap_company_code` — SAP company code (Bukrs)
- `sap_gl_account` — SAP G/L account code

## Sync Notes

SAP is the system of record for finance and procurement transactions.
Sync is largely SAP → EDM for posted transactions.
