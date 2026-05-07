# Application — Salesforce

Vendor-specific projections for **Salesforce** (CRM).

## Bidirectional Mapping

| Canonical | Salesforce | Notes |
|---|---|---|
| `Foundation.Person` (via `Sales.CustomerContactRole`) | `SalesforceContact` | Salesforce Contact |
| `Foundation.Organization` (via `Sales.Account`) | `SalesforceAccount` | Salesforce Account |
| `Sales.Opportunity` | `SalesforceOpportunity` | Salesforce Opportunity |
| `Sales.Order` | `SalesforceOrder` | Salesforce Order |

## Vendor-Specific Identifiers

- `sf_contact_id`, `sf_account_id`, `sf_opportunity_id`, `sf_order_id` —
  18-character Salesforce IDs
- `sf_record_url` — direct deep links

## Sync Notes

Salesforce is the system of record for sales-pursuit data. Sync direction
is bidirectional but Salesforce typically wins for sales-specific
attributes; canonical Sales Account is updated via Salesforce events.
