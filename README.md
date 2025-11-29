🚀 Predictive Maintenance — End-to-End Machine Learning System

This project predicts the Remaining Useful Life (RUL) of manufacturing equipment using real-time sensor data. It includes data preprocessing, model training, hyperparameter tuning, API development, dashboard UI, and cloud deployment.

🔍 Problem Overview

Manufacturing machines fail unexpectedly, causing downtime and financial loss.
This project solves that by predicting how long a machine will continue functioning before failure.

✔ Predict RUL using multivariate sensor data
✔ Expose a real-time prediction API
✔ Visualize predictions & trends on a dashboard

🧠 Machine Learning Pipeline

Data Processing: Missing value handling, scaling, feature engineering

Model: RandomForestRegressor / XGBoost (whichever you used — specify it)

Evaluation: MAE, RMSE, R²

Optimization: Hyperparameter tuning using GridSearchCV

(Add your actual numbers, otherwise it feels empty.)

🧱 Tech Stack

Languages/Tools: Python
ML: Pandas, NumPy, Scikit-learn
API: Flask
UI: Streamlit
Server: Gunicorn
Deployment: Render
Version Control: Git & GitHub

🌐 Live Deployment

Dashboard: https://predictive-maintenance-dashboard-cpog.onrender.com

API: https://predictive-maintenance-api-18.onrender.com

📡 API Usage
Endpoint

POST /predict

Sample Request
{
  "temperature": 85.3,
  "vibration": 0.91,
  "pressure": 31.5,
  "rpm": 1420
}

Sample Response
{
  "predicted_RUL": 52.7
}

📊 Dashboard Preview

(Add a screenshot — mandatory for good README.)

🛠 Run Locally
1. Clone the repo
git clone https://github.com/ri34ehs/predictive-maintenance-api.git
cd predictive-maintenance-api

2. Create a virtual environment
python -m venv venv


Activate:

venv\Scripts\activate      # Windows
source venv/bin/activate  # macOS/Linux

3. Install dependencies
pip install -r api/requirements.txt
pip install -r dashboard/requirements.txt

4. Start Backend API (Terminal 1)
cd api
python app.py

5. Start Streamlit Dashboard (Terminal 2)
cd dashboard
streamlit run streamlit_app.py

📁 Project Structure
project/
│── api/
│   ├── app.py
│   └── requirements.txt
│── dashboard/
│   ├── streamlit_app.py
│   └── requirements.txt
│── models/
│── data/
└── README.md

