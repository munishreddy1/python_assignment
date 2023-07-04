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



## Approach-2: Used Database for storing raw sensor data
In this approach I the server fetches sensor data from a PostgreSQL database, performs data processing, and provides access to the processed data via an API.

## Features

- Fetches the last 10 entries of sensor data from a PostgreSQL database.
- Calculates the average temperature and average humidity of the fetched data.
- Provides access to the processed data through a RESTful API.

## Requirements

- Python 3.x
- PostgreSQL database(Preferably docker container)
- pgadmin provides GUI for postgreSQL.
- Required Python packages (specified in `requirements.txt`)

## Installation

1. Dependencies:

   ```bash
   pip install -r requirements.txt

2. Set up the PostgreSQL database and provide the connection details as environment variables:

- DB_HOST: Hostname or IP address of the PostgreSQL server.
- DB_PORT: Port number on which the PostgreSQL server is running.
- DB_NAME: Name of the database.
- DB_USERNAME: Username to access the database.
- DB_PASSWORD: Password for the database user.

