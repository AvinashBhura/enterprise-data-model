# Process — _core

Core process abstractions used by every process family in the layer.
Other process folders (Onboarding, OrderFulfillment, etc.) specialize
these abstractions.

## Entities

- `ProcessDefinition` — Versioned workflow specification.
- `ProcessInstance` — Live execution bound to a definition.
- `ProcessStep` — A single step within a definition (is_a Activity).
- `StepCompletion` — Execution record for a step (is_a Activity).
- `ProcessTransition` — Allowed transitions between process states.
- `ProcessEvent` — State-change events for audit / event sourcing.

## Enums

- `ProcessDefinitionStateEnum` — Lifecycle of a ProcessDefinition (Draft, Published, Deprecated, Retired).
- `ProcessInstanceStateEnum` — Generic instance states (Initiated, InProgress, Paused, Completed, Cancelled).
- `StepOutcomeEnum` — Completed, Skipped, Failed, Cancelled.
- `ProcessEventTypeEnum` — Started, StepCompleted, Paused, Resumed, Completed, Cancelled.

Process families specialize ProcessDefinition and ProcessInstance and
introduce their own per-family lifecycle enums (e.g.,
OnboardingProcessStateEnum) where they need finer state machines.
