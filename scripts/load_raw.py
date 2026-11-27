from pathlib import Path
import duckdb

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "raw_data"
DB_PATH = ROOT / "northwind.duckdb"

SOURCES = {
    "customer": "raw/customer.csv",
    "employees": "raw/employees.csv",
    "suppliers": "raw/suppliers.csv",
    "shippers": "raw/shippers.csv",
    "products": "raw/products.csv",
    "orders": "raw/orders.csv",
    "order_details": "raw/order_details.csv",
    "legacy_orders": "legacy/orders.csv",
    "legacy_order_details": "legacy/order_details.csv",
}

def main():
    print(f"Loading data {DB_PATH.name}")
    con = duckdb.connect(str(DB_PATH))
    con.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    for table_name, rel_path in SOURCES.items():
        file_path = DATA_DIR / rel_path
        con.execute(f"CREATE OR REPLACE TABLE raw.{table_name} AS SELECT * FROM read_csv_auto('{file_path.as_posix()}');")
        row_count = con.execute(f"SELECT COUNT(*) FROM raw.{table_name}").fetchone()[0]
        print(f"  raw.{table_name:<22} {row_count:>6,} แถว")
    con.close()
    print("Loading raw data have done.")

if __name__ == "__main__":
    main()
