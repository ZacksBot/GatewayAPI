from flask import Flask, request, Response
import requests
import csv
import io
import json

app = Flask(__name__)

# Silobreaker API
SILOBREAKER_API_URL = "https://api.silobreaker.com/v1/heat?q=fromdate:-24h&tq=entitytype:vulnerability&apiKey=1c1phx2l0urct41di8x2&digest=xFPasGTSqwjYGn3aiTQ9%2BeAtLFU%3D"

def fetch_data():
    response = requests.get(SILOBREAKER_API_URL)
    response.raise_for_status()
    return response.json()

def json_to_csv(data):
    items = data.get("Items", [])
    if not items or not isinstance(items, list) or not isinstance(items[0], dict):
        raise ValueError("Invalid data format received from API.")

    keys = items[0].keys()
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=keys)
    writer.writeheader()
    writer.writerows(items)
    return output.getvalue()

@app.route('/vulnerabilities', methods=['GET'])
def vulnerabilities():
    try:
        data = fetch_data()

        format = request.args.get('format', 'csv').lower()

        if format == 'json':
            response = Response(json.dumps(data, indent=4), mimetype='application/json')
        elif format == 'csv':
            csv_data = json_to_csv(data)
            response = Response(csv_data, mimetype='text/csv')
            response.headers['Content-Disposition'] = 'attachment; filename=vulnerabilities.csv'
        else:
            response = Response("Unsupported format. Please use 'csv' or 'json'.", status=400)
    except ValueError as e:
        response = Response(str(e), status=500)
    except Exception as e:
        response = Response("An error occurred: " + str(e), status=500)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)