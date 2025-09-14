import json
import mysql.connector
import pandas as pd
import re

with open("sample_data_for_assignment.json", "r") as f:
    data_json = json.load(f)

columns = data_json['cols']
rows = data_json['data']

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="assignment_db"
)
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS json_to_sql_table")
cursor.execute("""
CREATE TABLE json_to_sql_table (
    id INT,
    name VARCHAR(50),
    email VARCHAR(100),
    postalZip VARCHAR(20),
    phone VARCHAR(20)
)
""")

insert_query = "INSERT INTO json_to_sql_table (id, name, email, postalZip, phone) VALUES (%s, %s, %s, %s, %s)"
for row in rows:
    cursor.execute(insert_query, tuple(row))
db.commit()
print("Data inserted into MySQL successfully!")

df = pd.read_sql("SELECT * FROM json_to_sql_table", con=db)
print("\nOriginal Data from MySQL:")
print(df)

df['email'] = 'abc@gmail.com'
df['postalZip'] = df['postalZip'].apply(lambda x: int(''.join(filter(str.isdigit, str(x)))))

def encode_phone(phone):
    digits = re.sub(r'\D', '', str(phone))
    code = ''
    for i in range(0, len(digits)-1, 2):
        num = int(digits[i:i+2])
        code += chr(num) if 65 <= num <= 99 else 'O'
    return code

df['coded_phone_number'] = df['phone'].apply(encode_phone)
df.drop(columns='phone', inplace=True)

print("\nProcessed DataFrame:")
print(df)
