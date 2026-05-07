# Process Layer

The Process layer holds **workflow definitions and instances** that
describe how capabilities are actually executed. Process references
Domain entities but never modifies them.

## Principles

| # | Principle | Caption |
|---|---|---|
| 1 | Consumption, Not Redefinition | **The Borrower Principle** — Process uses Domain; Process never edits Domain |
| 2 | Versionability | **The Snapshot Principle** — every process definition is versioned; instances bind to a snapshot |
| 3 | Event-Orientation | **The Ledger Principle** — state lives in events; events point to domain entities |
| 4 | Binding Immutability | **The Frozen-Contract Principle** — an instance's definition binding is set at birth and never changes |

## Operational Rule

**Process Binding Immutability** — Once a ProcessInstance is created
with a specific ProcessDefinition version, that binding never changes.
Process migrations are modeled as termination of the old instance and
creation of a new instance with explicitly carried-over state, never
as mutation of the binding.

## Directory Structure

```
03_process/
├── _core/                       # core process abstractions
│   ├── ProcessDefinition.yaml   # versioned workflow specification
│   ├── ProcessInstance.yaml     # live execution bound to a definition
│   ├── ProcessStep.yaml         # is_a Activity — a step in a definition
│   ├── StepCompletion.yaml      # is_a Activity — step execution record
│   ├── ProcessTransition.yaml   # allowed state transitions
│   ├── ProcessEvent.yaml        # event sourcing — state-change events
│   └── enums/
│       ├── ProcessDefinitionStateEnum.yaml
│       ├── ProcessInstanceStateEnum.yaml
│       ├── StepOutcomeEnum.yaml
│       └── ProcessEventTypeEnum.yaml
│
├── Onboarding/
├── Offboarding/
├── OrderFulfillment/
├── InvoiceApproval/
├── PurchaseApproval/
├── IncidentResolution/
└── ContractLifecycle/
```

## How Process Layer Works

1. A **ProcessDefinition** is the versioned workflow spec — what steps,
   in what order, by which roles.
2. A **ProcessInstance** is a live execution — it binds (immutably) to
   one specific ProcessDefinition version.
3. **ProcessStep** records (specializing Activity) define the steps of
   a definition.
4. **StepCompletion** records (specializing Activity) capture the actual
   execution of each step — who, when, what outcome.
5. **ProcessEvent** records capture state-change events for audit and
   event-sourcing patterns.

## Cross-Layer References

- Process imports Foundation (Activity, Person, Role, Entity).
- Process imports Domain (the specific entities the workflow operates on).
- Domain NEVER imports Process. Foundation NEVER imports Process.
- Application MAY import Process to project process instances into
  vendor systems (e.g., ServiceNow tickets).
