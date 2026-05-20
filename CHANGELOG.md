# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0] — Strict-Foundation + Hierarchical Domain

Major architectural refactor. **This is a breaking change** — file paths,
inheritance chains, and slot types changed throughout Domain, Process, and
Application layers. All quality gates pass: 186 schemas valid, 457 imports
upward-only, 38 compliance checks pass, 16 architectural-rule tests pass.

### Foundation expansion

- **Added `Document`** — formal informational artifacts (templates,
  specifications, policies, checklists, definitions). Used by
  OnboardingChecklist, ProcessDefinition, ProcessStep, ProcessTransition,
  RegulatoryObligation, GL Account, OrderLine, PositionHierarchy,
  PurchaseRequisition, and all `*Line` line-item classes.
- **Added `Period`** — defined time intervals with hierarchical containment.
  Used by FiscalPeriod.

Foundation now contains 11 concrete entities anchoring the model.

### Strict-Foundation principle (Closed-Ontology Rule)

`Entity` is now strictly an anchor — only Foundation entities may inherit
directly from it. Every Domain, Process, and Application entity has been
re-anchored to a specific Foundation kind:

| Entity | Old `is_a` | New `is_a` |
|---|---|---|
| `Position` | Entity | Role |
| `PositionHierarchy` | Entity | Document |
| `OnboardingChecklist`, `ChecklistItem` | Entity | Document |
| `CompensationPackage` | Entity | Agreement |
| `Account` (Finance GL) | Entity | Document |
| `Budget` | Entity | Agreement |
| `FiscalPeriod` | Entity | Period |
| `CostCenter` | Entity | OrganizationalUnit |
| `Account` (Sales) | Entity | Asset |
| `Opportunity` | Entity | Activity |
| `OrderLine` | Entity | Document |
| `PurchaseRequisition` | Entity | Document |
| `RegulatoryObligation` | Entity | Document |
| `AccessGrant` | Entity | Agreement |
| `UserAccount` | Entity | Asset |
| `ProcessDefinition` | Entity | Document |
| `ProcessInstance` | Entity | Activity |
| `ProcessTransition` | Entity | Document |
| `ProcessEvent` | Entity | Activity |
| Line-item classes (QuoteLine, InvoiceLine, JournalEntryLine, BudgetLine, PurchaseOrderLine, RequisitionLine, ApprovalThreshold) | (none) | Document |

Enforced by new test:
`tests/architectural_rules/test_entity_inheritance_discipline.py`.

### Hierarchical Domain restructure

Domain layer reorganized into 3-level hierarchy:
`<RootDomain>/<SubDomain>/<DataDomain>/<Entity>.yaml`

The 9 capability-named folders (HumanResources, Finance, Sales, Procurement,
Legal, Security, IT, Facilities, Governance) were renamed to root domains
and decomposed into sub-domains:

- `HR/` — TalentAcquisition, PeopleServices, Compensation, Performance
- `Finance/` — GeneralLedger, AccountsPayable, FinancialPlanning, CostAccounting
- `Sales/` — CustomerManagement, PipelineManagement, OrderManagement
- `Procurement/` — Sourcing, Purchasing
- `Legal/` — Contracts, Compliance, IntellectualProperty
- `Security/` — PhysicalSecurity, LogicalSecurity
- `IT/` — ServiceManagement, AssetManagement, IdentityManagement
- `Facilities/` — RealEstate
- `Governance/` — CorporateGovernance

80 Domain files moved; all imports updated automatically. Placement rules
documented in `docs/architecture/data_domain_organization.md`.

### Process layer reference tightening

- `StepCompletion.completed_by_role` — `string` → `Role` (typed Foundation reference)
- `ProcessEvent.actor_role` — `string` → `Role`

Generic `ProcessInstance.subject_entity_id` remains a string at the base
class for polymorphism; family-specific subclasses can narrow it via
`slot_usage`.

### Business capabilities documentation

New `docs/capabilities/` folder with 10 capability documents covering:
Customer Management, Employee Management, Order Fulfillment, Financial
Accounting, Procurement, Legal & Compliance, Workplace Security, IT
Service Management, Facilities Management, Corporate Governance.

Each capability document lists data domains consumed and processes used —
establishing the conceptual separation between *what the business does*
(capabilities), *what information it maintains* (data domains), and *how
it operationalizes* (processes).

### Operational rules added

Two new operational rules added to `docs/architecture/principles.md`:

- **Strict-Foundation Anchoring (Closed-Ontology Rule)**
- **Typed Cross-Entity References (No-Loose-Strings Rule)**

### Migration

The pre-refactor checkpoint is preserved as
`edm-pre-refactor-checkpoint.zip`. To migrate consuming code:

1. Update Domain import paths (the script
   `migration/v0.5.0_import_rewrite.py` can help)
