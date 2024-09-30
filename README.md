# Real-Time Data Pipeline for Patient Admissions

## Project Overview

This project sets up a **real-time data ingestion pipeline** for patient admissions using **Kafka**, **Spark Streaming**, **PostgreSQL**, and **Dagster**. The pipeline processes simulated patient admissions (e.g., emergency, routine, surgery) and stores them in a PostgreSQL database, allowing real-time processing. We use **PowerBI** for visualising admission trends.

### Objectives:
- Simulate real-time patient admission events using Kafka.
- Process and load the streaming data into PostgreSQL using Spark Streaming.
- Orchestrate tasks and monitor the pipeline using Dagster.
- Visualise the data trends with PowerBI.

## Project Structure

```plaintext
Real-Time-Data-Pipeline-for-Patient-Admissions/
│
├── dags/                    # Airflow DAGs for orchestration
├── scripts/                 # Python scripts for Kafka producer, Spark jobs
│   ├── kafka_producer.py    # Simulates patient admissions to Kafka
│   ├── spark_streaming.py   # Spark streaming job for processing Kafka events
│   └── db_setup.sql         # SQL script for PostgreSQL table creation
├── docker-compose.yml       # Docker Compose for Kafka, PostgreSQL, Airflow
├── requirements.txt         # Python dependencies (Dagster, Airflow, etc.)
├── powerbi_dashboard.pbit   # PowerBI file for data visualisation
└── README.md                # Documentation for GitHub

