import psycopg2
from kafka import KafkaProducer
import json
from datetime import datetime

# Database connection parameters
pg_conn_params = {
    'dbname': 'healthcare_pipeline_db',
    'user': 'itumeleng',
    'password': 'libra',
    'host': 'localhost',
    'port': '5432'
}

# Kafka parameters
kafka_broker = 'localhost:9092'
kafka_topic_admissions = 'patient_admissions'
kafka_topic_diagnoses = 'admissions_diagnoses'
kafka_topic_labs = 'labs_results'

# Connect to PostgreSQL
conn = psycopg2.connect(**pg_conn_params)
cursor = conn.cursor()

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_broker, 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def serialize_data(data):
    # Convert datetime objects to ISO format strings
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = value.isoformat()  # or any other preferred format
    return data

# Function to send data to Kafka
def send_to_kafka(query, topic):
    cursor.execute(query)
    for record in cursor.fetchall():
        data = {desc[0]: record[i] for i, desc in enumerate(cursor.description)}
        data = serialize_data(data)  # Serialize data before sending
        producer.send(topic, data)
        print(f"Sent to {topic}: {data}")

# Queries to get data
admissions_query = "SELECT * FROM medical_data.AdmissionsCorePopulatedTable;"
diagnoses_query = "SELECT * FROM medical_data.AdmissionsDiagnosesCorePopulatedTable;"
labs_query = "SELECT * FROM medical_data.LabsCorePopulatedTable;"

# Push patient admissions data
send_to_kafka(admissions_query, kafka_topic_admissions)

# Push admissions diagnoses data
send_to_kafka(diagnoses_query, kafka_topic_diagnoses)

# Push lab results data
send_to_kafka(labs_query, kafka_topic_labs)

# Clean up
cursor.close()
conn.close()
producer.flush()
producer.close()
