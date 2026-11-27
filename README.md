# **Command Lines**

- Create python env. with the name: .venv
`python -m venv .venv`

```python
python -m venv .venv
pip install -r requirements.txt

print('Hello World')
```

## dbt models

The dbt project is in `references/references`. Its staging models clean the
tables in the DuckDB `raw` schema, and its warehouse models build dimensions
and an order-line fact table.

Load the raw CSV files, then validate and build the models from the repository
root:

```bash
python scripts/load_raw.py
.venv/bin/dbt debug --project-dir references/references --profiles-dir references/references
.venv/bin/dbt run --project-dir references/references --profiles-dir references/references
.venv/bin/dbt test --project-dir references/references --profiles-dir references/references
```

