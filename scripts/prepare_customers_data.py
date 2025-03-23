import pandas as pd

# Load raw data
df = pd.read_csv('data/raw/customers_data.csv')

# Ensure column names are clean and expected
df.columns = df.columns.str.strip()
expected_columns = ['CustomerID', 'Name', 'Region', 'JoinDate', 'LoyaltyPoints', 'PreferredContactMethod']
if list(df.columns) != expected_columns:
    raise ValueError(f"Unexpected columns: {df.columns.tolist()}")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Clean and convert LoyaltyPoints
df['LoyaltyPoints'] = pd.to_numeric(df['LoyaltyPoints'], errors='coerce')
df = df.dropna(subset=['LoyaltyPoints'])
df['LoyaltyPoints'] = df['LoyaltyPoints'].astype(int)

# Remove outliers in LoyaltyPoints
Q1 = df['LoyaltyPoints'].quantile(0.25)
Q3 = df['LoyaltyPoints'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['LoyaltyPoints'] >= lower_bound) & (df['LoyaltyPoints'] <= upper_bound)]

# Convert JoinDate to datetime and remove invalid dates
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')
df = df[df['JoinDate'].notna()]

# Clean and standardize PreferredContactMethod
df['PreferredContactMethod'] = df['PreferredContactMethod'].str.lower().str.strip()

# Correct typos BEFORE filtering
contact_method_corrections = {
    'emal': 'email',
    'emial': 'email',
    'phne': 'phone'
}
df['PreferredContactMethod'] = df['PreferredContactMethod'].replace(contact_method_corrections)

# Keep valid methods after correction
valid_methods = ['email', 'text', 'phone']
df = df[df['PreferredContactMethod'].isin(valid_methods)]

# Validate Region values
valid_regions = ['East', 'West', 'North', 'South']
df = df[df['Region'].isin(valid_regions)]

# Save cleaned data
df.to_csv('data/prepared/customers_data_prepared.csv', index=False)
print("Customers data prepared and saved!")