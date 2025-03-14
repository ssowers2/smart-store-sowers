import pandas as pd

# Load CSC file info Data Frame
df = pd.read_csv('./data/raw/sales_data.csv')

# Calculate average sales
average_sales = df['SaleAmount'].mean()
print(f"The average sales is: {average_sales}")

# Calculate minimum sales
min_sales = df['SaleAmount'].min()
print(f"The minimum sales is: {min_sales}")

# Calculate maximum sales
max_sales = df['SaleAmount'].max()
print(f"The maximum sales is: {max_sales}")