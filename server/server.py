import time
import psycopg2

# Connection parameters for PostgreSQL
hostname = 'host.docker.internal'
port = 5432
database = 'postgres'
username = 'postgres'
password = 'password'

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host=hostname,
    port=port,
    database=database,
    user=username,
    password=password
)

# Create a cursor object
cursor = connection.cursor()


def generate_sensor_data():
    # Generating random temperature and humidity values
    import random
    temperature = random.uniform(80, 100)
    humidity = random.randint(40, 60)

    # Store the generated data in the database
    query = "INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s)"
    values = (temperature, humidity)
    cursor.execute(query, values)
    connection.commit()


if __name__ == '__main__':
    print("Sensor data generation started...")
    print("Press Ctrl+C to stop.")

    try:
        # Generate and store simulated sensor data every 60 seconds
        while True:
            generate_sensor_data()
            time.sleep(10)
    except KeyboardInterrupt:
        print("Sensor data generation stopped.")
