import duckdb

DB_PATH = "northwind.duckdb"

def main():
    con = duckdb.connect(DB_PATH)
    tables = con.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema IN ('main', 'raw') ORDER BY table_schema, table_name;").fetchall()
    print("Tables in DuckDB Data Warehouse:")
    for schema, name in tables:
        count = con.execute(f"SELECT COUNT(*) FROM {schema}.{name}").fetchone()[0]
        print(f" - {schema}.{name}: {count} rows")
    con.close()

if __name__ == "__main__":
    main()
