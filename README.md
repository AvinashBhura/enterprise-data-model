# Enterprise Data Model (EDM)

A layered, LinkML-based Enterprise Data Model implementing a "model once,
use everywhere" approach. The EDM is designed to provide a stable,
canonical representation of enterprise concepts that every system,
report, and integration can rely on.

> **Working with Claude Code?** Read `CLAUDE.md` first. It explains the
> file conventions, the operational rules, and the verification loop
> Claude Code should run after every change.

## Quick Start

```bash
make install   # install dev dependencies
make check     # run all four quality gates
make help      # see all available commands
```

## Architecture

Five layers, stacked from most stable (bottom) to most volatile (top),
with dependencies flowing **upward only**:

```
┌────────────────────────────────────────────────────────────┐
│ 5. APPLICATION     system-specific projections             │
├────────────────────────────────────────────────────────────┤
│ 4. PROCESS         workflows and instances                 │
├────────────────────────────────────────────────────────────┤
│ 3. DOMAIN          capability-aligned stable nouns         │
├────────────────────────────────────────────────────────────┤
│ 2. COMMON          shared construction material            │
│   (nested inside Foundation)                               │
├────────────────────────────────────────────────────────────┤
│ 1. FOUNDATION      permanent enterprise concepts           │
└────────────────────────────────────────────────────────────┘
```

**The One-Way Gate rule**: Foundation depends on nothing. Domain depends
on Foundation and Common. Process depends on Foundation, Common, and
Domain. Application depends on everything below it — and **nothing
below Application imports from it**.

## Directory Structure

```
enterprise-data-model/
├── src/
│   ├── 01_foundation/       # permanent enterprise concepts
│   │   ├── Entity.yaml      # semantic anchor
│   │   ├── Person.yaml      # ... + 7 more Foundation entities
│   │   └── common/          # shared construction material (base types, codelists, taxonomies)
│   ├── 02_domain/           # capability-aligned stable nouns
│   │   ├── HumanResources/
│   │   ├── Finance/
│   │   └── ... (7 more capabilities + _shared)
│   ├── 03_process/          # workflows and process instances
│   │   ├── _core/
│   │   ├── Onboarding/
│   │   └── ... (6 more process families)
│   └── 04_application/      # system-specific projections
│       ├── Workday/
│       ├── Salesforce/
│       └── ... (3 more systems + _shared)
├── tests/                   # validation, fixtures, architectural rules
├── docs/                    # architecture, layer guides, entity deep-dives
├── generators/              # LinkML → downstream artifact generators
├── tools/                   # quality tooling (validation, linting, compliance)
└── examples/                # runnable end-to-end scenarios
```

## Layer Principles Summary

| Layer | Principle Captions |
|---|---|
| **Foundation** | Highlander · Boring · Independence · Common Language · Spartan · Noun · Origin |
| **Common** | One-Meaning · Shared-Shelf · Rosetta · Scaffolding · Clean-Contract |
| **Domain** | Inheritance · What-Not-How · Fence · Thing · Who-Plays-What · Single Owner |
| **Process** | Borrower · Snapshot · Ledger · Frozen-Contract |
| **Application** | Extender · Shapeshifter · Fingerprint · Contract · One-Way Gate |

Full explanations in [`docs/architecture/principles.md`](docs/architecture/principles.md).

## Operational Rules

1. **Role Immutability** — Roles don't mutate core terms. Changes end one Role, start another.
2. **Natural Key Placement** — Enterprise-native keys on canonical entities via `Identifiable`; vendor keys on Application subclasses.
3. **Domain Primary Stewardship** — Entities live with their primary-steward domain.
4. **Process Binding Immutability** — Instance-to-Definition bindings are set at birth, never mutated.
5. **Codelist vs Taxonomy vs Instance Data** — Flat enums in codelists; abstract hierarchies in taxonomies; specific records in Domain.

## Getting Started

### Prerequisites

- Python 3.11+
- [LinkML](https://linkml.io/) (`pip install linkml`)

### Validate the schemas

```bash
python tools/validate_all.py
```

### Generate downstream artifacts

```bash
python generators/generate_json_schema.py
python generators/generate_sql_ddl.py
python generators/generate_python_classes.py
```

## Key Modeling Decisions

- **Entity is a concrete semantic anchor**, not an abstract root. Classes
  inherit from Entity to declare "I am an enterprise thing."
- **Employee is a Role, not a Person subtype.** A single Person can hold
  multiple concurrent Roles (employee, vendor, visitor) across time.
- **Team is independent**, not an Organization subtype. Teams span
  Organizations and have their own lifecycle semantics.
- **Process is a separate layer** from Domain. Domain models stable nouns;
  Process models volatile workflows that reference (never modify) Domain.
- **Application layer isolates vendor quirks** so vendor migrations don't
  ripple downward.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and the governance docs in
[`docs/governance/`](docs/governance/).

## License

Apache License 2.0 — see [`LICENSE`](LICENSE).
