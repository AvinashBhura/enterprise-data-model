# Layman's Guide — Application Layer

## What it is in one sentence

The system-specific projections of Domain and Process entities — with
vendor quirks, system identifiers, and integration-specific fields —
that represent how individual software applications hold the
enterprise's data.

## Why it matters

Workday, ServiceNow, Salesforce, and SAP each have their own
representation of "an employee," with their own identifiers and field
names. If you let those vendor quirks creep up into Domain, Domain
stops being canonical — it becomes Workday's shape wearing a disguise.

The Application layer gives each vendor its own dedicated space.
`WorkdayEmployeeRole` holds the Workday worker ID and Workday's
supervisory organization concept. `ServiceNowUser` holds the
ServiceNow user reference. Neither contaminates the clean Domain
`EmployeeRole`.

## A real-world example

When your company migrates from Workday to a new HR system:
1. Foundation: **no change**.
2. Common, Domain, Process: **no change**.
3. Application: Workday folder retires; new vendor folder appears.

If a vendor migration forces Domain changes, the architecture is
leaking. The Application layer is what keeps that leak sealed.

## The Five Vendor Folders + _shared

| Folder | System | Notable Projections |
|---|---|---|
| `Workday/` | HR system of record | WorkdayPerson, WorkdayEmployeeRole, WorkdayPosition, WorkdayOrganization |
| `Salesforce/` | CRM | SalesforceContact, SalesforceAccount, SalesforceOpportunity, SalesforceOrder |
| `SAP/` | ERP (finance + procurement) | SAPVendor, SAPInvoice, SAPPurchaseOrder, SAPAccount |
| `ServiceNow/` | IT service management | ServiceNowUser, ServiceNowIncident, ServiceNowOnboardingTicket |
| `Okta/` | Identity & access | OktaUser, OktaGroup, OktaUserProvisioningRecord |
| `_shared/` | Common sync infrastructure | SyncMetadata, SourceSystemReference, SyncStatusEnum |

## Why this layer is allowed to change constantly

Application-layer volatility is **expected and healthy**. Vendors
change schemas. Integrations add fields. The Application layer absorbs
all of that, leaving everything underneath stable. Churn here isn't a
design flaw — it's the whole point.

## The Five Application principles

1. **Extender** — Add fields to canonical shape; never change meaning.
2. **Shapeshifter** — Changes at the pace of the software that produces the data.
3. **Fingerprint** — Every Application entity names its source system.
4. **Contract** — Every projection documents bidirectional mapping.
5. **One-Way Gate** — Foundation, Common, Domain, Process never import from Application.

## Adding a New System

To add a new system (say, BambooHR):
1. Create `04_application/BambooHR/`.
2. For each canonical entity the system touches, create a `BambooHR*` subclass.
3. Add vendor-specific natural keys.
4. Embed `SyncMetadata` for sync tracking.
5. Document bidirectional mapping in the folder README.
6. **Never modify any file outside `04_application/`.**

## See also

- Application principles: `docs/architecture/principles.md`
- Worked example with applications: `examples/priya_onboarding/`
