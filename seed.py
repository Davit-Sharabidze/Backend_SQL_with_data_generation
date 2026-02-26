import random
import numpy as np
from db import get_connection


def generate_customers(n):
    conn = get_connection()
    cur = conn.cursor()
    countries = ["USA", "Germany", "Italy", "UK", "Canada"]

    for i in range(n):
        name = f"Customer-{i}"
        email = f"customer_{i}@example.com"
        country = random.choice(countries)

        cur.execute("""
            INSERT INTO customers (name, email, country)
            VALUES (%s, %s, %s)
        """, (name, email, country))

    conn.commit()
    cur.close()
    conn.close()


def generate_order_items(n):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM orders;")
    order_ids = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT id FROM products;")
    product_ids = [row[0] for row in cur.fetchall()]

    rng = np.random.default_rng()
    for _ in range(n):
        order_id = random.choice(order_ids)
        product_id = random.choice(product_ids)
        quantity = int(rng.integers(1, 5))

        cur.execute("""
            INSERT INTO order_items (order_id, product_id, quantity)
            VALUES (%s, %s, %s)
        """, (order_id, product_id, quantity))

    conn.commit()
    cur.close()
    conn.close()


def generate_products(n):
    conn = get_connection()
    cur = conn.cursor()
    products = ["Laptop", "Mechanical keyboard", "Mouse", "Desktop Computer","Wi-Fi Router","Headphones","Monitor"]
    for i in range(n):
        rng = np.random.default_rng()
        name = random.choice(products) 
        if name in ["Laptop","Desktop Computer","Monitor"]:
            price = int(rng.integers(1000,3501))
        else: price = int(rng.integers(50,200))

        cur.execute("""
            INSERT INTO products (name, price)
            VALUES (%s, %s)
        """, (name, price))

    conn.commit()
    cur.close()
    conn.close()


def generate_orders(n):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM customers;")
    customer_ids = [row[0] for row in cur.fetchall()]

    for _ in range(n):
        customer_id = random.choice(customer_ids)

        cur.execute("""
            INSERT INTO orders (customer_id)
            VALUES (%s)
        """, (customer_id,))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    generate_customers(100)
    generate_products(20)
    generate_orders(200)
    generate_order_items(400)