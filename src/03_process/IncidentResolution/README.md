# Process — IncidentResolution

Workflow definitions and instances for resolving IT incidents.
Implements the Incident Resolution capability owned by IT.

## Entities
- `IncidentResolutionProcessDefinition` (is_a ProcessDefinition)
- `IncidentResolutionProcessInstance` (is_a ProcessInstance)

## Lifecycle Enum
- `IncidentResolutionStateEnum`

## Notes
Subject is the IT Incident. Definitions vary by severity tier and SLA.
Application-layer projection: ServiceNowIncident extends ProcessInstance.
