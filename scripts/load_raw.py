import duckdb
import glob
import os

def main():
    con = duckdb.connect("northwind.duckdb")
    for file_path in glob.glob("data/raw/*.csv"):
        table_name = os.path.splitext(os.path.basename(file_path))[0]
        con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_csv_auto('{file_path}')")
        print(f"Loaded {file_path} into table '{table_name}'")
    con.close()

if __name__ == "__main__":
    main()
