import duckdb

def main():
    con = duckdb.connect("northwind.duckdb")
    tables = con.execute("SHOW TABLES").fetchall()
    print("Tables in database:", [t[0] for t in tables])
    if tables:
        sample = con.execute("SELECT * FROM customer LIMIT 5").fetchall()
        print("Sample customers:", sample)
    con.close()

if __name__ == "__main__":
    main()
