from pathlib import Path

import duckdb


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "data" / "raw"
DATABASE_PATH = PROJECT_ROOT / "northwind.duckdb"


def quote_identifier(identifier: str) -> str:
    escaped_identifier = identifier.replace('"', '""')
    return f'"{escaped_identifier}"'


def get_source_files(source_dir: Path) -> list[Path]:
    if not source_dir.is_dir():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    csv_files = sorted(source_dir.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in source directory: {source_dir}")

    return csv_files


def load_csv_files(connection: duckdb.DuckDBPyConnection, csv_files: list[Path]) -> int:
    loaded_count = 0

    for csv_file in csv_files:
        table_name = csv_file.stem
        quoted_table_name = quote_identifier(table_name)

        connection.execute(
            f"CREATE OR REPLACE TABLE {quoted_table_name} AS "
            "SELECT * FROM read_csv_auto(?)",
            [str(csv_file)],
        )

        row_count = connection.execute(
            f"SELECT COUNT(*) FROM {quoted_table_name}"
        ).fetchone()[0]
        print(
            f"Loaded {csv_file.relative_to(PROJECT_ROOT)} "
            f"into table {table_name} ({row_count} rows)"
        )
        loaded_count += 1

    return loaded_count


def main() -> None:
    csv_files = get_source_files(SOURCE_DIR)
    connection = duckdb.connect(str(DATABASE_PATH))

    try:
        loaded_count = load_csv_files(connection, csv_files)
    finally:
        connection.close()

    print(f"Finished loading {loaded_count} CSV file(s) into {DATABASE_PATH.name}")


if __name__ == "__main__":
    main()
