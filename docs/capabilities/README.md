# Business Capabilities

This folder documents the enterprise's **business capabilities** — what the
business must be able to do — as a separate concept from data domains and
processes.

## Why Capabilities Are Documented Separately

A **capability** is a stable, business-ability description (e.g., "Customer
Management", "Employee Onboarding"). It describes *what* the business does,
not *how*.

A **data domain** (modeled in `src/02_domain/`) is a logical grouping of
entities that supports one or more capabilities. Data domains describe *what
information* the business maintains.

A **business process** (modeled in `src/03_process/`) is a sequence of
activities that operationalizes a capability. Processes describe *how* the
business does what it does.

These three are related but distinct. A single capability typically consumes
multiple data domains and is operationalized by multiple processes.

## How to Use These Documents

Each capability document lists:

- **Description**: what business ability it provides
- **Data Domains Consumed**: cross-links to `src/02_domain/` paths
- **Processes Used**: cross-links to `src/03_process/` family folders
- **Primary Steward**: business owner
- **Maturity**: nascent / established / strategic
- **Related Capabilities**: cross-links to other capabilities

Capability documents are stewarded by business architects, not data modelers.
They are the input to data domain identification, not the output.

## Capability Catalog

| Capability | Domains Consumed | Processes Used |
|---|---|---|
| [Customer Management](customer_management.md) | Sales/CustomerManagement, Sales/PipelineManagement | (none process-modeled yet) |
| [Employee Management](employee_management.md) | HR/PeopleServices, HR/Compensation, HR/Performance | Onboarding, Offboarding |
| [Order Fulfillment](order_fulfillment.md) | Sales/OrderManagement, Sales/CustomerManagement | OrderFulfillment |
| [Financial Accounting](financial_accounting.md) | Finance/GeneralLedger, Finance/AccountsPayable | InvoiceApproval |
| [Procurement](procurement.md) | Procurement/Sourcing, Procurement/Purchasing | PurchaseApproval |
| [Legal & Compliance](legal_compliance.md) | Legal/Contracts, Legal/Compliance, Legal/IntellectualProperty | ContractLifecycle |
| [Workplace Security](workplace_security.md) | Security/PhysicalSecurity, Security/LogicalSecurity | (none process-modeled yet) |
| [IT Service Management](it_service_management.md) | IT/ServiceManagement, IT/AssetManagement, IT/IdentityManagement | IncidentResolution |
| [Facilities Management](facilities_management.md) | Facilities/RealEstate | (none process-modeled yet) |
| [Corporate Governance](corporate_governance.md) | Governance/CorporateGovernance | (none process-modeled yet) |
