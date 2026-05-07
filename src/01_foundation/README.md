# Foundation Layer

The Foundation layer holds the **permanent, universal concepts** that define
what an enterprise fundamentally consists of. Every higher layer extends
and references these entities.

## Principles

| # | Principle | Caption |
|---|---|---|
| 1 | Universality | **The Highlander Principle** — there can be only one |
| 2 | Structural Immutability | **The Boring Principle** — if it's changing, it doesn't belong here |
| 3 | Abstraction | **The Independence Principle** — exists without the business needing to do anything |
| 4 | Semantic Integrity | **The Common Language Principle** — one meaning, understood by everyone |
| 5 | Minimalism | **The Spartan Principle** — only concrete entities live here |
| 6 | Entity-Purity | **The Noun Principle** — the business is made of things, not construction material |
| 7 | Semantic Anchoring | **The Origin Principle** — Entity is where things begin, not what they must become |

## Foundation Entities

| Entity | File | Purpose |
|---|---|---|
| Entity | [`Entity.yaml`](Entity.yaml) | The semantic anchor — every concept declares membership by inheriting |
| Person | [`Person.yaml`](Person.yaml) | A human being — stable identity for all engagements |
| Organization | [`Organization.yaml`](Organization.yaml) | Abstract formal body — + LegalEntity, OrganizationalUnit subtypes |
| Team | [`Team.yaml`](Team.yaml) | Purposeful group (independent — not an Organization subtype) |
| Role | [`Role.yaml`](Role.yaml) | Time-bound engagement — the universal pivot for relationships |
| Activity | [`Activity.yaml`](Activity.yaml) | Something happening in time |
| Agreement | [`Agreement.yaml`](Agreement.yaml) | Formal commitment between parties |
| Asset | [`Asset.yaml`](Asset.yaml) | Thing of value, owned or managed |
| Address | [`Address.yaml`](Address.yaml) | Location reference |

## Common Sub-Layer

The [`common/`](common/) directory holds the reusable construction material:
base types, value types, codelists, and taxonomies used by this layer and
every layer above. See [`common/README.md`](common/README.md).

## Architectural Rules Anchored Here

- **Entity is concrete, not abstract** (Semantic Anchoring / Origin Principle).
  It carries only `entity_id`. All other cross-cutting concerns are in Common base types.
- **Roles are the pivot for engagements** (Who-Plays-What). Never specialize
  Person or Organization for relationships — specialize Role.
- **Role Immutability**: once effective, a Role doesn't mutate its core terms
  (employing_organization, position). Changes end one Role and begin another.
- **Natural Key Placement**: enterprise-native natural keys live on canonical
  entities via `Identifiable`. Vendor system keys live on Application subclasses.

## Dependencies

Foundation depends on nothing. Every other layer depends on Foundation.
This is the "One-Way Gate" rule.

## Modification Policy

Changes to Foundation require:
1. Architecture review (changes here ripple across every layer).
2. Formal deprecation of any removed slot over at least two release cycles.
3. Backward-compatible additions preferred; breaking changes require major version bump.
