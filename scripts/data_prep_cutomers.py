import pandas as pd
from data_scrubber import DataScrubber

# Load data
df = pd.read_csv("data//prepared/customers_data_prepared.csv")

# Create DataScrubber instance
scrubber = DataScrubber(df)

# Clean data
scrubber.remove_duplicate_records()
scrubber.handle_missing_data(fill_value="Unknown")
scrubber.convert_column_to_new_data_type("CustomerID", int)
scrubber.format_column_strings_to_lower_and_trim("Name")
scrubber.format_column_strings_to_upper_and_trim("Region")
scrubber.format_column_strings_to_lower_and_trim("PreferredContactMethod")

# Save data
scrubber.df.to_csv("data/prepared/customers_data_prepared.csv", index=False)