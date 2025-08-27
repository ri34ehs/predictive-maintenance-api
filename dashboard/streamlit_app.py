import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# -------------------- HEADER --------------------
st.title("⚙️ Predictive Maintenance Dashboard")
st.markdown("Use the sliders below to set **engine sensor readings** and predict the Remaining Useful Life (RUL).")

# Backend API URL (Update this with your Render/Cloud Run deployment URL)
API_URL = "https://your-api-service.onrender.com/predict"

# -------------------- INPUT SLIDERS --------------------
st.header("📊 Engine Sensor Readings")

col1, col2 = st.columns(2)

with col1:
    cycle = st.slider('Cycle', min_value=1, max_value=300, value=25)
    s2 = st.slider('Sensor 2', min_value=640.0, max_value=650.0, value=643.0, step=0.1)
    s3 = st.slider('Sensor 3', min_value=1570.0, max_value=1620.0, value=1592.0, step=0.1)
    s4 = st.slider('Sensor 4', min_value=1380.0, max_value=1440.0, value=1408.0, step=0.1)
    s7 = st.slider('Sensor 7', min_value=550.0, max_value=560.0, value=553.0, step=0.1)
    s8 = st.slider('Sensor 8', min_value=2380.0, max_value=2390.0, value=2388.0, step=0.01)
    s11 = st.slider('Sensor 11', min_value=46.0, max_value=49.0, value=47.0, step=0.01)

with col2:
    s12 = st.slider('Sensor 12', min_value=518.0, max_value=525.0, value=521.0, step=0.1)
    s13 = st.slider('Sensor 13', min_value=2380.0, max_value=2390.0, value=2388.0, step=0.01)
    s14 = st.slider('Sensor 14', min_value=8100.0, max_value=8250.0, value=8120.0, step=1.0)
    s15 = st.slider('Sensor 15', min_value=8.0, max_value=9.0, value=8.4, step=0.01)
    s17 = st.slider('Sensor 17', min_value=390, max_value=405, value=394)
    s20 = st.slider('Sensor 20', min_value=38.0, max_value=40.0, value=38.8, step=0.01)
    s21 = st.slider('Sensor 21', min_value=23.0, max_value=24.0, value=23.3, step=0.01)

# -------------------- PREDICTION --------------------
st.markdown("---")
if st.button("🔮 Predict RUL"):
    input_data = {
        "cycle": cycle,
        "s2": s2, "s3": s3, "s4": s4, "s7": s7, "s8": s8, "s11": s11,
        "s12": s12, "s13": s13, "s14": s14, "s15": s15,
        "s17": s17, "s20": s20, "s21": s21
    }

    try:
        response = requests.post(API_URL, json=input_data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            st.success(f"✅ Predicted Remaining Useful Life (RUL): **{result['rul']} cycles**")
        else:
            st.error(f"❌ API Error {response.status_code}: {response.text}")
    except requests.exceptions.Timeout:
        st.error("⏳ Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        st.error("🚨 Connection error: Could not reach API. Check URL or network.")
    except Exception as e:
        st.error(f"⚠️ Unexpected error: {e}")


