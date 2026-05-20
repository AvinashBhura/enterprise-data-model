# Claude Code Orientation

This file is for **Claude Code**. It explains what this project is, how it's
organized, and the rules to respect when modifying it.

## What This Project Is

A **layered, LinkML-based Enterprise Data Model** (EDM). It's a reference
data architecture organized in five layers, with strict rules about how
the layers depend on each other.

The deliverable is the *architecture itself* — the structure, the rules,
the operational checks. The specific entity instances (Person, Account,
Invoice, etc.) are illustrative; the value is in the layering and the
discipline that produces stability over time.

## Quick Start

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Verify everything is healthy (run after every meaningful change)
make check

# Or run the four checks individually:
python tools/validate_all.py            # 186 schemas parse cleanly
python tools/check_dependency_direction.py  # 457 imports flow upward
python tools/check_principle_compliance.py  # 38 architectural rules
pytest tests/                           # 16 tests
```

If any of those four fail, **do not proceed** until they pass.

## Architecture in One Picture

```
┌──────────────────────────────────────────────────────────────┐
│ 5. APPLICATION    src/04_application/    vendor projections   │
│                   organized by vendor (Workday, SAP, ...)     │
├──────────────────────────────────────────────────────────────┤
│ 4. PROCESS        src/03_process/        workflows + instances│
│                   organized by process family (Onboarding, ...│
├──────────────────────────────────────────────────────────────┤
│ 3. DOMAIN         src/02_domain/         capability nouns     │
│                   3-level hierarchy:                          │
│                   <Root>/<SubDomain>/<DataDomain>/Entity.yaml │
│                   e.g., HR/PeopleServices/Employee/...        │
├──────────────────────────────────────────────────────────────┤
│ 2. COMMON         src/01_foundation/common/   toolkit         │
├──────────────────────────────────────────────────────────────┤
│ 1. FOUNDATION     src/01_foundation/    permanent concepts    │
│                   Entity (anchor) + 10 concrete kinds:        │
│                   Person, Organization, Team, Role, Activity, │
│                   Agreement, Asset, Address, Document, Period │
└──────────────────────────────────────────────────────────────┘
```

**Dependencies flow upward only.** This is the single most important
rule. A schema in a lower layer must NEVER import from a higher layer.

For the full architecture story, read `docs/architecture/overview.md`.
For Domain layer organization rules, read
`docs/architecture/data_domain_organization.md`.
For business capabilities (separate from data domains), read
`docs/capabilities/`.

## Operational Rules (Non-Negotiable)

These are documented in `docs/architecture/operational_rules.md` and
enforced by tests in `tests/architectural_rules/`. Read them before
making changes.

1. **Role Immutability** — A Role's core terms don't mutate. Changes
   end the current Role and begin a new one.
2. **Natural Key Placement** — Vendor system keys live ONLY on
   Application-layer subclasses. Domain stays vendor-neutral.
3. **Domain Primary Stewardship** — Each Domain entity has exactly
   one steward capability. No replication.
4. **Process Binding Immutability** — A ProcessInstance's binding to
   a ProcessDefinition is set at creation and never changes.
5. **Codelist vs Taxonomy vs Instance Data** — Codelists are flat;
   taxonomies are hierarchical; specific instances belong in Domain
   master data, not Common.
6. **Strict-Foundation Anchoring (v0.5.0+)** — Only Foundation entities
   directly specialize `Entity`. Every Domain, Process, and Application
   entity must specialize a more specific Foundation kind (Person,
   Organization, Role, Activity, Agreement, Asset, Address, Document,
   Period, or one of their subtypes). Enforced by
   `tests/architectural_rules/test_entity_inheritance_discipline.py`.
7. **Typed Cross-Entity References (v0.5.0+)** — References between EDM
   entities must be typed slots (range a target entity), not loose
   `entity_id` strings. Exception: generic ProcessInstance.subject_entity_id
   on the base class, which family-specific subclasses narrow via
   `slot_usage`.

## Twenty-Seven Principles

Documented in `docs/architecture/principles.md`. Each has a one-phrase
caption (Highlander, Boring, Borrower, Frozen-Contract, etc.). When in
doubt about a design choice, the principles are the tiebreaker.

## File Conventions

### LinkML Schema Files (`src/**/*.yaml`)

Every schema file MUST have:
```yaml
id: https://example.org/edm/<layer>/<...>/SchemaName
name: <snake_case_unique_name>
title: "<Layer> — <SchemaName>"
description: <multi-line prose explanation>

license: Apache-2.0
version: 0.1.0

prefixes:
  linkml: https://w3id.org/linkml/
  edm: https://example.org/edm/

default_prefix: edm
default_range: string

imports:
  - linkml:types
  - <relative paths to other EDM schemas>

# Then: classes / enums / types
```

### Imports

- Imports use **relative paths** without the `.yaml` extension.
- Imports MUST point to the same layer or a **lower** layer. Never higher.
- The dependency-direction tool (`tools/check_dependency_direction.py`)
  enforces this.

### Naming

- **Classes** are `PascalCase`.
- **Slot/attribute names** are `snake_case`.
- **Enum names** end in `...Enum`.
- **Mixin/base type classes** end in `-able` (`Identifiable`,
  `Lifecycleable`) or are descriptive nouns (`RoleHolder`, `Temporal`).
- **Application-layer classes** are prefixed with the vendor name:
  `WorkdayEmployeeRole`, `SalesforceContact`, `ServiceNowIncident`.

### Per-Layer Folder Conventions

- Each capability/family folder has a `README.md` explaining steward,
  scope, entities, and notable decisions.
- Each capability has `enums/` for its lifecycle and type enums.
- Lifecycle state enums are **per-entity**, not shared across entities
  (Operational Rule decision in our architecture discussion).

## Where Things Live

| If you need to... | Look in... |
|---|---|
| Add a new permanent enterprise concept (rare!) | `src/01_foundation/` (review with steward first) |
| Add a new value type or codelist | `src/01_foundation/common/{base,codelists,taxonomies}/` |
| Add a new capability noun | `src/02_domain/<Capability>/` |
| Add a new process family | `src/03_process/<FamilyName>/` |
| Add a new vendor projection | `src/04_application/<Vendor>/` |
| Document a pattern | `docs/patterns/` |
| Look up an entity's deep dive | `docs/entities/` (skeleton only — extend as needed) |
| Run a worked example | `examples/priya_onboarding/` |

## What NOT To Do

- **DO NOT** add a downward import (e.g., a Foundation file importing
  from Domain). The dependency direction check will fail.
- **DO NOT** put vendor-specific identifiers (workday_*, sf_*, snow_*,
  sap_*, okta_*) on canonical Domain entities. They go in Application.
- **DO NOT** put workflow state (current_step, is_approved) on Domain
  entities. Workflow state lives on ProcessInstances.
- **DO NOT** mutate a `ProcessInstance.definition` reference once
  created. Migrate by creating a new instance.
- **DO NOT** put enterprise-specific instance data (named departments,
  named roles like "Acme CTO") in `src/01_foundation/common/`. Those
  belong in Domain master data.
- **DO NOT** copy an entity into multiple capability folders. Pick a
  primary steward; have the other capabilities reference it.
- **DO NOT** ship code that fails any of the four checks (`make check`).

## Common Tasks

### Adding a new entity to a capability

1. Choose the right capability folder under `src/02_domain/`.
2. Create the YAML schema file. Match the metadata template above.
3. Inherit from a Foundation entity (Entity, Person, Organization,
   Role, Activity, Agreement, Asset, Address) or a more-specific Domain
   entity in the same capability.
4. Add lifecycle enum under `<capability>/enums/` if needed.
5. Update the capability's `README.md` to mention the new entity.
6. Run `make check`.

### Adding a new vendor projection

1. Create `src/04_application/<VendorName>/` with subfolder `enums/`.
2. Add a `README.md` documenting the bidirectional mapping.
3. For each canonical entity the vendor touches, create a `<Vendor><Entity>.yaml`
   that inherits from the canonical entity.
4. Add vendor-specific natural keys (e.g., `vendor_record_id`).
5. Embed `SyncMetadata` from `04_application/_shared/`.
6. NEVER modify any file outside `src/04_application/<VendorName>/`.
7. Run `make check`.

### Adding a new process family

1. Create `src/03_process/<FamilyName>/` with subfolder `enums/`.
2. Add `README.md` describing what the workflow does and what Domain
   entity it operates on.
3. Create `<Family>ProcessDefinition.yaml` (is_a `ProcessDefinition`).
4. Create `<Family>ProcessInstance.yaml` (is_a `ProcessInstance`).
5. Create `<Family>StateEnum.yaml` for fine-grained workflow state.
6. Run `make check`.

## Documentation Map

```
docs/
├── architecture/
│   ├── overview.md             # READ FIRST
│   ├── principles.md           # All 27 principles
│   ├── operational_rules.md    # The 5 rules
│   ├── dependency_direction.md # The One-Way Gate rule
│   └── glossary.md
├── layers/                     # Layman's guide for each layer
└── patterns/                   # Reusable modeling patterns
```

## Key Files for Onboarding

If you've just opened this project, read in this order:
1. `README.md` — what this is, at a glance
2. `docs/architecture/overview.md` — the five layers explained
3. `docs/architecture/principles.md` — the 27 captioned principles
4. `docs/architecture/operational_rules.md` — the 5 hard rules
5. `examples/priya_onboarding/README.md` — concrete end-to-end example
6. Pick one capability and read its README + a couple of entities

## Verification Loop

Every meaningful change should run:
```bash
make check
```

Which is equivalent to:
```bash
python tools/validate_all.py && \
python tools/check_dependency_direction.py && \
python tools/check_principle_compliance.py && \
pytest tests/
```

If you've changed schemas, this is non-negotiable. If you've only
edited docs or READMEs, you can skip — but it's quick (~1 second), so
just run it.

## Project Status

The project is **complete and validated** as of v0.4.0 (Batch 4).
- 184 LinkML schemas, 127 classes, 68 enums, 2 types
- 4 layers, 9 Domain capabilities, 7 Process families, 5 vendor folders
- Full architectural rule enforcement
- 14 passing tests
- All 4 quality gates green

Future work likely includes:
- Per-entity deep-dive docs in `docs/entities/`
- More example fixtures (vendor_onboarding, reorganization, cross_role_person have READMEs but no fixture data yet)
- Additional generators (SHACL, OWL, GraphQL)
- More architectural rule tests
- Per-capability example docs in `docs/capability_examples/`

## Contact

This project was built collaboratively as a reference architecture.
Treat it as a starting point — adapt to your enterprise's specifics
while preserving the structure, the rules, and the discipline.
