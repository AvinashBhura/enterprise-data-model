# Example — Cross-Role Person Journey

Priya Menon's full enterprise journey:
- 2021: ContractorRole (intern via staffing agency)
- 2022: EmployeeRole (full-time conversion)
- 2024: ON_LEAVE (parental leave)
- 2025: ACTIVE (returned)
- 2026: SEPARATED (resigned)
- 2027: AlumniRole created on separation
- 2027: VendorRole (returns as independent consultant)

## Architectural Demonstrations

- **One Person.entity_id, six Roles over time**: the canonical example
  of the Role-based architecture. A single Person record persists
  across every engagement; the engagements come and go as separate
  Role instances.
- **Role-state vs Role-existence**: ON_LEAVE is a state on the same
  EmployeeRole (no new Role created); SEPARATED ends the EmployeeRole
  and creates an AlumniRole; the later vendor engagement is an entirely
  new VendorRole.
- **Identity continuity test**: a single query
  `SELECT * FROM Role WHERE held_by_person = priya.entity_id`
  returns her complete enterprise history.

## Files

(Sample fixtures to be added.)
