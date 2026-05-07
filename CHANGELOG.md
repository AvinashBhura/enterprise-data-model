# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
