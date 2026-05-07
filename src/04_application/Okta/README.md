# Application — Okta

Vendor-specific projections for **Okta** (identity and access management).

## Bidirectional Mapping
| Canonical | Okta | Notes |
|---|---|---|
| `IT.UserAccount` | `OktaUser` | Okta User |
| `Foundation.Team` | `OktaGroup` | Okta Group used for access control |
| `Process.StepCompletion` (provisioning steps) | `OktaUserProvisioningRecord` | Okta provisioning event |

## Vendor-Specific Identifiers
- `okta_user_id` (24 chars), `okta_group_id`, `okta_app_assignment_id`
