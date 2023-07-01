# Sensor Data Processing
## Approach-1: On-the-fly Generation

This project consists of a sensor data processing dashboard that retrieves simulated sensor data, processes it, and displays the processed data in a dashboard.

## Features

- Retrieves simulated raw sensor data (temperature and humidity) from the API server
- Converts the temperature from Fahrenheit to Celsius
- Displays the processed data (temperature in Celsius and humidity) in a web-based dashboard
- Auto-updates the dashboard every 10 seconds with the latest processed data

## Components

The project is divided into the following components:

- **Client**: A Python client that interacts with the backend server to retrieve processed data and renders an HTML dashboard.

- **Backend Server (Python API Server)**: A Python server that acts as an interface between the client and the API server. It retrieves raw sensor data from the server, processes it, and exposes the processed data through an API.

- **API Server (Simulated Sensor Data)**: A server-based application that generates simulated sensor data and exposes the raw data through an API.

## Usage

Follow the steps below to set up and run the project:

1. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt

Start the server by running the server.py script:

Start the backend server (Python API server) by running the backend_server.py script:

Start the client by running the client.py script:

Access the dashboard by opening a web browser and navigating to http://localhost:5002.

The dashboard will display the processed sensor data (temperature in Celsius and humidity) retrieved from the backend server. It will automatically update every 10 seconds with the latest data.

## Dependencies
The project relies on the following dependencies:

- Flask: A lightweight web framework for Python used for the API server and backend server.
- Requests: A library for making HTTP requests, used by the client to interact with the backend server.
- ApScheduler: For scheduling time intervals in the server
These dependencies are listed in the requirements.txt file and can be installed using pip.



Approach-2:
Data Storage:

In this approach, the server stores the generated sensor data in a database or file system.
When the backend server receives a request from the client, it retrieves the stored data from the API server's database or file system.
The backend server can then process the retrieved data and provide the processed data to the client.
With this approach, the data is stored persistently, allowing the backend server to retrieve and process it whenever needed.
