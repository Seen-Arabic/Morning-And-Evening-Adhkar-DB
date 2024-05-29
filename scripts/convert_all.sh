#!/bin/bash

# Define the result directory
RESULT_DIR="result"

# Create the result directory if it does not exist
if [ ! -d "$RESULT_DIR" ]; then
  mkdir -p "$RESULT_DIR"
  echo "Created directory $RESULT_DIR"
fi

# Run the Python scripts
echo "Running convert_to_csv.py..."
python scripts/convert_to_csv.py

echo "Running convert_to_sqlite.py..."
python scripts/convert_to_sqlite.py

echo "Running convert_to_sql.py..."
python scripts/convert_to_sql.py

cp ar.json $RESULT_DIR
echo "Copied ar.json to $RESULT_DIR"

cp en.json $RESULT_DIR
echo "Copied en.json to $RESULT_DIR"

echo "All conversions completed."
