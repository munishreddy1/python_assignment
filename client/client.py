from flask import Flask, render_template
import requests
import os

app = Flask(__name__, template_folder='../templates', static_folder='../plots') # Update new folders created at root level

# Define the backend server URL
backend_url = 'http://localhost:5000/api/processed-data'


@app.route('/')
def dashboard():
    # Sends a GET request to the backend server API
    response = requests.get(backend_url)
    if response.status_code == 200:
        # Extracts the processed data from the response
        processed_data = response.json()

        # Specify the path of the plot image
        plot_path = os.path.join('plots', 'plot.png')

        # Pass the processed data to the template for rendering
        return render_template('dashboard.html', data=processed_data, plot_image=plot_path)
    else:
        return 'Error retrieving data from the backend server.'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
