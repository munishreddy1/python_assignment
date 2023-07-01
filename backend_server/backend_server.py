from flask import Flask, jsonify
import requests

app = Flask(__name__)
server_url = 'http://127.0.0.1:5000/api/raw-data'  # server address


def process_sensor_data():
    # Retrieve raw sensor data from the server
    response = requests.get(server_url)

    if response.status_code == 200:
        raw_data = response.json()
        processed_data = {
            'temperature': fahrenheit_to_celsius(raw_data['temperature']),
            'humidity': raw_data['humidity']
        }
        return processed_data
    else:
        print('Error: Failed to fetch raw sensor data from the server.')
        return None


def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


@app.route('/api/processed-data', methods=['GET'])

def get_processed_data():
    # Retrieve processed data from process_sensor_data() function
    processed_data = process_sensor_data()

    if processed_data is not None:
        return jsonify(processed_data)
    else:
        return jsonify({'error': 'Failed to retrieve processed sensor data.'})


if __name__ == '__main__':
    # Run the Flask app in development mode on localhost
    app.run(host='127.0.0.1', port=5001, debug=True)
