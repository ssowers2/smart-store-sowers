import sqlite3

with open("sql/create_schema.sql", "r") as f:
    schema = f.read()

conn = sqlite3.connect("warehouse.db")
conn.executescript(schema)
conn.close()

print("Schema created successfully!")
