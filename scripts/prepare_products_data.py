import pandas as pd
import re

# Load raw data
df = pd.read_csv('data/raw/products_data.csv')

# Clean and validate column names
df.columns = df.columns.str.strip()
expected_columns = ['ProductID', 'ProductName', 'Category', 'UnitPrice', 'StockQuanity', 'StoreSection']
if list(df.columns) != expected_columns:
    raise ValueError(f"Unexpected columns: {df.columns.tolist()}")

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Fix or drop invalid StockQuanity
def fix_quantity(val):
    try:
        return int(val)
    except:
        match = re.search(r'\d+', str(val))
        return int(match.group()) if match else pd.NA

df['StockQuanity'] = df['StockQuanity'].apply(fix_quantity)
df = df.dropna(subset=['StockQuanity'])
df['StockQuanity'] = df['StockQuanity'].astype(int)

# Convert UnitPrice to numeric and drop invalids
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
df = df.dropna(subset=['UnitPrice'])

# Remove outliers from UnitPrice using IQR
Q1 = df['UnitPrice'].quantile(0.25)
Q3 = df['UnitPrice'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['UnitPrice'] >= lower_bound) & (df['UnitPrice'] <= upper_bound)]

# Normalize and correct StoreSection values
# Step 1: Normalize to lowercase for consistent correction
df['StoreSection'] = df['StoreSection'].str.strip().str.lower()

# Step 2: Apply known misspelling corrections
section_corrections = {
    'sport': 'sports',
    'sprots': 'sports',
    'soprts': 'sports',
    'apperal': 'apparel',
    'apprel': 'apparel',
    'gamingg': 'gaming',
    'gamming': 'gaming',
    'gagdets': 'gadgets',
    'gadets': 'gadgets',
    'gadgets and': 'gadgets'
}
df['StoreSection'] = df['StoreSection'].replace(section_corrections)

# Step 3: Title-case for consistency
df['StoreSection'] = df['StoreSection'].str.title()

# Step 4: Filter to keep only valid values
valid_sections = ['Sports', 'Apparel', 'Gaming', 'Gadgets']
df = df[df['StoreSection'].isin(valid_sections)]

# Save cleaned data
df.to_csv('data/prepared/products_data_prepared.csv', index=False)
print("Products data prepared and saved!")