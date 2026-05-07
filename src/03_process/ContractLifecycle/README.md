# Process — ContractLifecycle

Workflow definitions and instances for managing the contract lifecycle —
drafting, negotiation, review, signing, renewal, termination.
Implements the Contract Lifecycle Management capability owned jointly
by Legal and the contracting domain (Procurement, Sales, HR).

## Entities
- `ContractLifecycleProcessDefinition` (is_a ProcessDefinition)
- `ContractLifecycleProcessInstance` (is_a ProcessInstance)

## Lifecycle Enum
- `ContractLifecycleStateEnum`

## Notes
Subject is any Agreement specialization (VendorContract,
EmploymentContract, NDA, LicensingAgreement, Lease).
