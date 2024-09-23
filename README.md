# Real-Time Data Pipeline for Patient Admissions

## Project Overview

This project sets up a **real-time data ingestion pipeline** for patient admissions using **Kafka**, **Spark Streaming**, **PostgreSQL**, and **Airflow**. The pipeline processes simulated patient admissions (e.g., emergency, routine, surgery) and stores them in a PostgreSQL database, allowing real-time processing. We use **PowerBI** for visualising admission trends.

### Objectives:
- Simulate real-time patient admission events using Kafka.
- Process and load the streaming data into PostgreSQL using Spark Streaming.
- Orchestrate tasks and monitor the pipeline using Airflow.
- Visualise the data trends with PowerBI.

## Project Structure

```plaintext
Real-Time-Data-Pipeline-for-Patient-Admissions/
├── airflow/                      # Airflow-related DAGs and configurations
│   └── dags/
│       └── patient_admissions_dag.py
├── data/                         # Example datasets or configuration files (optional)
│   └── patient_data.csv
├── docker/                       # Docker configurations for Kafka, Zookeeper, Spark, etc.
│   └── docker-compose.yml
├── kafka_producer/               # Kafka producer script
│   └── kafka_producer.py
├── spark_streaming/              # Spark Streaming job
│   └── spark_streaming.py
├── README.md                     # Your project documentation
└── requirements.txt              # List of Python dependencies for the project
