# Example — Vendor Onboarding

Acme engages CloudServices LLC as a vendor for cloud infrastructure
services.

## Scenario

1. CloudServices LLC's authorized signatory (a Person) and the company
   itself (an Organization → LegalEntity) are recorded.
2. A VendorRole is created — `held_by: Organization` (CloudServices LLC).
3. A VendorContract Agreement is signed.
4. A VendorOnboarding ProcessInstance runs through qualification,
   compliance checks, and supplier-portal provisioning.
5. SAP Application-layer projection (SAPVendor) created with
   sap_vendor_number.

## Architectural Demonstrations

- **Union range on held_by**: VendorRole's `held_by` accepts either a
  Person or Organization. Here it points to an Organization.
- **Cross-domain references**: VendorRole (Procurement) references
  Foundation Organization; VendorContract (Procurement) references
  the Agreement structure from Foundation.

## Files

(Sample fixtures to be added — follows the same numbered-file pattern
as `priya_onboarding/`.)
