# Application — ServiceNow

Vendor-specific projections for **ServiceNow** (IT service management).

## Bidirectional Mapping

| Canonical | ServiceNow | Notes |
|---|---|---|
| `IT.UserAccount` | `ServiceNowUser` | sys_user record |
| `IT.Incident` | `ServiceNowIncident` | incident table record |
| `Process.OnboardingProcessInstance` | `ServiceNowOnboardingTicket` | catalog request projection |

## Vendor-Specific Identifiers
- `snow_sys_id` — universal 32-char ServiceNow record identifier
- `snow_number` — human-readable ticket number (INC, REQ, RITM, etc.)
