from flask import Flask, jsonify
import psycopg2
import os
app = Flask(__name__)

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


def fetch_sensor_data():
    # Fetch the last 10 entries from the database
    query = "SELECT temperature, humidity FROM sensor_data ORDER BY timestamp DESC LIMIT 10"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Calculate average and mean
    total_temperature = 0
    total_humidity = 0
    for row in rows:
        temperature, humidity = row
        total_temperature += temperature
        total_humidity += humidity
    average_temperature = total_temperature / len(rows)
    average_humidity = total_humidity / len(rows)

    # Find highest and lowest values
    highest_temperature = max(rows, key=lambda x: x[0])[0]
    lowest_temperature = min(rows, key=lambda x: x[0])[0]
    highest_humidity = max(rows, key=lambda x: x[1])[1]
    lowest_humidity = min(rows, key=lambda x: x[1])[1]

    # Prepare the response
    processed_data = {
        'average_temperature': average_temperature,
        'average_humidity': average_humidity,
        'highest_temperature': highest_temperature,
        'lowest_temperature': lowest_temperature,
        'highest_humidity': highest_humidity,
        'lowest_humidity': lowest_humidity
    }

    return processed_data


# Define the route for accessing the processed sensor data
@app.route('/api/processed-data')
def get_processed_data():
    data = fetch_sensor_data()
    return jsonify(data)


if __name__ == '__main__':
    app.run()



# hostname = 'host.docker.internal'
# port = 5432
# database = 'postgres'
# username = 'postgres'
# password = 'password'