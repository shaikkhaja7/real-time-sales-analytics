# Real-Time Sales Analytics & Monitoring System

This project demonstrates a beginner-friendly **real-time data analytics system** built using Python.  
It simulates live sales data, automatically processes it, stores it in a database, and displays insights on a live dashboard.

---

## 📌 Project Overview

In real companies, sales data is generated continuously.  
This project recreates that scenario by:

- Generating live sales data every few seconds
- Automatically ingesting only new data
- Storing data safely in a database
- Calculating business metrics (KPIs)
- Displaying everything on a real-time dashboard

---

## 🏗️ System Architecture

Data Generator
↓
CSV File
↓
Automated Ingestion
↓
SQLite Database
↓
Analytics Logic
↓
Streamlit Dashboard


---

## ✨ Features

- Live sales data simulation
- Automated ETL pipeline
- Duplicate-safe ingestion using checkpoints
- Business analytics (revenue, orders, AOV)
- Real-time Streamlit dashboard
- Clean and modular project structure

---

## 🛠️ Tech Stack

- Python
- Pandas
- SQLite
- Streamlit

---

## 📂 Project Structure

real_time_sales_analytics/
│
├── data_generator.py # Generates live sales data
├── data_ingestion.py # Inserts new data into database
├── automation.py # Runs ingestion automatically
│
├── analytics/
│ └── analytics_engine.py # Business metrics logic
│
├── dashboard/
│ └── app.py # Streamlit dashboard
│
├── data/ # CSV data (ignored in GitHub)
├── database/ # SQLite DB (ignored in GitHub)
├── checkpoints/ # Ingestion checkpoint
│
├── README.md
└── .gitignore


---

## ▶️ How to Run the Project

```bash
# Activate environment
source venv/bin/activate

# Start data generation
python data_generator.py

# In new terminal: start automation
python automation.py

# In new terminal: start dashboard
streamlit run dashboard/app.py
