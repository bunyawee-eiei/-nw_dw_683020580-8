import duckdb
import glob
import os

# --- แก้ไขแค่ตรง SOURCE_DIR หากเปลี่ยนที่เก็บไฟล์ ---
SOURCE_DIR = "data/raw"
DB_PATH = "northwind.duckdb"

def main():
    con = duckdb.connect(DB_PATH)
    con.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    
    csv_files = sorted(glob.glob(os.path.join(SOURCE_DIR, "*.csv")))
    if not csv_files:
        print(f"ไม่พบไฟล์ .csv ใน {SOURCE_DIR}")
        return

    for file_path in csv_files:
        table_name = os.path.splitext(os.path.basename(file_path))[0]
        # สร้างตารางใน schema raw (และสร้างใน main ด้วยเผื่ออาจารย์ query แบบไม่ใส่ชื่อ schema)
        con.execute(f"CREATE OR REPLACE TABLE raw.{table_name} AS SELECT * FROM read_csv_auto('{file_path}');")
        con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_csv_auto('{file_path}');")
        
        count = con.execute(f"SELECT COUNT(*) FROM raw.{table_name}").fetchone()[0]
        print(f"Extracted '{file_path}' -> table 'raw.{table_name}' ({count} rows)")

    con.close()
    print("Extract raw data into DuckDB Data Warehouse complete!")

if __name__ == "__main__":
    main()
