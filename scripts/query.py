import sys
import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "northwind.duckdb"

def main():
    if len(sys.argv) < 2:
        print('Usage: python scripts/query.py "<SQL_QUERY>"')
        return
    
    sql = sys.argv[1]
    con = duckdb.connect(str(DB_PATH))
    result = con.execute(sql).fetchall()
    cols = [desc[0] for desc in con.description]
    
    print(" | ".join(cols))
    print("-" * 50)
    for row in result:
        print(" | ".join(str(val) for val in row))
    con.close()

if __name__ == "__main__":
    main()
