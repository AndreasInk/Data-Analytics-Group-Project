import kagglehub 
import numpy as np
import pandas as pd
from scipy.stats import zscore
from sklearn import preprocessing as pre

'''
Loads a dataset from Kaggle and caches it or loads from cache
'''
def load_voice_dataset() -> pd.DataFrame:
    file_path = "./voice.csv"
    try:
        # Load from cache
        with open(file_path) as f:
            df = pd.read_csv(f)
            return df
    except:
        # Load from remote and then cache
        path = kagglehub.dataset_download("vikasukani/parkinsons-disease-data-set")
        df = pd.read_csv(path + "/parkinsons.data")
        df.to_csv("./voice.csv")
        print("First 5 records:", df.head())
        return df
    
'''
Perform all of the preprocessing steps
'''
def preprocess_dataset(df) -> pd.DataFrame:
    # Remove the "Unnamed: 0" column if present
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    # Purge the outliers from the dataset
    df_outlierless = remove_outliers(df)
    # Normalize each value to a number between 0 and 1
    df_normalized = normalize_dataset(df_outlierless)
    return df_normalized

'''
Take every numeric value in the dataset and normalize it to a value between 0 and 1
'''
def normalize_dataset(df) -> pd.DataFrame:
    # Drop the columns that don't need to be normalized (strings and target)
    static_attributes = ["name", "status"]
    df_normalizable = df.drop(columns=static_attributes, errors="ignore")
    
    # Prep the scaler. MinMaxScaler normalizes all the values to between 0 and 1
    min_max_scaler = pre.MinMaxScaler((0, 1))
    # Apply the normalization
    df_norm_array = min_max_scaler.fit_transform(df_normalizable)
    # Pack into DataFrame, preserving index and column names
    # Merge the normalized dataset with the attributes left out of normalization. This does change the ordering of the attributes, with the ones left out appearing at the front.
    df_normalized = pd.DataFrame(df_norm_array, columns=df_normalizable.columns, index=df_normalizable.index)
    return df_normalized

'''
Remove the outliers from the dataset
'''
def remove_outliers(df) -> pd.DataFrame:
    # Only select numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    # Compute z-scores only for numeric columns
    z_scores = np.abs(zscore(df[numeric_cols]))
    # Create a mask where all z-scores are less than 3
    mask = (z_scores < 3).all(axis=1)
    # Keep rows that satisfy the condition
    df_outlierless = df.loc[mask]
    return df_outlierless