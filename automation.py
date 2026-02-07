import time
import os

print("Starting automated ingestion... Press CTRL+C to stop.")

while True:
    os.system("python data_ingestion.py")
    time.sleep(10)

