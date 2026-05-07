# EDM Glossary

Definitions of every concept used in the Enterprise Data Model.

## Core Concepts

**Application Layer** — Layer 5. Holds vendor-specific projections
(Workday, Salesforce, SAP, ServiceNow, Okta).

**Base Type** — A reusable structural construct in Common applied to
entities via composition. Examples: `Identifiable`, `Lifecycleable`,
`Addressable`, `RoleHolder`, `Classifiable`, `Temporal`.

**Capability** — *What* the business can do. A noun-phrase. Modeled in
the Domain layer. Distinct from Process (*how* it's executed).

**Codelist** — A flat, closed enumeration of permissible values. No
hierarchy. Examples: `CurrencyCodeEnum`, `RoleTypeEnum`.

**Common Sub-Layer** — Nested under Foundation. Holds reusable
construction material: base types, value types, codelists, taxonomies.

**Domain Layer** — Layer 3. Capability-aligned stable nouns. Each
business function (HR, Finance, Sales, etc.) owns its piece.

**EDM** — Enterprise Data Model. This project.

**Entity** — The semantic anchor of the EDM. Concrete, minimal class
from which Foundation entities inherit to declare semantic membership.

**Entity ID** — The globally unique surrogate identifier (UUID) every
Entity carries. Stable across all systems, reorganizations, integrations.

**Foundation Layer** — Layer 1. Permanent enterprise concepts:
Person, Organization, Team, Activity, Role, Agreement, Asset, Address.

**LinkML** — Linked data Modeling Language. The schema language used
to express the EDM. See https://linkml.io.

**Mixin** — LinkML mechanism for composition. The EDM uses mixins to
implement Base Types. Documented as "Base Types" outside YAML to keep
architecture vocabulary tool-agnostic.

**Natural Identifier** — A business key (e.g., employee_number,
tax_id, vendor_number). Lives on canonical entities via `Identifiable`
when enterprise-issued, or on Application subclasses when vendor-issued.

**Process Definition** — A versioned workflow specification. Multiple
versions may coexist; instances bind to a single version for life.

**Process Instance** — A live execution of a Process Definition. Bound
immutably to a single definition version (Frozen-Contract principle).

**Process Layer** — Layer 4. Workflows and instances. References Domain
entities; never modifies them (Borrower principle).

**Role** — A time-bound engagement of a Person or Organization with
another party. The universal pivot for "who plays what with whom"
relationships. Specialized in Domain (EmployeeRole, VendorRole, etc.).

**Source-System Reference** — Pattern in Application layer: every
projection records its source system identity for round-trip mapping.

**Subject Entity** — The Domain-layer entity a ProcessInstance
operates on. Captured by `subject_entity_id` + `subject_entity_type`.

**Surrogate Key** — System-generated identifier (UUID) that never
changes. Distinct from natural keys (business identifiers that may
change). Both coexist in the EDM.

**Taxonomy** — An abstract hierarchical classification (categories
and their containment, not specific instances). Examples:
`OrganizationTypeTaxonomy`, `AssetTypeTaxonomy`.

**Value Type** — A self-contained composite value structure with no
independent identity. Examples: `AmountType` (value+currency),
`QuantityType` (value+unit), `DocumentType`.

## Lifecycle Concepts

**Lifecycle State** — Coarse entity-level state (Active, Inactive,
Archived, etc.). Lives on entities via the `Lifecycleable` base type.
Distinct from process workflow state.

**State Transition** — A recorded change from one lifecycle state to
another. Stored in `state_history` on Lifecycleable entities.

**Workflow State** — Fine-grained state managed by ProcessInstance.
Distinct from entity-level lifecycle state.

## Architectural Concepts

**Bounded Context** — A capability's "turf" — the set of entities it
owns and is the primary steward for.

**Borrower Principle** — Process references Domain; Process never
modifies Domain.

**Capability-Centricity** — Domain models capabilities (what the
business is) rather than processes (how it runs).

**Frozen-Contract** — A ProcessInstance's binding to a definition
version is set at instance creation and never changes.

**Highlander Principle** — There can be only one. Each concept
exists once across the enterprise.

**One-Way Gate** — Dependencies flow upward only. Foundation knows
nothing of Application.

**Operational Rule** — An enforceable constraint backed by tooling
and tests. Distinct from a principle (aspirational).

**Primary Stewardship** — Each Domain entity has exactly one
primary-steward capability that owns it.

**Reusability Test** — Before placing anything in Common, ask:
"Would another enterprise with a different business need this?"

**Role Immutability** — Roles do not mutate core terms. Changes end
one Role and begin another, preserving history.

**Single Owner Principle** — See Primary Stewardship.

**Snapshot Principle** — Every ProcessDefinition is versioned;
instances bind to a snapshot.
