# Pattern — Union Ranges

## The principle

> When a slot can legitimately hold either of multiple unrelated types,
> use LinkML's `any_of` to declare a union range. Reserve unions for
> cases where a shared abstract parent would be artificial.

## The "Party" alternative we rejected

In FIBO and ISO 20022, a `Party` abstract class sits over both Person
and Organization. Many slots have `range: Party` and either kind can
fill them. We chose **not** to introduce `Party` (it added an
abstraction layer without enough payoff for our scope) and instead
use union ranges where Person/Organization ambiguity arises.

## How to express a union range

```yaml
VendorRole:
  is_a: Role
  attributes:
    held_by:
      any_of:
        - range: Person          # independent consultant
        - range: Organization    # vendor company
      required: true
```

## When to use it

✅ **Use union range when:**
- Two unrelated types can both legitimately fill the slot.
- Inserting an abstract parent would be artificial.
- The union is at *one specific slot*, not pervasive across the model.

❌ **Don't use it when:**
- One type dominates and the other is rare. Just use the dominant
  type and handle the edge case separately.
- The "union" is really suggesting a missing abstraction. If you find
  yourself writing the same union in five places, the abstraction is
  earning its place.

## Concrete examples in the EDM

| Slot | Union | Why |
|---|---|---|
| `VendorRole.held_by` | Person OR Organization | Vendors are equally common as both |
| `Activity.participants` | Entity (lets any subtype participate) | Genuinely diverse — Person, Org, Team |
| `AgreementParty.party` | Entity | Agreements between any combination |
| `Asset.custodian` | Entity | Person, Org, or Team can be custodian |

## Strict types where appropriate

For roles where ambiguity *isn't* real, narrow the type:

```yaml
EmployeeRole:
  slot_usage:
    held_by_person:
      required: true                 # only Persons can be employees

VisitorRole:
  slot_usage:
    held_by_person:
      required: true                 # only Persons visit facilities
```

The ability to be strict where strictness is right is one reason we
chose unions over a universal Party abstraction.

## Trade-offs to be aware of

- **Generators must handle unions**: JSON Schema `oneOf`, SHACL
  alternatives, GraphQL unions. The generators in this project handle
  them, but downstream consumers must too.
- **Query complexity**: queries on union-typed slots may need
  type-discriminator logic.
- **Documentation**: every union range should explain *why* both types
  are legitimately valid in the slot's description.

## The "evolving abstraction" rule

If a union range starts appearing in many slots, that's a signal to
reconsider whether an abstraction (like Party) is now earning its
place. Re-introducing it later is a structured refactor:

1. Insert the abstract class above the existing concrete types.
2. Migrate all union-range slots to the new abstract type.
3. Existing data continues to validate (concrete classes still inherit).

We deferred this for now; the union approach is sufficient for the
EDM's current scope.
