import pandas as pd
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise

def load_data(customers, products, sales):
    """Load transformed data into MySQL database"""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Load customers
        for _, row in customers.iterrows():
            cursor.execute("""
                INSERT INTO dim_customers (customer_id, first_name, last_name, email, region)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    first_name = VALUES(first_name),
                    last_name = VALUES(last_name),
                    email = VALUES(email),
                    region = VALUES(region)
            """, (row['customer_id'], row['first_name'], row['last_name'], row['email'], row['region']))
        
        # Load products
        for _, row in products.iterrows():
            cursor.execute("""
                INSERT INTO dim_products (product_id, product_name, category, unit_price)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    product_name = VALUES(product_name),
                    category = VALUES(category),
                    unit_price = VALUES(unit_price)
            """, (row['product_id'], row['product_name'], row['category'], row['unit_price']))
        
        # Get customer and product keys for sales data
        customer_keys = pd.read_sql("SELECT customer_key, customer_id FROM dim_customers", conn)
        product_keys = pd.read_sql("SELECT product_key, product_id FROM dim_products", conn)
        
        # Merge keys with sales data
        sales_with_keys = sales.merge(
            customer_keys, 
            on='customer_id', 
            how='inner'
        ).merge(
            product_keys, 
            on='product_id', 
            how='inner'
        )
        
        # Load sales
        for _, row in sales_with_keys.iterrows():
            cursor.execute("""
                INSERT INTO fact_sales (order_id, customer_key, product_key, quantity, unit_price, total_amount, order_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    quantity = VALUES(quantity),
                    unit_price = VALUES(unit_price),
                    total_amount = VALUES(total_amount),
                    order_date = VALUES(order_date)
            """, (row['order_id'], row['customer_key'], row['product_key'], 
                  row['quantity'], row['unit_price'], row['total_amount'], row['order_date']))
        
        conn.commit()
        print("Data loaded successfully")
        
    except Error as e:
        if conn:
            conn.rollback()
        print(f"Error loading data: {e}")
        raise
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    # For testing
    from extract import extract_data
    from transform import transform_data
    customers, products, sales = extract_data()
    customers, products, sales = transform_data(customers, products, sales)
    load_data(customers, products, sales)