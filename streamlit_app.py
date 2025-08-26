# dashboard.py

import streamlit as st
import requests
import json

# --- Page Configuration ---
st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="centered"
)

# --- API Endpoint ---
API_URL = "https://predictive-api-final-298148143452-europe-west1.run.app"

# --- Page Title and Description ---
st.title("⚙️ Predictive Maintenance Dashboard")
st.write(
    "This dashboard predicts the Remaining Useful Life (RUL) of an engine "
    "based on its sensor readings. Adjust the sliders below to get a prediction from the live model."
)

st.markdown("---")

# --- Input Sliders for Features ---
st.header("Engine Sensor Readings")

# Create two columns for the sliders
col1, col2 = st.columns(2)

with col1:
    cycle = st.slider('Cycle', min_value=1, max_value=300, value=25)
    sensor2 = st.slider('Sensor 2', min_value=640.0, max_value=650.0, value=643.0, step=0.1)
    sensor3 = st.slider('Sensor 3', min_value=1570.0, max_value=1620.0, value=1592.0, step=0.1)
    sensor4 = st.slider('Sensor 4', min_value=1380.0, max_value=1440.0, value=1408.0, step=0.1)
    sensor7 = st.slider('Sensor 7', min_value=550.0, max_value=560.0, value=553.0, step=0.1)
    sensor8 = st.slider('Sensor 8', min_value=2380.0, max_value=2390.0, value=2388.0, step=0.01)
    sensor11 = st.slider('Sensor 11', min_value=46.0, max_value=49.0, value=47.0, step=0.01)

with col2:
    sensor12 = st.slider('Sensor 12', min_value=518.0, max_value=525.0, value=521.0, step=0.1)
    sensor13 = st.slider('Sensor 13', min_value=2380.0, max_value=2390.0, value=2388.0, step=0.01)
    sensor14 = st.slider('Sensor 14', min_value=8100.0, max_value=8250.0, value=8120.0, step=1.0)
    sensor15 = st.slider('Sensor 15', min_value=8.0, max_value=9.0, value=8.4, step=0.01)
    sensor17 = st.slider('Sensor 17', min_value=390, max_value=405, value=394)
    sensor20 = st.slider('Sensor 20', min_value=38.0, max_value=40.0, value=38.8, step=0.01)
    sensor21 = st.slider('Sensor 21', min_value=23.0, max_value=24.0, value=23.3, step=0.01)

# --- Prediction Button and Display ---
if st.button('Predict Remaining Useful Life', use_container_width=True):
    # Collect features from sliders into a list
    # The feature 'sensor9' has been removed to match the model's requirements
    features = [
        cycle, sensor2, sensor3, sensor4, sensor7, sensor8,
        sensor11, sensor12, sensor13, sensor14, sensor15, sensor17, sensor20, sensor21
    ]
    
    # Create the JSON payload
    payload = {"features": features}
    
    # Send request to the API
    try:
        response = requests.post(f"{API_URL}/predict", json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Display the prediction
        prediction = response.json()
        st.metric(
            label="Predicted RUL (in cycles)",
            value=f"{prediction['predicted_rul']:.2f}"
        )
        st.success("Prediction successful!")
        
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the API. Please ensure the Docker container is running. Error: {e}")
