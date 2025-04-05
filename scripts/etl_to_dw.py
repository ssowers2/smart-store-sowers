import sqlite3
import pandas as pd
import pathlib

# Set database path
DB_PATH = pathlib.Path("data").joinpath("dw").joinpath("smart_sales.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)  # ensure folder exists

def create_schema(cursor: sqlite3.Cursor) -> None:
    cursor.executescript("""
        DROP TABLE IF EXISTS sale;
        DROP TABLE IF EXISTS customer;
        DROP TABLE IF EXISTS product;

        CREATE TABLE customer (
            customer_id TEXT PRIMARY KEY,
            name TEXT,
            region TEXT,
            join_date DATE,
            loyalty_points INTEGER,
            preferred_contact_method TEXT
        );

        CREATE TABLE product (
            product_id TEXT PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            unit_price REAL,
            stock_quantity INTEGER,
            store_section TEXT
        );

        CREATE TABLE sale (
            transaction_id TEXT PRIMARY KEY,
            sale_date DATE,
            customer_id TEXT,
            product_id TEXT,
            store_id TEXT,
            campaign_id TEXT,
            sale_amount REAL,
            discount_percent REAL,
            payment_type TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
            FOREIGN KEY (product_id) REFERENCES product(product_id)
        );
    """)

def load_data(cursor: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    # Load CSV
    customers_df = pd.read_csv("data/prepared/customers_data_prepared.csv")
    products_df = pd.read_csv("data/prepared/products_data_prepared.csv")
    sales_df = pd.read_csv("data/prepared/sales_data_prepared.csv")

    # Rename columns to match schema
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

    # Filter out sales with missing customer or product references that were deleted during cleaning process
    sales_df = sales_df[
        sales_df["customer_id"].isin(customers_df["customer_id"]) &
        sales_df["product_id"].isin(products_df["product_id"])
    ]

    # Load data into the database with corrected table names
    customers_df.to_sql("customer", conn, if_exists="append", index=False)
    products_df.to_sql("product", conn, if_exists="append", index=False)
    sales_df.to_sql("sale", conn, if_exists="append", index=False)

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    create_schema(cursor)
    load_data(cursor, conn)

    conn.commit()
    conn.close()
    print("The data warehouse was successfully created!")

if __name__ == "__main__":
    main()