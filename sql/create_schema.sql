--Dimension Table: customers
CREATE TABLE customers (
    customerid TEXT PRIMARY KEY,
    name TEXT,
    region TEXT,
    joindate DATE,
    loyaltypoints INTEGER,
    preferredcontactmethod TEXT
);

--Dimension Table: products
CREATE TABLE products (
    productid TEXT PRIMARY KEY,
    productname TEXT,
    category TEXT,
    unitprice INTEGER,
    stockquantity INTEGER,
    storesection TEXT
);

--Fact Table: sales
CREATE TABLE sales (
    transactionid TEXT PRIMARY KEY,
    saledate DATE,
    customerid TEXT,
    productid TEXT, 
    storeid TEXT, 
    campaignid TEXT, 
    saleamount REAL, 
    discountpercent REAL,  
    paymenttype TEXT,
    FOREIGN KEY (customerid) REFERENCES customers(customerid),
    FOREIGN KEY (productid) REFERENCES products(productid)
);
