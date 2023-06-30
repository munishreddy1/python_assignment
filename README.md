# python_assignment
Approach-1:
On-the-fly Generation:

In this approach, the server generates the simulated sensor data periodically.
When backend server API receives a request from the client, it sends a request to the server for the raw sensor data.
The server generates the simulated data on-the-fly and returns it as a response to the backend server API.
The backend server can then process the raw sensor data for example I choose converting fahrenheit to celsius and provide the processed data to the client.
With this approach, the data is not stored and is generated dynamically upon request so I implemented data processing using single data.


Approach-2:
Data Storage:

In this approach, the API server stores the generated sensor data in a database or file system.
When the backend server receives a request from the client, it retrieves the stored data from the API server's database or file system.
The backend server can then process the retrieved data and provide the processed data to the client.
With this approach, the data is stored persistently, allowing the backend server to retrieve and process it whenever needed.

