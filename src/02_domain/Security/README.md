# Domain — Security

Primary steward for **identity-and-access stable nouns**: visitor
engagements, access credentials, access grants.

## Primary Steward
The Chief Information Security Officer's office.

## Entities
- `VisitorRole` (Role) — Time-bound facility access engagement.
- `AccessCredential` (Asset) — Badge, smart card, security token.
- `AccessGrant` (Entity) — Permission record (who can access what, when).

## Lifecycle Enums
In `enums/`: VisitLifecycleStateEnum, CredentialLifecycleStateEnum,
AccessGrantLifecycleStateEnum.

## Notes
- Identity provider integration (Okta, Azure AD) lives in the
  Application layer (`04_application/Okta/`).
- Cross-references with HR — visitor hosts are typically EmployeeRoles.
