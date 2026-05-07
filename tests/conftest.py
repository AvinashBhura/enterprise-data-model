"""
conftest.py — Shared pytest fixtures and configuration for the EDM
test suite.
"""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC = PROJECT_ROOT / "src"


@pytest.fixture(scope="session")
def project_root() -> Path:
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def src_root() -> Path:
    return SRC


@pytest.fixture(scope="session")
def all_schemas() -> list[tuple[Path, dict]]:
    """Load every LinkML schema under src/ into memory once per session."""
    schemas = []
    for path in sorted(SRC.rglob("*.yaml")):
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
            if isinstance(doc, dict):
                schemas.append((path, doc))
        except yaml.YAMLError:
            continue
    return schemas


@pytest.fixture(scope="session")
def foundation_schemas(all_schemas) -> list[tuple[Path, dict]]:
    return [
        (p, d) for p, d in all_schemas if "01_foundation" in p.parts
    ]


@pytest.fixture(scope="session")
def domain_schemas(all_schemas) -> list[tuple[Path, dict]]:
    return [
        (p, d) for p, d in all_schemas if "02_domain" in p.parts
    ]


@pytest.fixture(scope="session")
def process_schemas(all_schemas) -> list[tuple[Path, dict]]:
    return [
        (p, d) for p, d in all_schemas if "03_process" in p.parts
    ]


@pytest.fixture(scope="session")
def application_schemas(all_schemas) -> list[tuple[Path, dict]]:
    return [
        (p, d) for p, d in all_schemas if "04_application" in p.parts
    ]
