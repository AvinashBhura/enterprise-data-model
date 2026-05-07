# Tools

Quality and validation tooling for the EDM.

## Scripts

| Script | Purpose |
|---|---|
| `validate_all.py` | Validate every YAML schema parses and has required LinkML metadata |
| `lint_yaml.py` | Light style/lint pass on YAML files |
| `check_dependency_direction.py` | Enforce the One-Way Gate rule across layers |
| `check_principle_compliance.py` | Check architectural rules (codelist vs taxonomy, base type non-overlap) |
| `diff_schema.py` | Show structural changes between two schema versions |

## Usage

From the project root:

```bash
# Run full validation suite
python tools/validate_all.py

# Check dependency direction
python tools/check_dependency_direction.py

# Lint YAML
python tools/lint_yaml.py

# Compliance checks
python tools/check_principle_compliance.py
```

All scripts return non-zero exit codes on failure for CI integration.
