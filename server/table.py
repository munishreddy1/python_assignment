import psycopg2

# Connection parameters for PostgreSQL
hostname = 'host.docker.internal'
port = 5432
database = 'postgres'
username = 'postgres'
password = 'password'

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host=hostname,
    port=port,
    database=database,
    user=username,
    password=password
)

# Create a cursor object
cursor = connection.cursor()

# Define the SQL statement to create the table
create_table_query = '''
    CREATE TABLE sensor_data (
        id SERIAL PRIMARY KEY,
        temperature FLOAT NOT NULL,
        humidity INT NOT NULL,
        timestamp TIMESTAMP DEFAULT NOW()
    )'''

# Execute the CREATE TABLE statement
cursor.execute(create_table_query)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()

print("Table created successfully!")
