# Pattern — Lifecycle Modeling

## The principle

> Lifecycle is a **base type** (`Lifecycleable`) entities opt into. The
> specific lifecycle state enum is **per-entity**. Coarse entity
> lifecycle is distinct from fine workflow state.

## The two scales of state

The EDM tracks state at two scales:

| Scale | Where it lives | Example |
|---|---|---|
| **Entity-level lifecycle** | `Lifecycleable.lifecycle_state` on the entity | `EmployeeRole.lifecycle_state = ACTIVE` |
| **Workflow state** | `ProcessInstance.lifecycle_state` + per-process state attribute | `OnboardingProcessInstance.onboarding_state = ACCESS_PROVISIONED` |

Don't conflate them. An employee being ACTIVE (entity lifecycle) is
different from her onboarding being ACCESS_PROVISIONED (workflow state).

## Entity-level lifecycle pattern

```yaml
EmployeeRole:
  is_a: Role
  mixins:
    - Lifecycleable
  slot_usage:
    lifecycle_state:
      range: EmploymentLifecycleStateEnum   # per-entity narrowing
      required: true
```

`Lifecycleable` itself comes from Common:

```yaml
Lifecycleable:
  mixin: true
  attributes:
    lifecycle_state: { range: string, required: true }
    state_effective_from: { range: datetime }
    state_effective_to: { range: datetime }
    state_history: { range: StateTransition, multivalued: true }
```

The actual state enum (`EmploymentLifecycleStateEnum`) is defined per
entity, in the entity's `enums/` folder.

## The "one enum per entity" decision

We chose **one lifecycle enum per entity** rather than a few shared
enums for two reasons:

1. **Semantic precision** — Person's lifecycle (PROSPECT → ACTIVE → MERGED)
   is genuinely different from Agreement's (DRAFT → SIGNED → EXECUTED →
   TERMINATED). Forcing them to share an enum forces awkward middle
   ground.
2. **Independent evolution** — adding a new state to one entity (say,
   adding `RECONSIDERATION` to Offer) shouldn't affect every other
   entity that happens to share the enum.

## State transitions are append-only

`state_history` is an immutable list of `StateTransition` records.
Each transition records `from_state`, `to_state`, timestamp, actor, and
reason. Never edit a past transition; always append a new one when state
changes.

```yaml
StateTransition:
  attributes:
    from_state: { range: string, required: true }
    to_state: { range: string, required: true }
    transition_timestamp: { range: datetime, required: true }
    transitioned_by: { range: Entity }
    reason: { range: string }
```

This gives you point-in-time reconstruction: "what state was this
entity in on July 17?" is answerable by walking the state_history.

## What about workflow state?

Workflow state lives on the ProcessInstance, not on the entity.
- `OnboardingProcessInstance.lifecycle_state` (generic instance state:
  IN_PROGRESS, COMPLETED, ...)
- `OnboardingProcessInstance.onboarding_state` (fine-grained workflow
  state: INITIATED → ACCESS_PROVISIONED → ... → COMPLETE)

Both can coexist on a single instance.

## Why entities don't carry workflow state

Putting workflow state on entities is a common error. It feels
convenient ("just add `current_workflow_step` to Employee") but it
breaks the architecture:

- Domain becomes bloated with fields only relevant to specific processes
- A single entity can't be in multiple processes simultaneously
- Process changes force Domain schema changes (volatility leak)

Keep workflow state on `ProcessInstance`. The entity carries only
its coarse lifecycle.
