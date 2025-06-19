# 📊 Sales Data Warehouse - ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-yellowgreen)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

A robust ETL pipeline that processes sales transactions into an analytical data warehouse with star schema design.

## 🌟 Key Features
- **Data Validation**: Automatic duplicate removal and missing value handling
- **Star Schema**: Optimized dimensional modeling for analytics
- **Idempotent Operations**: Safe for repeated executions
- **Data Quality Checks**: Unit price validation, negative quantity prevention

## 🏗️ Database Schema
```mermaid
erDiagram
    dim_customers ||--o{ fact_sales : "places"
    dim_products ||--o{ fact_sales : "contains"
    
    dim_customers {
        int customer_key PK
        int customer_id
        string first_name
        string last_name
        string email
        string region
    }
    
    dim_products {
        int product_key PK
        int product_id
        string product_name
        string category
        float unit_price
    }
    
    fact_sales {
        int sale_key PK
        int order_id
        int customer_key FK
        int product_key FK
        int quantity
        float unit_price
        float total_amount
        date order_date
    }

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MySQL 8.0+
- Git

### Installation & Setup
```bash
# Clone repository
git clone git@github.com:Praseed35/Sales-Data---ETL.git
cd Sales-Data---ETL

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure database (edit before running)
cp config.example.py config.py
