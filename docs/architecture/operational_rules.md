# Operational Rules

Five enforceable rules that turn the principles into concrete behaviors.
These are checked by the tooling in `tools/` and tested in
`tests/architectural_rules/`.

## Rule 1 — Role Immutability

> Roles do not mutate their core terms once effective. Changes to
> `employing_organization`, `primary_position`, or `employment_type`
> end the current Role (set `effective_to`) and begin a new one.

**Why:** preserves accurate history. A reorg or position change is
a new engagement, not an edit. A single Person may accumulate dozens
of Role records over a career — that is correct, not bloat.

**Anti-pattern:** mutating `employing_organization` on an existing
EmployeeRole when an employee transfers between divisions. The
correct action is to end the existing Role and create a new one.

**Test:** `tests/architectural_rules/test_role_immutability.py`

## Rule 2 — Natural Key Placement

> Enterprise-native natural keys live on canonical entities via
> `Identifiable.natural_identifiers`. Vendor system keys live ONLY on
> Application-layer subclasses.

**Why:** keeps Domain vendor-neutral. When a vendor system migrates,
Domain entities stay unchanged.

**Anti-pattern:** adding `workday_worker_id` as an attribute on the
canonical `EmployeeRole` in `02_domain/HumanResources/`. The correct
location is `WorkdayEmployeeRole` in `04_application/Workday/`.

**Test:** `tests/architectural_rules/test_natural_key_placement.py`

## Rule 3 — Domain Primary Stewardship

> Every Domain entity has a single primary-steward capability and lives
> in that capability's folder. Cross-cutting entities with no single
> steward live in `02_domain/_shared/`. Specific instances (e.g., Acme's
> actual Engineering Division) are master data, not part of `src/`.

**Why:** clear ownership. No replication of similar entities across
capabilities.

**Anti-pattern:** copying `Position` into both `HumanResources/` and
`Sales/` because both reference it. Sales should reference HR's `Position`.

**Test:** `tests/architectural_rules/test_domain_stewardship.py`

## Rule 4 — Process Binding Immutability

> A ProcessInstance's binding to a ProcessDefinition is set at instance
> creation and NEVER changes. Process migrations are modeled as
> termination of the old instance (state → MIGRATED) and creation of
> a new instance with explicitly carried-over state.

**Why:** reproducibility and audit. An instance's behavior must always
be explainable by reference to a single, immutable definition version.

**Anti-pattern:** updating an existing OnboardingProcessInstance's
`definition` field from v3.2 to v4.0 mid-flight.

**Test:** `tests/architectural_rules/test_process_binding_immutability.py`

## Rule 5 — Codelist vs Taxonomy vs Instance Data

> - **Code Lists** hold flat, closed vocabularies (no hierarchy).
> - **Taxonomies** hold abstract hierarchical classifications (categories
>   and their containment, not specific instances).
> - **Instance Data** (specific records like Acme's actual divisions)
>   lives in Domain or master data — never in Common.

**Why:** keeps Common reusable across enterprises. The Reusability Test:
*would another enterprise with a different business need this exact
construct?* If yes → Common-worthy. If no → instance data.

**Anti-pattern:** creating a `taxonomies/AcmeOrgChart.yaml` with
specific Acme departments. The OrganizationTypeTaxonomy belongs there
(abstract category hierarchy); Acme's specific divisions belong in HR
domain master data.

**Test:** `tests/architectural_rules/test_codelist_vs_taxonomy_placement.py`

---

## Enforcement Summary

| Rule | Tool | Test |
|---|---|---|
| Role Immutability | (manual review + lint) | architectural_rules/test_role_immutability.py |
| Natural Key Placement | tools/check_natural_key_placement.py | architectural_rules/test_natural_key_placement.py |
| Domain Stewardship | tools/check_dependency_direction.py | architectural_rules/test_domain_stewardship.py |
| Process Binding Immutability | (instance-level — runtime check) | architectural_rules/test_process_binding_immutability.py |
| Codelist vs Taxonomy vs Instance | tools/check_principle_compliance.py | architectural_rules/test_codelist_vs_taxonomy_placement.py |
