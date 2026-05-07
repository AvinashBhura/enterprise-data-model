# Process — InvoiceApproval

Workflow definitions and instances for approving incoming invoices (AP).
Implements the AP Invoice Approval capability owned by Finance.

## Entities
- `InvoiceApprovalProcessDefinition` (is_a ProcessDefinition)
- `InvoiceApprovalProcessInstance` (is_a ProcessInstance)

## Lifecycle Enum
- `InvoiceApprovalStateEnum`

## Notes
Subject is the Finance Invoice. Approval definitions vary by amount
threshold and routing rules.
