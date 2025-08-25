import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# --- Define the file and folder paths ---
DATA_PATH = 'data/train_FD001.txt'
MODEL_DIR = 'models'
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.joblib')

print("--- Script Starting: Phase 3 Preprocessing ---")

# --- 1. Load Data ---
try:
    # Load the training dataset
    train_df = pd.read_csv(DATA_PATH, sep=" ", header=None)
    print("Data loaded successfully.")
except FileNotFoundError:
    print(f"Error: Data file not found at {DATA_PATH}")
    print("Please ensure 'train_FD001.txt' is in the 'data' folder.")
    exit() # Stop the script if data is not found

# Drop extra empty columns
train_df.drop([26, 27], axis=1, inplace=True)

# Assign column names
col_names = ['id','cycle','setting1','setting2','setting3'] + [f'sensor{i}' for i in range(1,22)]
train_df.columns = col_names

# --- 2. Compute RUL ---
# Find the last cycle for each engine
rul = train_df.groupby('id')['cycle'].max().reset_index()
rul.columns = ['id', 'max_cycle']
train_df = train_df.merge(rul, on='id', how='left')

# Calculate RUL
train_df['RUL'] = train_df['max_cycle'] - train_df['cycle']
train_df.drop('max_cycle', axis=1, inplace=True)
print("RUL calculated.")

# --- 3. Feature Selection ---
features_to_drop = [
    'id', 'cycle', 'setting1', 'setting2', 'setting3',
    'sensor1', 'sensor5', 'sensor6', 'sensor10', 'sensor16', 'sensor18', 'sensor19'
]
df_processed = train_df.drop(features_to_drop, axis=1)

# --- 4. Prepare X and y ---
y = df_processed['RUL']
X = df_processed.drop('RUL', axis=1)
print(f"Features being used for the model: {X.columns.tolist()}")

# --- 5. Split and Scale Data ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
print("Data scaling complete.")

# --- 6. Save the Scaler ---
# Create the 'models' directory if it doesn't exist
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(scaler, SCALER_PATH)
print(f"Success! Scaler has been saved to '{SCALER_PATH}'")
print("--- Script Finished ---")