import sqlite3
import pandas as pd
from datetime import datetime, timedelta

DB_FILE = "database/sales.db"

# Connect to DB
conn = sqlite3.connect(DB_FILE)

# Load data
df = pd.read_sql("SELECT * FROM sales", conn)
conn.close()

if df.empty:
    print("No data available for analytics")
    exit()

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Revenue column
df["revenue"] = df["price"] * df["quantity"]

# KPI 1: Total Revenue
total_revenue = df["revenue"].sum()

# KPI 2: Total Orders
total_orders = len(df)

# KPI 3: Revenue by Product
revenue_by_product = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# KPI 4: Sales in last 1 minute
one_minute_ago = datetime.now() - timedelta(minutes=1)
recent_sales = df[df["timestamp"] >= one_minute_ago]

# Print results
print("\n📊 SALES ANALYTICS\n")
print(f"💰 Total Revenue: ₹{total_revenue:,.0f}")
print(f"📦 Total Orders: {total_orders}")

print("\n🛍️ Revenue by Product:")
print(revenue_by_product)

print(f"\n⏱️ Orders in Last 1 Minute: {len(recent_sales)}")

