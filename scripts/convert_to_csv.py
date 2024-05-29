import json
import csv
import os


def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # Write header
        writer.writerow(data[0].keys())
        # Write data
        for entry in data:
            writer.writerow(entry.values())


if __name__ == "__main__":
    paths = [("ar.json", "result/ar.csv"), ("en.json", "result/en.csv")]
    result_dir = "result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
        print(f"Created directory {result_dir}")
    for json_path, csv_path in paths:
        convert_json_to_csv(json_path, csv_path)
        print(f"Converted {json_path} to {csv_path}")
