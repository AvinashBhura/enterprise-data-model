# Domain — IT

Primary steward for **IT-asset and IT-service stable nouns**: devices,
software licenses, user accounts, incidents.

## Primary Steward
The CIO's office.

## Entities
- `Device` (Asset) — Laptops, servers, phones, network equipment.
- `SoftwareLicense` (Asset) — License instance held by the enterprise.
- `UserAccount` (Entity) — A system identity (linked to a Person via Role).
- `Incident` (Activity) — An IT incident (issue, outage, security event).

## Lifecycle Enums
In `enums/`: DeviceLifecycleStateEnum, LicenseLifecycleStateEnum,
UserAccountLifecycleStateEnum, IncidentLifecycleStateEnum.

## Notes
- Identity-provider-specific user accounts (Okta, Azure AD) live in the
  Application layer.
- Incident resolution workflow lives in `03_process/IncidentResolution/`.
