import psycopg2

def test_postgres_connection():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            user="itumeleng",
            password="libra",
            host="postgres_db",  # This should match your docker-compose service name
            port="5432",
            database="healthcare_pipeline_db"
        )
        
        cursor = connection.cursor()
        
        # Execute a simple query to check the connection
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You're connected to - ", record)

    except Exception as error:
        print("Error while connecting to PostgreSQL:", error)
    
    finally:
        # Clean up and close the connection
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    test_postgres_connection()
