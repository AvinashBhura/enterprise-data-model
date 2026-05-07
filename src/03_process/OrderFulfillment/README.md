# Process — OrderFulfillment

Workflow definitions and instances for fulfilling customer Orders.
Implements the Order Fulfillment capability owned by the Sales domain.

## Entities
- `OrderFulfillmentProcessDefinition` (is_a ProcessDefinition)
- `OrderFulfillmentProcessInstance` (is_a ProcessInstance)

## Lifecycle Enum
- `OrderFulfillmentStateEnum`

## Notes
Subject is the Order (Sales domain). Process never modifies the Order;
state changes are recorded on the ProcessInstance.
