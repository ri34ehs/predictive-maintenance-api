import streamlit as st
import requests
import os

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# -------------------- HEADER --------------------
st.title("⚙️ Predictive Maintenance Dashboard")
st.markdown("Use the sliders below to set **engine sensor readings** and predict the Remaining Useful Life (RUL).")

# -------------------- BACKEND API URL --------------------
# Use environment variable if deployed, else default to local
API_URL = os.environ.get("API_URL", "http://127.0.0.1:5000")

# -------------------- INPUT SLIDERS --------------------
st.header("📊 Engine Sensor Readings")

col1, col2 = st.columns(2)

with col1:
    cycle = st.slider('Cycle', 1, 300, 25)
    s2 = st.slider('Sensor 2', 640.0, 650.0, 643.0, 0.1)
    s3 = st.slider('Sensor 3', 1570.0, 1620.0, 1592.0, 0.1)
    s4 = st.slider('Sensor 4', 1380.0, 1440.0, 1408.0, 0.1)
    s7 = st.slider('Sensor 7', 550.0, 560.0, 553.0, 0.1)
    s8 = st.slider('Sensor 8', 2380.0, 2390.0, 2388.0, 0.01)
    s11 = st.slider('Sensor 11', 46.0, 49.0, 47.0, 0.01)

with col2:
    s12 = st.slider('Sensor 12', 518.0, 525.0, 521.0, 0.1)
    s13 = st.slider('Sensor 13', 2380.0, 2390.0, 2388.0, 0.01)
    s14 = st.slider('Sensor 14', 8100.0, 8250.0, 8120.0, 1.0)
    s15 = st.slider('Sensor 15', 8.0, 9.0, 8.4, 0.01)
    s17 = st.slider('Sensor 17', 390, 405, 394)
    s20 = st.slider('Sensor 20', 38.0, 40.0, 38.8, 0.01)
    s21 = st.slider('Sensor 21', 23.0, 24.0, 23.3, 0.01)

# -------------------- PREDICTION --------------------
st.markdown("---")
if st.button("🔮 Predict RUL"):
    # Build the full URL to the /predict endpoint
    PREDICT_URL = f"{API_URL}/predict"

    # Convert sliders to feature list
    features = [
        cycle, s2, s3, s4, s7, s8, s11,
        s12, s13, s14, s15, s17, s20, s21
    ]
    input_data = {"features": features}

    try:
        # Use requests.post() and the corrected URL
        response = requests.post(PREDICT_URL, json=input_data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            st.success(f"✅ Predicted Remaining Useful Life (RUL): **{result['predicted_rul']} cycles**")
        else:
            st.error(f"❌ API Error {response.status_code}: {response.text}")
    except requests.exceptions.Timeout:
        st.error("⏳ Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        st.error("🚨 Connection error: Could not reach API. Check URL")