# scripts/phase5_tune_model.py

import pandas as pd
import joblib
import os
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Define file paths
PROCESSED_DATA_PATH = 'data/train_processed.csv'
MODEL_DIR = 'models'
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.joblib')
TUNED_MODEL_PATH = os.path.join(MODEL_DIR, 'tuned_rul_prediction_model.joblib')

def run():
    print("--- Phase 5: Tuning model hyperparameters ---")

    # Load data and scaler
    train_df = pd.read_csv(PROCESSED_DATA_PATH)
    scaler = joblib.load(SCALER_PATH)

    # Same feature selection and data prep as before
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

    # Define the hyperparameter grid to search
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [10, 20, 30, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Set up Randomized Search
    rf = RandomForestRegressor(random_state=42)
    random_search = RandomizedSearchCV(estimator=rf, param_distributions=param_grid,
                                       n_iter=20, cv=3, verbose=2,
                                       random_state=42, n_jobs=-1)

    print("Starting hyperparameter search... (This may take a few minutes)")
    random_search.fit(X_train_scaled, y_train)

    print(f"Best Hyperparameters Found: {random_search.best_params_}")

    # Get the best model
    best_rf = random_search.best_estimator_

    # Evaluate the tuned model
    tuned_preds = best_rf.predict(X_test_scaled)
    tuned_rmse = np.sqrt(mean_squared_error(y_test, tuned_preds))
    print(f"Tuned Model RMSE: {tuned_rmse:.2f}")

    # Save the final, tuned model
    joblib.dump(best_rf, TUNED_MODEL_PATH)

    print(f"Final tuned model successfully saved to '{TUNED_MODEL_PATH}'")
    print("--- Phase 5 Finished ---\n")

if __name__ == '__main__':
    run()