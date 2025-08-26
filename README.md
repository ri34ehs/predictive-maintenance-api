Predictive Maintenance API for Manufacturing Equipment
This project is an end-to-end machine learning application that predicts the Remaining Useful Life (RUL) of manufacturing equipment based on sensor data. It includes data preprocessing, model training, hyperparameter tuning, and a Flask API for serving live predictions.

Tech Stack
Python

Pandas for data manipulation

Scikit-learn for machine learning modeling

Flask for the prediction API

Git & GitHub for version control

Live Application 🌐
This project is fully deployed and accessible on the internet.

Live Dashboard
You can interact with the live dashboard to see predictions and monitor your equipment.

Dashboard URL: https://dashboardpy-bdkmgpcutfzngcqpljwksp.streamlit.app/

Backend API
The backend API is deployed on Google Cloud Run and serves the predictions for the dashboard.

API URL: https://predictive-api-825581194035.europe-west1.run.app

How to Run This Project Locally
Clone the repository:

Bash

git clone <your-repo-url>
cd predictive-maintenance-api
Install dependencies:

Bash

pip install -r requirements.txt
Run the data and model pipeline:
(Ensure train_FD001.txt is in the data/ folder first)

Bash

python scripts/phase1_load_data.py
python scripts/phase3_preprocess.py
python scripts/phase5_tune_model.py
Start the API server:

Bash

python api/app.py
Test the API (in a new terminal):

Bash

python api/test_api.py
