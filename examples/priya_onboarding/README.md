# Example — Priya Onboarding (End-to-End)

This scenario traces Priya Menon from offer-acceptance through her
first week as an employee at Acme Corp.

## Cast

- **Priya Menon** — the Person being hired.
- **Acme Corp** — the LegalEntity employing her.
- **Engineering Division → Platform Department → Infra Team** — the
  org-chart path.
- **OnboardingProcessDefinition v3.2 (US Engineering)** — the process
  she is onboarded under.

## Files (read in order)

1. `01_create_person.yaml` — Priya's Foundation Person record is created.
2. `02_create_employee_role.yaml` — Her HR EmployeeRole is created with
   employee_number E10847.
3. `03_workday_projection.yaml` — Workday Application-layer projections
   (WorkdayPerson + WorkdayEmployeeRole) are created with
   workday_worker_id WD-998234.
4. `04_start_onboarding_process.yaml` — An OnboardingProcessInstance is
   started, bound to OnboardingProcessDefinition v3.2.
5. `05_servicenow_ticket.yaml` — ServiceNowOnboardingTicket projection
   is created for IT to track onboarding tasks.
6. `06_complete_steps.yaml` — Sequential StepCompletion records as
   onboarding steps complete (laptop provisioning, Okta account, etc.).
7. `07_okta_provisioning.yaml` — OktaUserProvisioningRecord captures
   the Okta account provisioning specifically.
8. `08_activate_employment.yaml` — On Day 5, EmployeeRole transitions
   from PENDING_START to ACTIVE; OnboardingProcessInstance completes.

## Architectural Demonstrations

- **Role-based pattern**: Person.entity_id stays stable; EmployeeRole
  carries employment-specific data.
- **Layered references**: The OnboardingProcessInstance references the
  EmployeeRole's entity_id (subject_entity_id), never modifying the Role.
- **Application projections**: WorkdayEmployeeRole, ServiceNowOnboardingTicket,
  OktaUserProvisioningRecord — each carries vendor-specific identifiers
  without polluting Domain or Process.
- **Frozen-Contract**: The OnboardingProcessInstance binds to v3.2 of
  the definition; even if v4.0 launches mid-onboarding, Priya's
  instance continues against v3.2.
- **Lifecycle separation**: EmployeeRole.employment_status (coarse:
  PENDING_START → ACTIVE) is distinct from
  OnboardingProcessInstance.onboarding_state (fine-grained workflow:
  INITIATED → ... → COMPLETE).
