import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("warehouse.db")

# Load CSVs
customers_df = pd.read_csv("data/prepared/customers_data_prepared.csv")
products_df = pd.read_csv("data/prepared/products_data_prepared.csv")
sales_df = pd.read_csv("data/prepared/sales_data_prepared.csv")

# Rename columns to use lowercase with underscores
customers_df.rename(columns={
    "CustomerID": "customer_id",
    "Name": "name",
    "Region": "region",
    "JoinDate": "join_date",
    "LoyaltyPoints": "loyalty_points",
    "PreferredContactMethod": "preferred_contact_method"
}, inplace=True)

products_df.rename(columns={
    "ProductID": "product_id",
    "ProductName": "product_name",
    "Category": "category",
    "UnitPrice": "unit_price",
    "StockQuantity": "stock_quantity",
    "StoreSection": "store_section"
}, inplace=True)

sales_df.rename(columns={
    "TransactionID": "transaction_id",
    "SaleDate": "sale_date",
    "CustomerID": "customer_id",
    "ProductID": "product_id",
    "StoreID": "store_id",
    "CampaignID": "campaign_id",
    "SaleAmount": "sale_amount",
    "DiscountPercent": "discount_percent",
    "PaymentType": "payment_type"
}, inplace=True)

# Load data into tables
customers_df.to_sql("customers", conn, if_exists="append", index=False)
products_df.to_sql("products", conn, if_exists="append", index=False)
sales_df.to_sql("sales", conn, if_exists="append", index=False)

# Close the connection
conn.close()

# Confirm success
print("Data loaded into warehouse.db successfully!")
