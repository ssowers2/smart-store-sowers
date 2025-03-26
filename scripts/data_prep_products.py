import pandas as pd
from data_scrubber import DataScrubber

# Load data
df = pd.read_csv("data//prepared/products_data_prepared.csv")

# Create DataScrubber instance
scrubber = DataScrubber(df)

# Clean data
scrubber.remove_duplicate_records()
scrubber.handle_missing_data(fill_value="Unknown")
scrubber.convert_column_to_new_data_type("ProductID", int)
scrubber.format_column_strings_to_upper_and_trim("ProductName")
scrubber.format_column_strings_to_upper_and_trim("Category")
scrubber.convert_column_to_new_data_type("UnitPrice", float)
scrubber.convert_column_to_new_data_type("StockQuantity", int)
scrubber.filter_column_outliers("StockQuantity", lower_bound=0, upper_bound=10000)
scrubber.format_column_strings_to_lower_and_trim("StoreSection")
scrubber.filter_column_outliers("UnitPrice", lower_bound=0.01, upper_bound=10000.00)

# Save data
scrubber.df.to_csv("data/prepared/products_data_prepared.csv", index=False)