import requests

backend_server_url = 'http://127.0.0.1:5001/api/processed-data'  # Replace with the actual backend server URL

def get_processed_data():
    try:
        response = requests.get(backend_server_url)
        if response.status_code == 200:
            processed_data = response.json()
            temperature_celsius = processed_data['temperature']
            humidity = processed_data['humidity']
            print("Processed Data:")
            print(f"Temperature: {temperature_celsius}°C")
            print(f"Humidity: {humidity}")
        else:
            print(f"Error: Failed to retrieve processed data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    get_processed_data()
