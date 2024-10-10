# Real-Time Data Pipeline for Patient Admissions

## Project Overview

This project establishes a **real-time data ingestion pipeline** for patient admissions using a variety of tools, including **Apache Kafka**, **Spark Streaming**, **PostgreSQL**, **Airflow**, **Kafka Connect**, **Schema Registry**, **REST Proxy**, **Kafdrop**, and **KSQLDB**. The pipeline simulates patient admission data (demographics, diagnoses, lab results) and processes it in real-time, storing the data in a PostgreSQL database. **PowerBI** is used for visualising admission trends and medical data insights.

### Key Objectives:
- **Simulate real-time patient admission events** with Kafka.
- **Process streaming data** using Spark and store it in PostgreSQL.
- **Orchestrate and automate tasks** using Airflow.
- **Visualise trends** in patient admissions with PowerBI.
  
---

## Data Flow Architecture

### 1. **Data Generation**:
   - **KSQL Datagen** generates synthetic patient admission data based on defined characteristics (gender, race, medical history, lab results, etc.).
   - The data is structured into multiple topics in Kafka (e.g., `patient_admissions`, `patient_diagnoses`, `patient_labs`).

### 2. **Kafka Topics and Schema Registry**:
   - **Kafka** acts as the messaging broker for streaming patient data in real-time.
   - Each patient data type (e.g., admissions, diagnoses, labs) is published into a corresponding Kafka topic.
   - **Schema Registry** ensures consistent data formats across these topics using Avro schemas.

### 3. **Data Ingestion**:
   - **Kafka Connect** connects Kafka topics to external systems (e.g., PostgreSQL) and continuously ingests streaming data.
   - **REST Proxy** provides an HTTP-based interface for producing and consuming data from Kafka topics if needed.

### 4. **Real-Time Processing with Spark**:
   - **Spark Streaming** processes patient admission events in real-time from Kafka.
   - The processed data is cleaned and transformed before being written to a **PostgreSQL** database.

### 5. **Airflow Orchestration**:
   - **Airflow** manages the entire pipeline, scheduling tasks for Spark streaming jobs, Kafka data ingestion, and database updates.
   - DAGs (Directed Acyclic Graphs) ensure that tasks run in a predefined sequence.

### 6. **Data Storage in PostgreSQL**:
   - Real-time data is stored in PostgreSQL for persistence and easy querying.
   - Tables include patient demographics, admissions, diagnoses, and lab results.

### 7. **Monitoring with Kafdrop**:
   - **Kafdrop** provides a UI for monitoring Kafka clusters, topics, partitions, and consumer groups.

### 8. **Data Visualisation**:
   - **PowerBI** connects to PostgreSQL to generate real-time visualisations and dashboards, displaying trends in patient admissions, diagnoses, and lab results.

---

## Project Structure

```plaintext
Real-Time-Data-Pipeline-for-Patient-Admissions/
│
├── dags/                           # Airflow DAGs for task orchestration
│   ├── kafka_to_postgres_dag.py    # Airflow DAG for Kafka to PostgreSQL ingestion
│   └── spark_processing_dag.py     # Airflow DAG for Spark Streaming jobs
│
├── scripts/                        # Python scripts and SQL for various tasks
│   ├── kafka_producer.py           # Custom Kafka producer script (if needed)
│   ├── spark_streaming.py          # Spark job for processing Kafka data
│   └── db_setup.sql                # SQL script for PostgreSQL table creation
│
├── docker-compose.yml              # Docker Compose for Kafka, PostgreSQL, Schema Registry, etc.
├── requirements.txt                # Python dependencies (Airflow, PySpark, etc.)
├── powerbi_dashboard.pbit          # PowerBI file for real-time data visualisation
└── README.md                       # Documentation for the project
```

---

## Prerequisites

Ensure you have the following set up before running the pipeline:
1. **Docker**: To run Kafka, PostgreSQL, and other services in containers.
2. **Airflow**: To orchestrate the data pipeline.
3. **Spark**: For real-time processing of Kafka events.
4. **PowerBI**: To visualise the patient admission data.

---

## Setup and Execution

### 1. **Set Up Docker Services**:
   Use the `docker-compose.yml` file to spin up Kafka, PostgreSQL, Schema Registry, Kafdrop, and other services:
   ```bash
   docker-compose up -d
   ```

### 2. **Database Setup**:
   Run the `db_setup.sql` script to create the necessary tables in PostgreSQL:
   ```bash
   psql -h localhost -U postgres -d healthcare_pipeline_db -f scripts/db_setup.sql
   ```

### 3. **Simulate Data with KSQL Datagen**:
   Use KSQL Datagen to generate synthetic data for the Kafka topics:
   ```bash
   ksql-datagen quickstart=PATIENT_ADMISSIONS format=json topic=patient_admissions
   ```

### 4. **Run Airflow DAGs**:
   Start Airflow and trigger the DAGs to begin data ingestion and processing:
   ```bash
   airflow scheduler
   airflow trigger_dag kafka_to_postgres_dag
   airflow trigger_dag spark_processing_dag
   ```

### 5. **Monitor with Kafdrop**:
   Visit the Kafdrop UI to monitor Kafka topic activity:
   ```
   http://localhost:9000
   ```

### 6. **Visualise Data in PowerBI**:
   Use `powerbi_dashboard.pbit` to visualise the data trends from PostgreSQL.

---

## Future Enhancements
- Add **alerting** using Airflow or other monitoring tools for failed tasks or abnormal data patterns.
- Implement more complex transformations using **KSQLDB** or **Spark Structured Streaming**.
- Expand the visualisation layer to include more granular insights on patient data.

---
