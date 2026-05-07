# Process — PurchaseApproval

Workflow definitions and instances for approving PurchaseRequisitions
and PurchaseOrders. Implements the Procurement approval capability.

## Entities
- `PurchaseApprovalProcessDefinition` (is_a ProcessDefinition)
- `PurchaseApprovalProcessInstance` (is_a ProcessInstance)

## Lifecycle Enum
- `PurchaseApprovalStateEnum`

## Notes
Subject can be a PurchaseRequisition (pre-PO) or a PurchaseOrder.
Approval routing varies by amount, category, and vendor risk tier.
