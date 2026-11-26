import duckdb

def main():
    con = duckdb.connect("northwind.duckdb")
    print("Connected and created northwind.duckdb successfully.")
    con.close()

if __name__ == "__main__":
    main()
