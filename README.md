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
