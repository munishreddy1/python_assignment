from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

backend_server_url = 'http://127.0.0.1:5001/api/processed-data'

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/processed-data')
def get_processed_data():
    try:
        response = requests.get(backend_server_url)
        if response.status_code == 200:
            processed_data = response.json()
            return processed_data
        else:
            return f"Error: Failed to retrieve processed data. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)
