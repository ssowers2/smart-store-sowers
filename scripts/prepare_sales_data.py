import pandas as pd
import re

# Load raw data
df = pd.read_csv('data/raw/sales_data.csv')

# Strip column names of leading/trailing spaces
df.columns = df.columns.str.strip()

# Validate expected columns
expected_columns = [
    'TransactionID', 'SaleDate', 'CustomerID', 'ProductID',
    'StoreID', 'CampaignID', 'SaleAmount', 'DiscountPercent', 'PaymentType'
]
if list(df.columns) != expected_columns:
    raise ValueError(f"Unexpected columns: {df.columns.tolist()}")

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Convert SaleDate to datetime
df['SaleDate'] = pd.to_datetime(df['SaleDate'], errors='coerce')
df = df[df['SaleDate'].notna()]

# Convert numeric columns, fix if possible
df['SaleAmount'] = pd.to_numeric(df['SaleAmount'], errors='coerce')
df['DiscountPercent'] = pd.to_numeric(df['DiscountPercent'], errors='coerce')

# Drop rows with missing numeric values after attempted fix
df = df.dropna(subset=['SaleAmount', 'DiscountPercent'])

# Remove outliers from SaleAmount using IQR
Q1 = df['SaleAmount'].quantile(0.25)
Q3 = df['SaleAmount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['SaleAmount'] >= lower_bound) & (df['SaleAmount'] <= upper_bound)]

# Remove outliers from DiscountPercent (with upper sanity cap at 100%)
df = df[(df['DiscountPercent'] >= 0) & (df['DiscountPercent'] <= 100)]

# Normalize and fix typos
df['PaymentType'] = df['PaymentType'].str.lower().str.strip()

payment_type_corrections = {
    'cardgift': 'giftcard',
    'gift card': 'giftcard',
    'debt': 'debit',
    'cred': 'credit',
    'pay pal': 'paypal',
}
df['PaymentType'] = df['PaymentType'].replace(payment_type_corrections)

# Filter valid payment types
valid_payment_types = ['credit', 'debit', 'giftcard', 'paypal', 'cash']
df = df[df['PaymentType'].isin(valid_payment_types)]

# Save cleaned data
df.to_csv('data/prepared/sales_data_prepared.csv', index=False)
print("Sales data prepared and saved!")