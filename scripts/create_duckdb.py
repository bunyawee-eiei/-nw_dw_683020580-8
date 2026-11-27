import duckdb

DB_PATH = "northwind.duckdb"

def main():
    con = duckdb.connect(DB_PATH)
    con.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    print(f"Created Data Warehouse '{DB_PATH}' with schema 'raw' successfully.")
    con.close()

if __name__ == "__main__":
    main()
