import joblib
import numpy as np
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Load model and scaler
try:
    model = joblib.load('models/tuned_rul_prediction_model.joblib')
    scaler = joblib.load('models/scaler.joblib')
except FileNotFoundError:
    print("Error: Model or scaler files not found in the 'models' directory.")
    print("Please run the training scripts first.")
    exit()


@app.route('/predict', methods=['POST'])
def predict():
    """Receives sensor data in a POST request and returns a RUL prediction."""
    try:
        # Get the JSON data from the request
        data = request.get_json()
        print("📥 Received data:", data)

        # Ensure the 'features' key exists and is a list
        if 'features' not in data or not isinstance(data['features'], list):
            return jsonify({'error': "Invalid input: 'features' key missing or not a list."}), 400

        # Convert feature list to a NumPy array for processing
        features = np.array(data['features']).reshape(1, -1)
        print("🔹 features (raw input array):", features)

        # Scale the new data using the loaded scaler
        features_scaled = scaler.transform(features)
        print("🔹 features_scaled (after StandardScaler):", features_scaled)

        # Make a prediction
        prediction = model.predict(features_scaled)
        print("🔹 prediction (raw output):", prediction)

        # Return the prediction as a JSON response
        result = {'predicted_rul': round(prediction[0], 2)}
        print("✅ Final result:", result)

        return jsonify(result)

    except Exception as e:
        # Handle potential errors during prediction
        print("❌ Error during prediction:", str(e))
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Starting Flask server on port {port}")
    app.run(host="0.0.0.0", port=port)
