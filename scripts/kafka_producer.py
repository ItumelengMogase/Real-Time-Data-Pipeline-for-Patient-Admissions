import json
import time
from kafka import KafkaProducer
import random
from datetime import datetime

# Kafka producer setup
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Simulate patient admissions
def simulate_patient_admissions():
    patient_ids = ["P001", "P002", "P003", "P004"]
    admission_types = ["Emergency", "Routine", "Surgery"]
    while True:
        event = {
            "PatientID": random.choice(patient_ids),
            "AdmissionType": random.choice(admission_types),
            "AdmissionStartDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        producer.send('patient_admissions', event)
        print(f"Sent: {event}")
        time.sleep(5)  # Adjust for real-time simulation

if __name__ == "__main__":
    simulate_patient_admissions()
