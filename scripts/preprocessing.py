import pandas as pd
import sqlite3

# Connect to warehouse
conn = sqlite3.connect("warehouse/ecommerce_dw.db")

# Load required columns
query = """
SELECT CustomerID, InvoiceDate, TotalAmount
FROM Fact_Sales
"""

df = pd.read_sql(query, conn)
conn.close()

# Convert InvoiceDate to datetime (CRITICAL FIX)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# Drop invalid dates
df = df.dropna(subset=["InvoiceDate"])

# Feature Engineering
features = df.groupby("CustomerID").agg(
    Monetary=("TotalAmount", "sum"),
    FirstPurchase=("InvoiceDate", "min"),
    LastPurchase=("InvoiceDate", "max")
).reset_index()

# Time spent in days
features["TimeSpent"] = (
    features["LastPurchase"] - features["FirstPurchase"]
).dt.days

# Replace 0 or negative with 1
features.loc[features["TimeSpent"] <= 0, "TimeSpent"] = 1

# Keep only required columns
final_df = features[["CustomerID", "Monetary", "TimeSpent"]]

final_df.to_csv("data/customer_features.csv", index=False)

print("Customer Monetary & Time features created successfully")
print("Total customers:", final_df.shape[0])
