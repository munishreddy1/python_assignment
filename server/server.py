import time
import psycopg2
import os

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
    database=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USERNAME'),
    password=os.environ.get('DB_PASSWORD')
)

# Create a cursor object
cursor = connection.cursor()


def generate_sensor_data():
    # Generate random temperature and humidity values
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





# Connection parameters for PostgreSQL
# hostname = 'host.docker.internal'
# port = 5432
# database = 'postgres'
# username = 'postgres'
# password = 'password'