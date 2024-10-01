from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PatientAdmissionStreaming") \
    .config("spark.jars", "/path/to/postgresql-42.2.18.jar") \
    .getOrCreate()

# Define schema for patient admissions
schema = StructType() \
    .add("PatientID", "string") \
    .add("AdmissionType", "string") \
    .add("AdmissionStartDate", "string")

# Read from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "patient_admissions") \
    .load()

# Parse the Kafka value
df = df.selectExpr("CAST(value AS STRING)")
df = df.withColumn("jsonData", from_json(col("value"), schema)).select("jsonData.*")

# Write to PostgreSQL
def write_to_postgres(df, epoch_id):
    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/healthcare_pipeline_db") \
        .option("dbtable", "AdmissionsCorePopulatedTable") \
        .option("user", "itumeleng") \
        .option("password", "libra") \
        .mode("append") \
        .save()

# Start streaming query
query = df.writeStream \
    .foreachBatch(write_to_postgres) \
    .start()

query.awaitTermination()