2. Update inheritance chains in any custom subclasses
3. Replace loose `entity_id` string references with typed slots
4. Re-run `make check` to verify

### Statistics

- Schemas: 184 → 186 (+2 Foundation)
- Classes: 127 → 129 (Document, Period added)
- Imports checked: 442 → 457
- Tests: 14 → 16 (added entity-inheritance discipline tests)
- Domain folders: 10 flat → 9 root + ~25 sub-domains + ~50 data domains
- Files moved: 80
- Inheritance updates: 27 (20 from migration + 7 line-item classes)

---

## [0.4.0] — Batch 4 Complete

### Added — Application Layer (`src/04_application/`)
- `_shared/` — SyncMetadata, SourceSystemReference, SyncStatusEnum.
- `Workday/` — WorkdayPerson, WorkdayEmployeeRole, WorkdayPosition, WorkdayOrganization.
- `Salesforce/` — SalesforceContact, SalesforceAccount, SalesforceOpportunity, SalesforceOrder.
- `SAP/` — SAPVendor, SAPInvoice, SAPPurchaseOrder, SAPAccount.
- `ServiceNow/` — ServiceNowUser, ServiceNowIncident, ServiceNowOnboardingTicket.
- `Okta/` — OktaUser, OktaGroup, OktaUserProvisioningRecord.

### Added — Examples (`examples/`)
- `priya_onboarding/` — full 8-step end-to-end trace through every layer.
- READMEs for vendor_onboarding, reorganization, cross_role_person scenarios.

### Added — Documentation (`docs/`)
- `architecture/overview.md`, `principles.md`, `operational_rules.md`,
  `dependency_direction.md`, `glossary.md`.
- `layers/foundation.md`, `common.md`, `domain.md`, `process.md`, `application.md`.
- `patterns/role_based_relationships.md`, `lifecycle_modeling.md`,
  `natural_keys_and_surrogates.md`, `process_versioning.md`,
  `bitemporal_modeling.md`, `union_ranges.md`.

### Added — Tools (`tools/`)
- `validate_all.py` — schema validity (184 schemas, all clean).
- `check_dependency_direction.py` — One-Way Gate enforcement
  (442 imports verified, all upward).
- `lint_yaml.py` — YAML style/lint.
- `check_principle_compliance.py` — architectural rule compliance
  (38 checks, all passing).
- `diff_schema.py` — version-to-version diff.

### Added — Generators (`generators/`)
- `generate_json_schema.py`, `generate_python_classes.py`, `generate_sql_ddl.py`.
- README documenting the LinkML generator integration.

### Added — Tests (`tests/`)
- `validation/test_schema_validity.py` — every schema parses, has metadata.
- `architectural_rules/test_natural_key_placement.py` — Operational Rule 2.
- `architectural_rules/test_role_immutability.py` — Operational Rule 1.
- `architectural_rules/test_domain_stewardship.py` — Operational Rule 3.
- `architectural_rules/test_process_binding_immutability.py` — Operational Rule 4.
- `architectural_rules/test_codelist_vs_taxonomy_placement.py` — Operational Rule 5.
- `conftest.py` — shared fixtures across the suite.
- 14 tests, all passing.

### Fixed
- Removed enterprise-specific instance data from
  `OrganizationTypeTaxonomy.yaml` description (caught by
  `test_codelist_vs_taxonomy_placement::test_no_specific_instance_data_in_taxonomies`).

## [0.3.0] — Batch 3 Complete

### Added — Process Layer (`src/03_process/`)
- `_core/` — ProcessDefinition, ProcessInstance, ProcessStep,
  StepCompletion, ProcessTransition, ProcessEvent + 4 generic enums.
- 7 process families with Definition + Instance + state enum + README:
  Onboarding, Offboarding, OrderFulfillment, InvoiceApproval,
  PurchaseApproval, IncidentResolution, ContractLifecycle.

## [0.2.0] — Batch 2 Complete

### Added — Domain Layer (`src/02_domain/`)
- 9 capability folders + `_shared/`.
- 55 entity classes across HR, Finance, Sales, Procurement, Legal,
  Security, IT, Facilities, Governance.
- 31 lifecycle and type enums.
- READMEs for every capability documenting steward, scope, entities.

## [0.1.0] — Batch 1 Complete

### Added — Foundation + Common (`src/01_foundation/`)
- 9 concrete entities: Entity, Person, Organization (+ LegalEntity,
  OrganizationalUnit), Team, Role, Activity, Agreement, Asset, Address.
- Common sub-layer with base types, value types, codelists, taxonomies.
- Project scaffolding: README, LICENSE, CONTRIBUTING, pyproject.toml,
  linkml-config.yaml, .gitignore, GitHub Actions workflow.
