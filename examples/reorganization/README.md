# Example — Reorganization

Engineering Division is split into Platform Engineering and Product
Engineering. All 240 engineers are reassigned.

## Architectural Demonstrations

- **Role Immutability operational rule**: existing EmployeeRole records
  are end-dated (effective_to set, lifecycle_state → SUPERSEDED). New
  EmployeeRole records are created with new employing_organization,
  same Person, new effective_from. Person.entity_id is unchanged for
  every affected employee.
- **OrganizationalUnit lifecycle**: original "Engineering Division"
  Organization transitions to RETIRED; two new OrganizationalUnit
  records appear with lifecycle_state ACTIVE.
- **No Process layer disruption**: ongoing OnboardingProcessInstances
  continue against their original ProcessDefinition versions, with
  only the EmployeeRole references updated.

## Files

(Sample fixtures to be added.)
