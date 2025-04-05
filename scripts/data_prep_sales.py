# imports from the Python standard library
import pandas as pd
from data_scrubber import DataScrubber

# Load data
df = pd.read_csv("data/prepared/sales_data_prepared.csv")

# Create DataScrubber instance
scrubber = DataScrubber(df)

# Clean data
scrubber.remove_duplicate_records()
scrubber.handle_missing_data(fill_value="Unknown")
scrubber.convert_column_to_new_data_type("TransactionID", int)
scrubber.convert_column_to_new_data_type("CustomerID", int)
scrubber.convert_column_to_new_data_type("ProductID", int)
scrubber.convert_column_to_new_data_type("SaleAmount", float)
scrubber.convert_column_to_new_data_type("DiscountPercent", int)

# Make sure date format is SQLite friendly
scrubber.df["SaleDate"] = pd.to_datetime(scrubber.df["SaleDate"], errors="coerce")
scrubber.df["SaleDate"] = scrubber.df["SaleDate"].dt.date.astype(str)

# Format payment type
scrubber.format_column_strings_to_lower_and_trim("PaymentType")

# Filter outliers
scrubber.filter_column_outliers("SaleAmount", lower_bound=0.01, upper_bound=5000)
scrubber.filter_column_outliers("DiscountPercent", lower_bound=0, upper_bound=100)

# Filter invalid foreign keys before saving
customers_df = pd.read_csv("data/prepared/customers_data_prepared.csv")
products_df = pd.read_csv("data/prepared/products_data_prepared.csv")

# Save data
scrubber.df.to_csv("data/prepared/sales_data_prepared.csv", index=False)