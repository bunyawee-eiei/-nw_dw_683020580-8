from pathlib import Path

import duckdb


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = ROOT / "northwind.duckdb"

SOURCES = {
    "customer": "raw/customer.csv",
    "employees": "raw/employees.csv",
    "order_details": "raw/order_details.csv",
    "orders": "raw/orders.csv",
    "products": "raw/products.csv",
    "shippers": "raw/shippers.csv",
    "suppliers": "raw/suppliers.csv",
    "legacy_orders": "legacy/orders.csv",
    "legacy_order_details": "legacy/order_details.csv",
}


def quote_identifier(identifier: str) -> str:
    escaped_identifier = identifier.replace('"', '""')
    return f'"{escaped_identifier}"'


def main() -> None:
    connection = duckdb.connect(str(DB_PATH))

    try:
        connection.execute("CREATE SCHEMA IF NOT EXISTS raw")
        print(f"Loading source data into {DB_PATH.name}")

        for table_name, relative_path in SOURCES.items():
            csv_path = DATA_DIR / relative_path
            if not csv_path.is_file():
                raise FileNotFoundError(f"Source file not found: {csv_path}")

            table = f"raw.{quote_identifier(table_name)}"
            connection.execute(
                f"CREATE OR REPLACE TABLE {table} AS "
                "SELECT * FROM read_csv_auto(?)",
                [str(csv_path)],
            )
            row_count = connection.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()[0]
            print(f"raw.{table_name:<22} {row_count:>6,} rows")
    finally:
        connection.close()

    print("Finished loading all source files.")


if __name__ == "__main__":
    main()
