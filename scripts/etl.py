import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("data/OnlineRetail.csv", encoding="ISO-8859-1")

# Drop missing CustomerID
df.dropna(subset=["CustomerID"], inplace=True)

# Create Total Amount
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# Connect to SQLite Data Warehouse
conn = sqlite3.connect("warehouse/ecommerce_dw.db")

# Load Fact Table
df[["CustomerID", "InvoiceNo", "Quantity", "TotalAmount", "InvoiceDate"]].to_sql(
    "Fact_Sales", conn, if_exists="replace", index=False
)

conn.close()
print("ETL Process Completed Successfully")
