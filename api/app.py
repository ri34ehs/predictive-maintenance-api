import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# -------------------- LOAD MODEL AND SCALER --------------------
MODEL_PATH = 'models/tuned_rul_prediction_model.joblib'
SCALER_PATH = 'models/scaler.joblib'

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print(f"✅ Model loaded from {MODEL_PATH}")
    print(f"✅ Scaler loaded from {SCALER_PATH}")
except FileNotFoundError:
    print("❌ Error: Model or scaler files not found in the 'models' directory.")
    print("Please run the training scripts first to generate the files.")
    exit()
except Exception as e:
    print(f"❌ Unexpected error while loading model/scaler: {e}")
    exit()

# -------------------- HEALTH CHECK --------------------
@app.route("/", methods=["GET"])
def health_check():
    """Simple route to check if the API is running."""
    return jsonify({"status": "API is running ✅"}), 200

# -------------------- PREDICTION ROUTE --------------------
@app.route("/predict", methods=["POST"])
def predict():
    """
    Receives sensor data in a POST request and returns a RUL prediction.
    Expected JSON format: {"features": [f1, f2, f3, ..., fn]}
    """
    try:
        data = request.get_json()
        if not data or 'features' not in data or not isinstance(data['features'], list):
            return jsonify({'error': "Invalid input: 'features' key missing or not a list."}), 400

        features = np.array(data['features']).reshape(1, -1)
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)

        return jsonify({'predicted_rul': round(prediction[0], 2)}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# -------------------- START SERVER --------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Starting Flask server on port {port}")
    app.run(host="0.0.0.0", port=port)
