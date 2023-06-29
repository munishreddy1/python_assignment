from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# Create an instance of BackgroundScheduler
scheduler = BackgroundScheduler()


def generate_sensor_data():
    # Code to generate simulated sensor data
    # For example, generating random temperature and humidity values
    import random
    temperature = random.uniform(20, 30)
    humidity = random.uniform(40, 60)

    # Return the generated data as a JSON response
    data = {
        'temperature': temperature,
        'humidity': humidity
    }
    return jsonify(data)


# Define the route for accessing the raw sensor data
@app.route('/api/raw-data')
def get_raw_data():
    return generate_sensor_data()


if __name__ == '__main__':
    # Add the generate_sensor_data function to the scheduler to be called every 1 minute
    scheduler.add_job(generate_sensor_data, 'interval', minutes=1)

    # Start the scheduler
    scheduler.start()

    # Run the Flask app
    app.run()
