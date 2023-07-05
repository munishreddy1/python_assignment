# Use an appropriate base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the client code and template files into the container
COPY client.py /app/
COPY templates/ /app/templates/
COPY plots/ /app/plots/

# Install the required dependencies
RUN pip install flask requests

# Expose the port on which the Flask app will run
EXPOSE 5001

# Set the environment variable for the backend server URL
ENV BACKEND_URL http://backend:5000/api/processed-data

# Run the client
CMD [ "python", "client.py" ]
