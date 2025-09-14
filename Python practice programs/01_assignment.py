import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",  # replace with your actual password
    database="employees"
)

cursor = conn.cursor(dictionary=True)

def fetch_large_data(query, chunk_size=10000):
    cursor.execute(query)
    while True:
        rows = cursor.fetchmany(chunk_size)
        if not rows:
            break
        for row in rows:
            yield row

query = "SELECT emp_no, first_name, last_name FROM employees"

for row in fetch_large_data(query):
    print(row)

cursor.close()
conn.close()
