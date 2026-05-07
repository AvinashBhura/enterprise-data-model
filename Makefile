.PHONY: help install check validate dependency-check principle-check lint test clean generate

# Default: show help
help:
	@echo "Enterprise Data Model — common commands"
	@echo ""
	@echo "  make install            Install project + dev dependencies"
	@echo "  make check              Run all quality gates (validate + dependency + principle + tests)"
	@echo "  make validate           Validate every LinkML schema parses cleanly"
	@echo "  make dependency-check   Verify imports flow upward only (One-Way Gate)"
	@echo "  make principle-check    Verify architectural rule compliance"
	@echo "  make lint               YAML lint pass"
	@echo "  make test               Run pytest test suite"
	@echo "  make generate           Run all LinkML generators (requires linkml installed)"
	@echo "  make clean              Remove generated artifacts and caches"
	@echo ""
	@echo "After any meaningful schema change, run 'make check' before committing."

install:
	pip install -e ".[dev]"

# The four quality gates. Run before every commit.
check: validate dependency-check principle-check test
	@echo ""
	@echo "✅ All quality gates passed."

validate:
	@python tools/validate_all.py

dependency-check:
	@python tools/check_dependency_direction.py

principle-check:
	@python tools/check_principle_compliance.py

lint:
	@python tools/lint_yaml.py

test:
	@python -m pytest tests/ -q

generate:
	@python generators/generate_json_schema.py
	@python generators/generate_python_classes.py
	@python generators/generate_sql_ddl.py

clean:
	rm -rf generated/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	@echo "Cleaned."
