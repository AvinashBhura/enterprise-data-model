# Generators

LinkML can generate downstream artifacts from the EDM schemas. The
scripts here invoke LinkML's generators with the right inputs.

## Available Generators

| Script | Output | LinkML generator used |
|---|---|---|
| `generate_json_schema.py` | JSON Schema files (`generated/json_schema/`) | `gen-json-schema` |
| `generate_sql_ddl.py` | SQL DDL (`generated/sql/`) | `gen-sqltables` |
| `generate_python_classes.py` | Python pydantic classes (`generated/python/`) | `gen-pydantic` |
| `generate_shacl.py` | SHACL shapes (`generated/shacl/`) | `gen-shacl` |
| `generate_owl.py` | OWL ontology (`generated/owl/`) | `gen-owl` |
| `generate_graphql.py` | GraphQL schema (`generated/graphql/`) | `gen-graphql` |
| `generate_docs.py` | Human-readable docs (`generated/docs/`) | `gen-doc` |

## Prerequisites

Install LinkML:
```bash
pip install linkml
```

## Usage

From the project root:
```bash
python generators/generate_json_schema.py
```

Each script processes every entity-defining schema in `src/` and emits
the corresponding artifact under `generated/`. Outputs are gitignored.

## Limitations

- Generators are best-effort; the EDM uses LinkML features (mixins,
  union ranges, slot_usage narrowing) that downstream generators may
  handle imperfectly. Inspect outputs before relying on them.
- Cross-layer references via `entity_id` (rather than typed slot ranges)
  are intentional in some places to avoid generator-confusion or
  oversharing across Application boundaries.

## See also

- LinkML generator docs: https://linkml.io/linkml/generators/
