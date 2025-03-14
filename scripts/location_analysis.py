import pandas as pd

# Load CSC file info Data Frame
df= pd.read_csv('./data/raw/customers_data.csv')

# Find the most common customer location
common_location = df['Region'].mode()[0]
print(f"The most common customer location is: {common_location}")
