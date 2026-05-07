# Application — Workday

Vendor-specific projections for **Workday** (HR system of record).
Workday holds the system-of-record data for Person, EmployeeRole,
Position, and OrganizationalUnit.

## Bidirectional Mapping

| Canonical (Domain) | Workday (Application) | Notes |
|---|---|---|
| `Foundation.Person` | `WorkdayPerson` | Workday "Worker" identity |
| `HR.EmployeeRole` | `WorkdayEmployeeRole` | Workday "Worker assignment" |
| `HR.Position` | `WorkdayPosition` | Workday "Position" |
| `Foundation.Organization` | `WorkdayOrganization` | Workday "Supervisory Organization" |

## Vendor-Specific Identifiers

- `workday_worker_id` — primary natural key for a person in Workday
- `workday_position_id` — Position identifier
- `workday_supervisory_org_id` — supervisory org identifier (Workday-specific concept)
- `workday_cost_center` — Workday cost center reference

## Sync Notes

Workday is the canonical system-of-record for HR data; sync direction
is typically **Workday → EDM** (Workday is authoritative). Sync status
tracking via the standard `SyncMetadata` from `_shared/`.
