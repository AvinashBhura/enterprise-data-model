# Domain — Governance

Primary steward for **governance-and-board stable nouns**: board members,
committee leadership, formal advisors.

## Primary Steward
The Corporate Secretary's office (typically reporting to General Counsel
and the Board).

## Entities
- `BoardMemberRole` (Role) — A Person serving on a governing board.
- `CommitteeChairRole` (Role) — A Person leading a formal committee.
- `CommitteeMemberRole` (Role) — A Person serving on a committee.
- `AdvisorRole` (Role) — A Person engaged as a formal advisor.

## Lifecycle Enum
In `enums/`: GovernanceRoleLifecycleStateEnum (shared across these Roles).

## Notes
- Committees themselves are Teams (Foundation), with `team_type: COMMITTEE`.
  This domain captures the formal Roles people hold in those committees.
- Distinct from generic ManagerRole (HR) — governance roles carry
  fiduciary responsibility and have term limits.
