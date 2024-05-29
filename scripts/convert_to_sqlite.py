import json
import sqlite3
import os


def convert_json_to_sqlite(json_file, sqlite_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()

    headers = data[0].keys()
    columns = ", ".join([f'"{header}"' for header in headers])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS morning_and_evening ({columns})")

    for entry in data:
        placeholders = ", ".join(["?"] * len(headers))
        values = tuple(entry.values())
        cursor.execute(
            f"INSERT INTO morning_and_evening ({columns}) VALUES ({placeholders})",
            values,
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    paths = [("ar.json", "result/ar.sqlite"), ("en.json", "result/en.sqlite")]
    result_dir = "result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
        print(f"Created directory {result_dir}")
    for json_path, sqlite_path in paths:
        convert_json_to_sqlite(json_path, sqlite_path)
        print(f"Converted {json_path} to {sqlite_path}")
