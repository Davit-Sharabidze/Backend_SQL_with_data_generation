from db import get_connection

def total_revenue_per_customer():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            c.name,
            SUM(p.price * oi.quantity) AS total_spent
        FROM customers c
        JOIN orders o ON c.id = o.customer_id
        JOIN order_items oi ON o.id = oi.order_id
        JOIN products p ON oi.product_id = p.id
        GROUP BY c.name
        ORDER BY total_spent DESC;
    """)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    conn.close()

if __name__ == "__main__":
    total_revenue_per_customer()