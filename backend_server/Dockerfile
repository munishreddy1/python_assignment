# Use an appropriate base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the backend server code into the container
COPY backend_server.py /app/

# Install the required dependencies
RUN pip install flask psycopg2 matplotlib

# Expose the port on which the Flask app will run
EXPOSE 5000

# Pass system environment variables as build arguments
ARG DB_HOST
ARG DB_PORT
ARG DB_NAME
ARG DB_USERNAME
ARG DB_PASSWORD

# Set the environment variables using the build arguments
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_NAME=$DB_NAME
ENV DB_USERNAME=$DB_USERNAME
ENV DB_PASSWORD=$DB_PASSWORD

# Run the backend server
CMD [ "python", "backend_server.py" ]
