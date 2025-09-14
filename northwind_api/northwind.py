from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="assignment_northwind"
)
db_cursor = db_conn.cursor()

@app.route("/customers", methods=["POST"])
def add_customer():
    info = request.json
    sql = "INSERT INTO customers (CustomerName, ContactName, Country) VALUES (%s, %s, %s)"
    db_cursor.execute(sql, (info['CustomerName'], info.get('ContactName'), info['Country']))
    db_conn.commit()
    return jsonify({"status": "success", "message": "New customer added"}), 201

@app.route("/customers/<int:customer_id>", methods=["PUT"])
def modify_customer(customer_id):
    info = request.json
    sql = "UPDATE customers SET CustomerName=%s, ContactName=%s, Country=%s WHERE CustomerID=%s"
    db_cursor.execute(sql, (info.get('CustomerName'), info.get('ContactName'), info.get('Country'), customer_id))
    db_conn.commit()
    return jsonify({"status": "success", "message": "Customer info updated"})

@app.route("/customers", methods=["GET"])
def fetch_customers():
    db_cursor.execute("SELECT * FROM customers")
    rows = db_cursor.fetchall()
    customers_list = []
    for row in rows:
        customer = {
            "CustomerID": row[0],
            "CustomerName": row[1],
            "ContactName": row[2],
            "Country": row[3]
        }
        customers_list.append(customer)
    return jsonify(customers_list)

if __name__ == "__main__":
    app.run(debug=True)