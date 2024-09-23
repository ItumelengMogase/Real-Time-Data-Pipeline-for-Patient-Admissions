from kafka import KafkaProducer
import json
import time

# Configuration
KAFKA_BROKER = 'localhost:9092'  # Change if needed
TOPIC_NAME = 'patient_admissions'  # Change to your desired topic name

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialise messages to JSON
)

# Function to send messages
def send_messages():
    for i in range(10):  # Adjust the range for the number of messages
        message = {'number': i, 'message': f'This is message {i}'}
        producer.send(TOPIC_NAME, value=message)
        print(f'Sent: {message}')
        time.sleep(1)  # Sleep for a second between messages

# Main execution
if __name__ == '__main__':
    try:
        send_messages()
    finally:
        producer.close()
