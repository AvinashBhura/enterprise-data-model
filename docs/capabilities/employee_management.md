# Capability: Employee Management

**Description**: The enterprise's ability to attract, onboard, develop,
compensate, evaluate, and offboard employees throughout the employment
lifecycle.

**Primary Steward**: Chief Human Resources Officer (CHRO)

**Maturity**: Established — core enterprise capability with mature processes

## Data Domains Consumed

- `src/02_domain/HR/PeopleServices/Employee/` — EmployeeRole, ContractorRole, AlumniRole, ManagerRole
- `src/02_domain/HR/PeopleServices/Position/` — Position, PositionHierarchy
- `src/02_domain/HR/PeopleServices/EmploymentContract/` — EmploymentContract
- `src/02_domain/HR/PeopleServices/OnboardingChecklist/` — OnboardingChecklist, ChecklistItem
- `src/02_domain/HR/Compensation/CompensationPackage/` — CompensationPackage
- `src/02_domain/HR/Performance/PerformanceReview/` — PerformanceReview
- `src/02_domain/HR/TalentAcquisition/Offer/` — Offer

## Processes Used

- `src/03_process/Onboarding/` — Employee onboarding workflow
- `src/03_process/Offboarding/` — Employee offboarding workflow

## Related Capabilities

- Compensation & Benefits (sub-capability)
- Performance Management (sub-capability)
- Workforce Planning (cross-cutting with Finance)
