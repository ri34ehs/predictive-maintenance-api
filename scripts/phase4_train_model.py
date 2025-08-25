# scripts/phase4_train_model.py

import pandas as pd
import joblib
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Define file paths
PROCESSED_DATA_PATH = 'data/train_processed.csv'
MODEL_DIR = 'models'
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.joblib')
MODEL_PATH = os.path.join(MODEL_DIR, 'rul_prediction_model.joblib')

def run():
    print("--- Phase 4: Training baseline model ---")
    
    # Load data and scaler
    train_df = pd.read_csv(PROCESSED_DATA_PATH)
    scaler = joblib.load(SCALER_PATH)
    
    # Same feature selection and data prep as in Phase 3
    features_to_drop = [
        'id', 'cycle', 'setting1', 'setting2', 'setting3',
        'sensor1', 'sensor5', 'sensor6', 'sensor10', 'sensor16', 'sensor18', 'sensor19'
    ]
    df_processed = train_df.drop(features_to_drop, axis=1)
    y = df_processed['RUL']
    X = df_processed.drop('RUL', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale data
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest model
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train_scaled, y_train)
    
    # Evaluate model
    preds = rf.predict(X_test_scaled)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"Baseline Random Forest RMSE: {rmse:.2f}")
    
    # Save the trained model
    joblib.dump(rf, MODEL_PATH)
    
    print(f"Baseline model successfully trained and saved to '{MODEL_PATH}'")
    print("--- Phase 4 Finished ---\n")

if __name__ == '__main__':
    run()