-- Create dimension tables
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_key INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    region VARCHAR(100),
    UNIQUE(customer_id)
);

CREATE TABLE IF NOT EXISTS dim_products (
    product_key INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    product_name VARCHAR(255),
    category VARCHAR(100),
    unit_price DECIMAL(10, 2),
    UNIQUE(product_id)
);

-- Create fact table
CREATE TABLE IF NOT EXISTS fact_sales (
    sale_key INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    customer_key INT,
    product_key INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    total_amount DECIMAL(10, 2),
    order_date DATE,
    UNIQUE(order_id),
    FOREIGN KEY (customer_key) REFERENCES dim_customers(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_products(product_key)
);