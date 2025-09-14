import requests

BASE = "http://127.0.0.1:5000"

def test_customers_api():
    print("\n--- Customers API Tests ---")

    customer_data = {"CustomerName": "Sunny Corp", "ContactName": "Alice Ray", "Country": "USA"}
    res = requests.post(f"{BASE}/customers", json=customer_data)
    print("POST /customers:", res.json())

    update_data = {"CustomerName": "Sunny Corp Updated", "ContactName": "Alice R.", "Country": "USA"}
    res = requests.put(f"{BASE}/customers/1", json=update_data)
    print("PUT /customers/1:", res.json())

    res = requests.get(f"{BASE}/customers")
    print("GET /customers:", res.json())


def test_products_api():
    print("\n--- Products API Tests ---")

    product_data = {"ProductName": "Herbal Tea", "SupplierID": 1, "CategoryID": 1, "Unit": "15 boxes x 10 bags", "Price": 20.50}
    res = requests.post(f"{BASE}/products", json=product_data)
    print("POST /products:", res.json())

    update_data = {"ProductName": "Green Herbal Tea", "SupplierID": 1, "CategoryID": 1, "Unit": "20 boxes x 10 bags", "Price": 22.00}
    res = requests.put(f"{BASE}/products/1", json=update_data)
    print("PUT /products/1:", res.json())

    res = requests.get(f"{BASE}/products")
    print("GET /products:", res.json())


def test_orders_api():
    print("\n--- Orders API Tests ---")

    order_data = {"CustomerID": 1, "ProductID": 1, "Quantity": 10, "OrderDate": "2025-09-16"}
    res = requests.post(f"{BASE}/orders", json=order_data)
    print("POST /orders:", res.json())

    update_data = {"CustomerID": 1, "ProductID": 1, "Quantity": 12, "OrderDate": "2025-09-17"}
    res = requests.put(f"{BASE}/orders/1", json=update_data)
    print("PUT /orders/1:", res.json())

    res = requests.get(f"{BASE}/orders")
    print("GET /orders:", res.json())


def test_order_history_api(customer_id):
    print(f"\n--- Order History for Customer ID {customer_id} ---")
    res = requests.get(f"{BASE}/orders/history/{customer_id}")
    print(f"GET /orders/history/{customer_id}:", res.json())


if __name__ == "__main__":
    test_customers_api()
    test_products_api()
    test_orders_api()
    test_order_history_api(1)
