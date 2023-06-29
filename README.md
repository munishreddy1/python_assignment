# python_assignment
On-the-fly Generation:

In this approach, the api_server generates the simulated sensor data periodically.
When your backend server receives a request from the client, it sends a request to the API server for the raw sensor data.
The API server generates the simulated data on-the-fly and returns it as a response to the backend server.
The backend server can then process the raw sensor data and provide the processed data to the client.
With this approach, the data is not stored persistently and is generated dynamically upon request.
