# predictive-maintenance-api

# Predictive Maintenance API for Manufacturing Equipment

This project is an end-to-end machine learning application that predicts the Remaining Useful Life (RUL) of manufacturing equipment based on sensor data. It includes data preprocessing, model training, hyperparameter tuning, and a Flask API for serving live predictions.

## Tech Stack
- **Python**
- **Pandas** for data manipulation
- **Scikit-learn** for machine learning modeling
- **Flask** for the prediction API
- **Git & GitHub** for version control

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd predictive-maintenance-api
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the data and model pipeline:**
    *(Ensure `train_FD001.txt` is in the `data/` folder first)*
    ```bash
    python scripts/phase1_load_data.py
    python scripts/phase3_preprocess.py
    python scripts/phase5_tune_model.py
    ```

4.  **Start the API server:**
    ```bash
    python api/app.py
    ```

5.  **Test the API (in a new terminal):**
    ```bash
    python api/test_api.py
    ```
    python api/app.py
    ```

5.  **Test the API (in a new terminal):**
    ```bash
    python api/test_api.py
    ```
