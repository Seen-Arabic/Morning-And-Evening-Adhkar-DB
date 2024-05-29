import json
import os


def convert_json_to_sql(json_file, sql_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    headers = data[0].keys()
    columns = ", ".join([f'"{header}"' for header in headers])

    with open(sql_file, 'w', encoding='utf-8') as f:
        f.write(f"CREATE TABLE IF NOT EXISTS morning_and_evening ({columns});\n")

        for entry in data:
            values = ", ".join([f"'{value}'" for value in entry.values()])
            f.write(f"INSERT INTO morning_and_evening ({columns}) VALUES ({values});\n")


if __name__ == "__main__":
    paths = [("ar.json", "result/ar.sql"), ("en.json", "result/en.sql")]
    result_dir = "result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
        print(f"Created directory {result_dir}")
    for json_path, sql_path in paths:
        convert_json_to_sql(json_path, sql_path)
        print(f"Converted {json_path} to {sql_path}")
