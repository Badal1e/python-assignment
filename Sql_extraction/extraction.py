import re
import json
import sys
import os

# Get input SQL file path from command line
if len(sys.argv) != 2:
    print("Usage: python extraction.py <sql_file>")
    sys.exit(1)

sql_file = sys.argv[1]

if not os.path.isfile(sql_file):
    print(f"File '{sql_file}' not found!")
    sys.exit(1)

# Read the SQL file content
with open(sql_file, 'r', encoding='utf-8') as f:
    sql_text = f.read()

# Extract information using regex
# Example: table names, columns, and stored procedure names
procedure_match = re.search(r'CREATE\s+PROCEDURE\s+(\w+)', sql_text, re.IGNORECASE)
tables_match = re.findall(r'FROM\s+(\w+)|JOIN\s+(\w+)|INTO\s+(\w+)', sql_text, re.IGNORECASE)
columns_match = re.findall(r'SELECT\s+(.*?)\s+FROM', sql_text, re.IGNORECASE | re.DOTALL)

procedure_name = procedure_match.group(1) if procedure_match else "UnknownProcedure"
tables = [t for group in tables_match for t in group if t]
columns = [col.strip() for col_group in columns_match for col in col_group.split(',') if col.strip()]

# Prepare output dictionary
extracted_info = {
    "ProcedureName": procedure_name,
    "Tables": tables,
    "Columns": columns
}

# Create output JSON file
json_file = os.path.splitext(sql_file)[0] + ".json"
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(extracted_info, f, indent=4)

print(f"Extraction completed! JSON saved as '{json_file}'")
