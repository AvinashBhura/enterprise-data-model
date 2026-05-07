# Application Layer

The Application layer holds **system-specific projections** of Domain
and Process entities. Each vendor system has its own folder containing
entity classes that inherit from the canonical Domain/Process entities
and add vendor-specific identifiers and quirks.

## Principles

| # | Principle | Caption |
|---|---|---|
| 1 | Inheritance-Only Extension | **The Extender Principle** — add fields to the canonical shape; never change its meaning |
| 2 | Adaptability | **The Shapeshifter Principle** — changes at the pace of the software that produces the data |
| 3 | Source-System Transparency | **The Fingerprint Principle** — every Application entity names its source system |
| 4 | Bidirectional Mapping | **The Contract Principle** — every projection documents its transformation to and from the canonical shape |
| 5 | No Upstream Pollution | **The One-Way Gate Principle** — Foundation, Common, Domain, and Process never import from Application |

## Folder Layout

```
04_application/
├── Workday/         # HR system of record
├── Salesforce/      # CRM
├── SAP/             # ERP — finance + procurement
├── ServiceNow/      # IT service management
├── Okta/            # Identity and access management
└── _shared/         # Cross-application shared structures (sync metadata)
```

## Naming Convention

Application classes are prefixed with the vendor name:
`WorkdayEmployeeRole`, `SalesforceContact`, `ServiceNowIncident`,
`OktaUser`, `SAPInvoice`. This makes the source system visible at the
type level and prevents accidental confusion with canonical entities.

## Operational Rule — Natural Key Placement

Vendor system natural keys (workday_worker_id, sf_contact_id, etc.)
live ONLY on Application-layer subclasses, never on canonical Domain
entities. This keeps Domain vendor-neutral.

## Adding a New System

To add a new system:
1. Create a vendor folder under `04_application/`.
2. For each canonical entity the system touches, create a `Vendor*` subclass
   that inherits from the Domain/Process entity.
3. Add vendor-specific natural keys (e.g., `vendor_id`).
4. Add `last_synced_at` and `sync_status` for sync tracking.
5. Document the bidirectional mapping in the vendor folder's README.
6. Never modify any file outside `04_application/`.
