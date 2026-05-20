# Capability: Order Fulfillment

**Description**: The enterprise's ability to convert customer orders into
delivered products or services, including order capture, processing,
fulfillment, and billing.

**Primary Steward**: VP of Operations

**Maturity**: Established

## Data Domains Consumed

- `src/02_domain/Sales/OrderManagement/Order/` — Order, OrderLine
- `src/02_domain/Sales/CustomerManagement/Customer/` — Account (customer reference)
- `src/02_domain/Finance/AccountsPayable/Invoice/` — Invoice (AR invoice)

## Processes Used

- `src/03_process/OrderFulfillment/` — Order fulfillment workflow

## Related Capabilities

- Customer Management (upstream)
- Financial Accounting (downstream — billing/revenue recognition)
