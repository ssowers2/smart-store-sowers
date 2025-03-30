import sqlite3
import pandas as pd

# conn to SQLite db
conn = sqlite3.connect("warehouse.db")

# load csv data files into warehouse
customers_df = pd.read_csv("data/prepared/customers_data_prepared.csv")
products_df = pd.read_csv("data/prepared/products_data_prepared.csv")
sales_df = pd.read_csv("data/prepared/sales_data_prepared.csv")

# write each DataFrame to the appropriate table
customers_df.to_sql("customers", conn, if_exists="append", index=False)
products_df.to_sql("products", conn, if_exists="append", index=False)
sales_df.to_sql("sales", conn, if_exists="append", index=False)

# connion closed between this python code and the SQLite database
conn.close()

# confirmation data was loaded
print ("Data loaded into warehouse.db successfully!")
