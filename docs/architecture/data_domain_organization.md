# Data Domain Organization

> Reference: this document explains how the Domain layer is physically organized
> and the rules for placing new entities. Read alongside `principles.md`.

## Three-Level Hierarchy

The Domain layer (`src/02_domain/`) is organized in three levels:

```
02_domain/
└── <RootDomain>/          ← Level 1: business function (HR, Finance, Sales, ...)
    └── <SubDomain>/       ← Level 2: capability cluster (TalentAcquisition, GeneralLedger, ...)
        └── <DataDomain>/  ← Level 3: data grouping (Employee, Account, Customer, ...)
            ├── <Entity>.yaml
            ├── <Entity>.yaml
            └── enums/
                └── <Enum>.yaml
```

### Level 1: Root Domain

A **root domain** corresponds to a major business function — typically the
top-level capability area in the enterprise capability map.

Current root domains: `HR`, `Finance`, `Sales`, `Procurement`, `Legal`,
`Security`, `IT`, `Facilities`, `Governance`.

A root domain is stewarded by a senior business owner (CHRO for HR, CFO for
Finance, etc.). Adding a new root domain is a significant architectural
decision and should be reviewed by the data architecture committee.

### Level 2: Sub-Domain

A **sub-domain** corresponds to a capability cluster within a business
function — typically aligning with a department, function, or service line.

Examples:
- `HR/TalentAcquisition` — recruiting and hiring
- `HR/PeopleServices` — employee lifecycle management
- `Finance/GeneralLedger` — core accounting
- `Sales/CustomerManagement` — customer relationship management

A sub-domain is stewarded by a functional owner reporting to the root-domain
owner. Sub-domain boundaries are stable but may shift on reorganization.

### Level 3: Data Domain

A **data domain** is a logical grouping of related entities within a sub-domain.
It holds entity schemas plus their supporting enums.

Examples:
- `HR/PeopleServices/Employee/` — EmployeeRole, ContractorRole, AlumniRole, ManagerRole
- `Finance/GeneralLedger/Account/` — Account (GL chart of accounts)
- `Sales/CustomerManagement/Customer/` — Account, CustomerContactRole

A data domain has a data steward responsible for the quality and definitions of
its entities.

## Placement Rules

When deciding where a new entity belongs, follow these rules in order:

### Rule 1 — Single Sub-Domain Home

Every entity has **exactly one** primary sub-domain home. This is its
canonical location and the source of its stewardship. Cross-domain
references happen via import, not by duplicating the entity.

### Rule 2 — Place by Stewardship, Not by Consumer Count

Place an entity in the sub-domain that *stewards* it (defines, evolves,
governs), not necessarily the sub-domain with the most consumers.

Example: `Customer` is consumed by Sales, Marketing, Customer Service, and
Billing — but is stewarded by Sales (specifically, `Sales/CustomerManagement`).
That's its home; others import.

### Rule 3 — Prefer Specificity When Sub-Domains Overlap

When two sub-domains both touch an entity, place it under the more specific
one. Example: an `Onboarding` entity could plausibly live under TA (which
initiates onboarding) or PeopleServices (which executes it). Because
PeopleServices is the steward, place it there.

### Rule 4 — Cross-Cutting Goes to `_shared/`

Entities used across multiple sub-domains within a root domain go to that
root's `_shared/` folder (e.g., `02_domain/HR/_shared/`).

Entities used across multiple root domains go to the top-level
`02_domain/_shared/` folder.

Example: `LegalEntityReference` (used across HR, Finance, Legal, Sales) lives
in `02_domain/_shared/`.

### Rule 5 — Don't Create One-Entity Sub-Domains Speculatively

A sub-domain with only one data domain inside it is acceptable only when
the sub-domain is a real organizational unit. Don't invent sub-domains to
hold a single entity.

### Rule 6 — Enum and Code Lists Live with Their Owning Entity

Lifecycle enums and entity-specific code lists go in the `enums/` folder
*inside* their data domain, not in a separate top-level enums folder.

Domain-wide or industry-standard taxonomies/codelists live in
`src/01_foundation/common/codelists/` or `taxonomies/`.

## Capabilities Are Documented Separately

Business **capabilities** (e.g., "Customer Management", "Employee Onboarding")
are not directly modeled in the Domain layer. They are documented in
`docs/capabilities/`. Each capability document lists:

- The data domains it consumes
- The processes that operationalize it
- The primary steward organization

This separation reflects the fact that capabilities are *what the business
does* while data domains are *what information the business maintains*.
A single capability typically consumes multiple data domains; a single
data domain is consumed by multiple capabilities.

## Example: A New Entity Walkthrough

You want to add a `Certification` entity (employee certifications and
training credentials).

1. **What is it?** A formal record of an employee's earned credential.
2. **Who stewards it?** HR — specifically, Learning & Development (if that
   sub-domain exists) or PeopleServices (if not).
3. **Place it**: If L&D sub-domain doesn't exist yet, create
   `HR/LearningAndDevelopment/Certification/` (Rule 5 says we don't invent
   speculative sub-domains, but L&D is a real org unit). Otherwise place
   under existing PeopleServices.
4. **What does it inherit from?** Likely `is_a: Document` (a credential
   certificate is a documented record).
5. **References**: typed slot to EmployeeRole for who holds it.

If usage later expands beyond HR (e.g., Finance tracks CFO certifications),
keep it in HR and have Finance import.

## Process and Application Layers — Different Organization

The Domain layer is the only layer using this 3-level hierarchy.

- **Process layer** (`src/03_process/`) is flat — organized by process family
  (Onboarding, OrderFulfillment, InvoiceApproval, etc.). Process families
  align with capabilities, not sub-domains.
- **Application layer** (`src/04_application/`) is organized by **vendor**
  (Workday, Salesforce, SAP, ServiceNow, Okta). Vendor is its own
  organizing dimension.

This asymmetry is intentional: Domain has many entities and benefits from
hierarchy; Process and Application have fewer items at each level and stay
flat for simpler navigation.
