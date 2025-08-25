import joblib
import numpy as np
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# --- Load the Model and Scaler ---
# These paths are relative to the root project folder (predictive-maintenance)
# where you will run the `python api/app.py` command.
try:
   # NEW - Use the tuned model
    model = joblib.load('models/tuned_rul_prediction_model.joblib')
    scaler = joblib.load('models/scaler.joblib')
except FileNotFoundError:
    print("Error: Model or scaler files not found in the 'models' directory.")
    print("Please run the training scripts first.")
    # Exit if files are not found
    exit()

@app.route('/predict', methods=['POST'])
def predict():
    """Receives sensor data in a POST request and returns a RUL prediction."""
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Ensure the 'features' key exists and is a list
        if 'features' not in data or not isinstance(data['features'], list):
            return jsonify({'error': "Invalid input: 'features' key missing or not a list."}), 400

        # Convert feature list to a NumPy array for processing
        features = np.array(data['features']).reshape(1, -1)
        
        # Scale the new data using the loaded scaler
        features_scaled = scaler.transform(features)
        
        # Make a prediction
        prediction = model.predict(features_scaled)
        
        # Return the prediction as a JSON response
        return jsonify({'predicted_rul': round(prediction[0], 2)})

    except Exception as e:
        # Handle potential errors during prediction
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app, making it accessible on your local network
    app.run(host='0.0.0.0', port=5000, debug=True)