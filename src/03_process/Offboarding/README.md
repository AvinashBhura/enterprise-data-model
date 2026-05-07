# Process — Offboarding

Workflow definitions and instances for offboarding EmployeeRoles or
ContractorRoles.

## Entities
- `OffboardingProcessDefinition` (is_a ProcessDefinition)
- `OffboardingProcessInstance` (is_a ProcessInstance)

## Lifecycle Enum
- `OffboardingProcessStateEnum`

## Notes
Mirrors Onboarding in shape; subject is the Role being offboarded.
The completion creates an AlumniRole (HR domain) for the Person.
