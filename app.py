from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated in-memory storage for processed data
data_storage = {}

# Mock data to simulate fetching from an external service
mock_data = [
    {"id": 1, "value": "apple"},
    {"id": 2, "value": "banana"},
    {"id": 3, "value": "cherry"},
]

def process_data(data):
    """ Process the fetched data by converting all text to uppercase. """
    return [item['value'].upper() for item in data]

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    """ Simulate fetching data from an external service. """
    global mock_data
    return jsonify(mock_data)

@app.route('/process-data', methods=['POST'])
def process_data_endpoint():
    """ Process fetched data and store it in memory. """
    global mock_data, data_storage
    processed_data = process_data(mock_data)
    data_storage['processed_data'] = processed_data
    return jsonify({"message": "Data processed successfully", "data": processed_data})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """ Return the processed data stored in memory. """
    global data_storage
    processed_data = data_storage.get('processed_data', [])
    return jsonify({"processed_data": processed_data})

if __name__ == '__main__':
    app.run(debug=True)