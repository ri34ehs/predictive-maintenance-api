# scripts/phase1_load_data.py

import pandas as pd
import os

# Define file paths
RAW_DATA_PATH = 'data/train_FD001.txt'
PROCESSED_DATA_PATH = 'data/train_processed.csv'

def run():
    print("--- Phase 1: Loading data and computing RUL ---")
    
    # Check if raw data exists
    if not os.path.exists(RAW_DATA_PATH):
        print(f"Error: Raw data file not found at '{RAW_DATA_PATH}'")
        print("Please download the data and place it in the 'data' folder.")
        return

    # Load the training dataset
    train_df = pd.read_csv(RAW_DATA_PATH, sep=" ", header=None)
    
    # Drop extra empty columns and assign names
    train_df.drop([26, 27], axis=1, inplace=True)
    col_names = ['id','cycle','setting1','setting2','setting3'] + [f'sensor{i}' for i in range(1,22)]
    train_df.columns = col_names
    
    # Compute RUL
    rul = train_df.groupby('id')['cycle'].max().reset_index()
    rul.columns = ['id', 'max_cycle']
    train_df = train_df.merge(rul, on='id', how='left')
    train_df['RUL'] = train_df['max_cycle'] - train_df['cycle']
    train_df.drop('max_cycle', axis=1, inplace=True)
    
    # Save the processed data
    train_df.to_csv(PROCESSED_DATA_PATH, index=False)
    
    print(f"Data processed successfully and saved to '{PROCESSED_DATA_PATH}'")
    print("--- Phase 1 Finished ---\n")

if __name__ == '__main__':
    run()