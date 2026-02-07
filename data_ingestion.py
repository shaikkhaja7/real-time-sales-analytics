import pandas as pd
import sqlite3
import os

CSV_FILE = "data/live_sales.csv"
DB_FILE = "database/sales.db"
CHECKPOINT_FILE = "checkpoints/last_row.txt"

# Ensure checkpoint folder exists
os.makedirs("checkpoints", exist_ok=True)

# Read last processed row
if os.path.exists(CHECKPOINT_FILE):
    with open(CHECKPOINT_FILE, "r") as f:
        last_row = int(f.read().strip())
else:
    last_row = 0

# Read CSV
df = pd.read_csv(CSV_FILE)

# Get only new rows
new_data = df.iloc[last_row:]

if new_data.empty:
    print("No new data to ingest")
    exit()

# Connect to database
conn = sqlite3.connect(DB_FILE)

# Create table if not exists
conn.execute("""
CREATE TABLE IF NOT EXISTS sales (
    timestamp TEXT,
    product TEXT,
    price INTEGER,
    quantity INTEGER
)
""")

# Insert only new rows
new_data.to_sql("sales", conn, if_exists="append", index=False)

# Update checkpoint
with open(CHECKPOINT_FILE, "w") as f:
    f.write(str(len(df)))

conn.close()

print(f"Ingested {len(new_data)} new rows")

