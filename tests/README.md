# Tests

The EDM project tests fall into four categories.

## Categories

### `validation/`
Schema-level validation tests — does each schema parse, do all required
fields exist, do imports resolve. Largely covered by
`tools/validate_all.py` but exposed here as pytest tests so they
integrate with the standard test runner.

### `architectural_rules/`
Tests for the five operational rules:
- `test_role_immutability.py`
- `test_natural_key_placement.py`
- `test_domain_stewardship.py`
- `test_process_binding_immutability.py`
- `test_codelist_vs_taxonomy_placement.py`

These tests are **structural** (run against the schemas) and
**instance-level** (run against fixture data).

### `cross_layer/`
End-to-end scenario tests using the fixtures in `tests/fixtures/` —
the Priya onboarding scenario, vendor onboarding, reorganization,
process version migration, multi-system master data.

### `fixtures/`
Sample instance YAML files for use in the tests above. Mirrors the
structure of `examples/priya_onboarding/` but stripped to minimal
data needed for assertions.

## Running

```bash
pip install -e ".[dev]"
pytest                         # all tests
pytest tests/validation/       # just schema validation
pytest tests/architectural_rules/  # just rule tests
pytest tests/cross_layer/      # just scenario tests
```

CI runs all four categories on every PR. See
`.github/workflows/validate.yml`.
