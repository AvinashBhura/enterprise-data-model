# Domain — Finance

Primary steward for **financial stable nouns**: GL accounts, journal
entries, invoices, payments, budgets, fiscal periods.

## Primary Steward
The CFO's office. Day-to-day stewardship by Finance Data Architecture team.

## Entities

### Stable Nouns
- `Account` — GL account
- `CostCenter` — accounting unit for cost allocation
- `Budget` — planned financial commitment
- `FiscalPeriod` — accounting period (year, quarter, month)

### Activities
- `JournalEntry` — accounting posting (specializes Activity)
- `Payment` — money movement (specializes Activity)

### Agreements
- `Invoice` — payable/receivable (specializes Agreement)

## Lifecycle Enums
In `enums/`: AccountLifecycleStateEnum, InvoiceLifecycleStateEnum,
PaymentLifecycleStateEnum, JournalEntryLifecycleStateEnum,
BudgetLifecycleStateEnum.

## Notes
- The Chart of Accounts hierarchy is in Common (`ChartOfAccountsTaxonomy`).
- Specific account instances live HERE in the Finance domain.
- Approval workflows for invoices and payments live in the Process layer
  (`03_process/InvoiceApproval/`).
