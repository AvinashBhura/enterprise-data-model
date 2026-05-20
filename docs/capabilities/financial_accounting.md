# Capability: Financial Accounting

**Description**: The enterprise's ability to record, classify, and report
financial transactions according to accounting standards. Covers the general
ledger, accounts payable, accounts receivable, and financial planning.

**Primary Steward**: Chief Financial Officer (CFO)

**Maturity**: Established — regulatory required

## Data Domains Consumed

- `src/02_domain/Finance/GeneralLedger/Account/` — Account (GL chart, is_a Document)
- `src/02_domain/Finance/GeneralLedger/JournalEntry/` — JournalEntry, JournalEntryLine
- `src/02_domain/Finance/AccountsPayable/Invoice/` — Invoice, InvoiceLine
- `src/02_domain/Finance/AccountsPayable/Payment/` — Payment
- `src/02_domain/Finance/FinancialPlanning/Budget/` — Budget, BudgetLine
- `src/02_domain/Finance/FinancialPlanning/FiscalPeriod/` — FiscalPeriod (is_a Period)
- `src/02_domain/Finance/CostAccounting/CostCenter/` — CostCenter (is_a OrganizationalUnit)

## Processes Used

- `src/03_process/InvoiceApproval/` — Invoice approval workflow

## Related Capabilities

- Procurement (upstream — generates AP invoices)
- Order Fulfillment (upstream — generates AR invoices)
- Workforce Compensation (cross-cutting with HR)
