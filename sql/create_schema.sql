-- Drop old tables
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS sale;

-- Create new schema with corrected column names
CREATE TABLE customer (
    customer_id TEXT PRIMARY KEY,
    name TEXT,
    region TEXT,
    join_date DATE,
    loyalty_points INTEGER,
    preferred_contact_method TEXT
);

CREATE TABLE product (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    unit_price REAL,
    stock_quantity INTEGER,
    store_section TEXT
);

CREATE TABLE sale (
    transaction_id TEXT PRIMARY KEY,
    sale_date DATE,
    customer_id TEXT,
    product_id TEXT,
    store_id TEXT,
    campaign_id TEXT,
    sale_amount REAL,
    discount_percent REAL,
    payment_type TEXT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);