from flask import Flask, jsonify
import requests

app = Flask(__name__)
api_server_url = 'http://127.0.0.1:5000/api/raw-data'  # API server address


def process_sensor_data():
    # Retrieve raw sensor data from the API server
    response = requests.get(api_server_url)

    if response.status_code == 200:
        raw_data = response.json()
        processed_data = {
            'temperature': fahrenheit_to_celsius(raw_data['temperature']),
            'humidity': raw_data['humidity']
        }
        return processed_data
    else:
        print('Error: Failed to fetch raw sensor data from the API server.')
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


# import requests

# def fahrenheit_to_celsius(fahrenheit):
#     # Convert temperature from Fahrenheit to Celsius
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# def process_sensor_data(sensor_data):
#     # Code to process the raw sensor data
#     # For example, apply data transformations, perform calculations, etc.
#     # Modify this function based on your processing requirements

#     # Convert temperature from Fahrenheit to Celsius
#     temperature_fahrenheit = sensor_data.get('temperature')
#     temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit) if temperature_fahrenheit else None

#     processed_data = {
#         'temperature_celsius': temperature_celsius,
#         'humidity': sensor_data.get('humidity')
#     }
#     return processed_data

# def get_sensor_data_from_api():
#     # Make a request to the API server to get the raw sensor data
#     api_url = 'http://127.0.0.1:5000/api/raw-data'  # Replace with the actual API server address
#     response = requests.get(api_url)

#     if response.status_code == 200:
#         sensor_data = response.json()
#         processed_data = process_sensor_data(sensor_data)
#         return processed_data
#     else:
#         print('Error: Failed to fetch sensor data from the API server.')
#         return None

# # Example usage:
# if __name__ == '__main__':
#     # Retrieve the sensor data from the API server
#     data = get_sensor_data_from_api()

#     if data is not None:
#         # Processed data is available
#         print('Processed Sensor Data:')
#         print(data)
