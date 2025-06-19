import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def create_database():
    """Create database if it doesn't exist"""
    try:
        # Connect without specifying database
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute(f"SHOW DATABASES LIKE '{DB_CONFIG['database']}'")
        result = cursor.fetchone()
        
        if not result:
            cursor.execute(f"CREATE DATABASE {DB_CONFIG['database']}")
            print(f"Database {DB_CONFIG['database']} created successfully")
        else:
            print(f"Database {DB_CONFIG['database']} already exists")
            
        # Switch to our database
        cursor.execute(f"USE {DB_CONFIG['database']}")
        
        # Create tables
        with open('queries/create_tables.sql', 'r') as file:
            sql_script = file.read()
        
        # Execute multiple statements
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        conn.commit()
        print("Tables created successfully")
        
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    create_database()