Predictive Maintenance API for Manufacturing Equipment
This project is an end-to-end machine learning application that predicts the Remaining Useful Life (RUL) of manufacturing equipment based on sensor data. It includes data preprocessing, model training, hyperparameter tuning, and a Flask API for serving live predictions.

Tech Stack
Python

Pandas for data manipulation

Scikit-learn for machine learning modeling

Flask for the prediction API

Streamlit for the interactive dashboard

Gunicorn for the production API server

Render for cloud deployment

Git & GitHub for version control

Live Application 🌐
This project is fully deployed on Render and is accessible via the following URLs:

Live Dashboard: https://predictive-maintenance-dashboard-cpog.onrender.com

Backend API: https://predictive-maintenance-api-18.onrender.com

How to Run This Project Locally
Clone the repository:

Bash

git clone https://github.com/ri34ehs/predictive-maintenance-api.git
cd predictive-maintenance-api
Create and activate a virtual environment:

Bash

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
Install dependencies:

Bash

pip install -r api/requirements.txt
pip install -r dashboard/requirements.txt
Run the API locally (Terminal 1):
First, start the backend API.

Bash

cd api
python app.py
Run the Streamlit Dashboard locally (Terminal 2):
Next, open a new terminal window and start the dashboard.

Bash

cd dashboard
streamlit run streamlit_app.py
