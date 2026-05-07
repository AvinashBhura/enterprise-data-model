# Process — Onboarding

Workflow definitions and live instances for onboarding new EmployeeRoles
or ContractorRoles. Implements the Employee Onboarding capability owned
by the HumanResources domain.

## Entities

- `OnboardingProcessDefinition` (is_a ProcessDefinition) — versioned
  onboarding workflow specification.
- `OnboardingProcessInstance` (is_a ProcessInstance) — live execution
  for a specific EmployeeRole / ContractorRole.

## Lifecycle Enum

- `OnboardingProcessStateEnum` — Onboarding-specific fine-grained states
  (Initiated → EquipmentOrdered → AccessProvisioned → SystemsTrained →
  Complete).

## Cross-Layer References

- References Domain entities: EmployeeRole / ContractorRole / Person /
  Position / OnboardingChecklist (NEVER modifies them).
- Application-layer projections: ServiceNowOnboardingTicket extends
  OnboardingProcessInstance with ServiceNow-specific fields.
