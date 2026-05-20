# Domain — Human Resources

Primary steward for **employment-related stable nouns**: people-as-employees,
positions, organizational units (HR's view), compensation packages,
performance reviews, and employment-related agreements.

## Primary Steward

The Chief People Officer's office. Day-to-day stewardship by HR Data
Architecture team.

## Scope

This capability owns the stable **nouns** of HR — what HR is. The
volatile workflows (onboarding processes, performance review cycles,
parental leave processes) live in the Process layer, not here.

## Entities

### Roles (specializations of Foundation `Role`)
- `EmployeeRole` — A Person engaged as an employee under an EmploymentContract.
- `ContractorRole` — A Person engaged under a contracting arrangement.
- `AlumniRole` — A former employee after separation.
- `ManagerRole` — Management authority over other Roles.

### Stable Nouns (specializations of Foundation `Entity`)
- `Position` — A defined job slot independent of who fills it.
- `PositionHierarchy` — Reporting structure between Positions.
- `CompensationPackage` — Salary, bonus, benefits structure.
- `OnboardingChecklist` — Template defining onboarding requirements.
- `ChecklistItem` — Individual item within an OnboardingChecklist.

### Stable Activities (specializations of Foundation `Activity`)
- `PerformanceReview` — A periodic performance evaluation event.

### Agreements (specializations of Foundation `Agreement`)
- `EmploymentContract` — Formal employment agreement.
- `Offer` — Pre-employment offer letter.

## Per-Entity Lifecycle Enums

In `enums/`:
- `EmploymentLifecycleStateEnum` — for EmployeeRole
- `ContractorLifecycleStateEnum` — for ContractorRole
- `PositionLifecycleStateEnum` — for Position
- `OfferLifecycleStateEnum` — for Offer

## Key Modeling Decisions

- **Employee is a Role, NOT a Person subtype.** A Person can hold
  EmployeeRole, ContractorRole, AlumniRole — sometimes simultaneously
  or in sequence — without identity disruption.
- **Position is independent of Role.** A Position is a job slot;
  EmployeeRole.primary_position references it. Vacant positions exist
  without any Role; one Position may be filled by sequential Roles.
- **OnboardingChecklist is a TEMPLATE.** Live executions of onboarding
  belong in `03_process/Onboarding/`.
