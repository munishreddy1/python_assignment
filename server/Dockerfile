# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app/api_server

# Copy the API server code into the container
COPY api_server.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the API server port
EXPOSE 5000

# Define the command to run the API server
CMD ["python", "api_server.py"]
