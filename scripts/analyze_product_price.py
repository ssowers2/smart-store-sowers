import pandas as pd

# Load CSC file info Data Frame
df = pd.read_csv('./data/raw/products_data.csv')

# Find highest product price
highest_price = df['UnitPrice'].max()
print(f"The highest product price is: {highest_price}")

# Find lowest product price
lowest_price = df['UnitPrice'].min()
print(f"The lowest product price is: {lowest_price}")
