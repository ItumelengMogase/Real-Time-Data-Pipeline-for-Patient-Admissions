consumer = KafkaConsumer(
    'patient_admissions',
    bootstrap_servers='localhost:9092',
    group_id='patient_admission_group',  # Make sure this matches
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
