import pandas as pd
from datetime import datetime

def transform_data(customers, products, sales):
    """Clean and transform the data"""
    try:
        # Clean customers data
        customers = customers.drop_duplicates('customer_id')
        customers['email'] = customers['email'].str.lower().str.strip()
        
        # Clean products data
        products = products.drop_duplicates('product_id')
        products['product_name'] = products['product_name'].str.strip()
        products['category'] = products['category'].str.strip()
        products['unit_price'] = pd.to_numeric(products['unit_price'], errors='coerce')
        
        # Clean sales data
        sales = sales.drop_duplicates('order_id')
        sales['order_date'] = pd.to_datetime(sales['order_date']).dt.date
        sales['quantity'] = pd.to_numeric(sales['quantity'], errors='coerce')
        
        # Join sales with products to get unit_price
        sales = sales.merge(
            products[['product_id', 'unit_price']], 
            on='product_id', 
            how='left'
        )
        
        # Calculate total amount
        sales['total_amount'] = sales['quantity'] * sales['unit_price']
        
        # Drop rows with missing critical data
        sales = sales.dropna(subset=['customer_id', 'product_id', 'quantity', 'total_amount'])
        
        print("Data transformed successfully")
        return customers, products, sales
        
    except Exception as e:
        print(f"Error transforming data: {e}")
        raise

if __name__ == '__main__':
    # For testing
    from extract import extract_data
    customers, products, sales = extract_data()
    customers, products, sales = transform_data(customers, products, sales)
    print(sales.head())