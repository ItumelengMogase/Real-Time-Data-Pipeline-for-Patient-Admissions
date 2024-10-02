from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

# Initialise Spark Session
spark = SparkSession.builder.appName("PatientAdmissions").getOrCreate()

# Define schema for Kafka messages
schema = StructType() \
    .add("PatientID", StringType()) \
    .add("AdmissionID", StringType()) \
    .add("AdmissionStartDate", StringType()) \
    .add("AdmissionEndDate", StringType()) \
    .add("PrimaryDiagnosisCode", StringType()) \
    .add("PrimaryDiagnosisDescription", StringType())

# Read from Kafka topic
admissions_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "admissions") \
    .load()

# Convert the data
admissions_df = admissions_stream.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Write to PostgreSQL
def write_to_postgres(df, epoch_id):
    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/healthcare_pipeline_db") \
        .option("dbtable", "medical_data.AdmissionsCorePopulatedTable") \
        .option("user", "itumeleng") \
        .option("password", "libra") \
        .mode("append") \
        .save()

admissions_df.writeStream.foreachBatch(write_to_postgres).start().awaitTermination()
