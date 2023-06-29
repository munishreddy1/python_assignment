# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app/backend_server

# Copy the backend server code into the container
COPY backend_server.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the backend server port
EXPOSE 5001

# Define the command to run the backend server
CMD ["python", "backend_server.py"]
