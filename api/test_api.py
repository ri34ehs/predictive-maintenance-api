import requests

# The URL of your running Flask API's prediction endpoint
url = 'http://127.0.0.1:5000/predict'

# Sample data for one engine cycle.
# This MUST have the same number of features the model was trained on (14 in our case).
sample_input = {
    "features": [
        25.0,   # cycle
        643.0,  # sensor2
        1592.0, # sensor3
        1408.0, # sensor4
        47.0,   # sensor7
        521.0,  # sensor8
        2388.0, # sensor9
        8120.0, # sensor11
        8.0,    # sensor12
        394.0,  # sensor13
        2388.0, # sensor14
        8120.0, # sensor15
        39.0,   # sensor17
        23.0    # sensor20
    ]
}

try:
    # Send the POST request with the JSON data to the API
    response = requests.post(url, json=sample_input)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("API Response:")
        print(response.json())
    else:
        print(f"Error: API returned status code {response.status_code}")
        print("Response content:", response.text)

except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: Could not connect to the API at {url}")
    print("Please ensure the 'app.py' server is running.")