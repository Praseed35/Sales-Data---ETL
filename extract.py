import pandas as pd
from config import DATA_FILES

def extract_data():
    """Extract data from CSV files"""
    try:
        customers = pd.read_csv(DATA_FILES['customers'])
        products = pd.read_csv(DATA_FILES['products'])
        sales = pd.read_csv(DATA_FILES['sales'])
        
        print("Data extracted successfully")
        return customers, products, sales
        
    except Exception as e:
        print(f"Error extracting data: {e}")
        raise

if __name__ == '__main__':
    customers, products, sales = extract_data()
    print(customers.head())