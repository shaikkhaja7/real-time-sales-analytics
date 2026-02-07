import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import time

DB_FILE = "database/sales.db"

st.set_page_config(page_title="Real-Time Sales Dashboard", layout="wide")
st.title("📊 Real-Time Sales Analytics Dashboard")

# Auto refresh
REFRESH_INTERVAL = 5  # seconds

def load_data():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    return df

df = load_data()

if df.empty:
    st.warning("No data available yet...")
else:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["revenue"] = df["price"] * df["quantity"]

    # KPIs
    total_revenue = df["revenue"].sum()
    total_orders = len(df)
    aov = total_revenue / total_orders

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
    col2.metric("📦 Total Orders", total_orders)
    col3.metric("🧾 Avg Order Value", f"₹{aov:,.0f}")

    st.divider()

    # Revenue by product
    st.subheader("🛍️ Revenue by Product")
    revenue_by_product = df.groupby("product")["revenue"].sum()
    st.bar_chart(revenue_by_product)

    st.divider()

    # Recent sales
    st.subheader("⏱️ Recent Sales (Last 1 Minute)")
    one_minute_ago = datetime.now() - timedelta(minutes=1)
    recent_sales = df[df["timestamp"] >= one_minute_ago]
    st.dataframe(recent_sales.tail(10), use_container_width=True)

# Refresh dashboard
time.sleep(REFRESH_INTERVAL)
st.rerun()

