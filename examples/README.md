# Examples

Runnable end-to-end scenarios that trace data through every layer of
the EDM. Each example demonstrates the full lifecycle of a real-world
business event using the canonical entities.

## Scenarios

### `priya_onboarding/`
The canonical end-to-end trace introduced in our architecture
discussions: Priya Menon is hired as an engineer. The example shows:
1. Person record creation (Foundation).
2. EmployeeRole creation (Domain — HR).
3. Onboarding process initiation (Process — Onboarding).
4. Workday and ServiceNow application projections (Application).
5. Step completions and Okta provisioning.
6. Employment activation.

### `vendor_onboarding/`
A vendor (independent consultant) is engaged. Demonstrates:
- Person reuse across role types
- VendorRole creation
- Procurement vendor onboarding workflow

### `reorganization/`
The Engineering Division is split into Platform Engineering and
Product Engineering. Demonstrates:
- Role Immutability operational rule (existing EmployeeRoles end-dated;
  new ones created with new employing_organization)
- OrganizationalUnit lifecycle transitions

### `cross_role_person/`
The Priya Menon journey: hired as employee, leaves, returns as vendor.
Demonstrates the "single Person, many Roles over time" pattern that is
the backbone of the Role-based architecture.

## Format

Each example folder contains numbered YAML files representing
sequential events. Reading them in order tells the story.

These files are example INSTANCE data conformant to the schemas in
`src/`. They are NOT additional schema definitions.
