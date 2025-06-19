from create_schema import create_database
from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl_pipeline():
    """Run the complete ETL pipeline"""
    try:
        # Step 1: Ensure database and tables exist
        print("Checking/Creating database schema...")
        create_database()
        
        # Step 2: Extract data
        print("\nExtracting data...")
        customers, products, sales = extract_data()
        
        # Step 3: Transform data
        print("\nTransforming data...")
        customers, products, sales = transform_data(customers, products, sales)
        
        # Step 4: Load data
        print("\nLoading data...")
        load_data(customers, products, sales)
        
        print("\nETL pipeline completed successfully!")
        
    except Exception as e:
        print(f"\nETL pipeline failed: {e}")

if __name__ == '__main__':
    run_etl_pipeline()