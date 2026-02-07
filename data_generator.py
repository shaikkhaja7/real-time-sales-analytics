import pandas as pd
import random
import time
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

file_path = "data/live_sales.csv"

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("timestamp,product,price,quantity\n")

products = ["Laptop", "Mobile", "Headphones", "Tablet", "Watch"]

while True:
    data = {
        "timestamp": datetime.now(),
        "product": random.choice(products),
        "price": random.randint(500, 50000),
        "quantity": random.randint(1, 5)
    }

    df = pd.DataFrame([data])
    df.to_csv(file_path, mode="a", header=False, index=False)

    print("New sale added")
    time.sleep(5)

