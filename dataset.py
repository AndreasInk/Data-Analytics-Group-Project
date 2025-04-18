import kagglehub 
import pandas as pd
import os
from sklearn import preprocessing as pre

def load_voice_dataset() -> pd.DataFrame:
    """
    Loads a dataset from Kaggle and caches it or loads from cache
    """
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
    
# Perform all the preprocessing steps
def preprocess_dataset(df) -> pd.DataFrame:
    df_outlierless = remove_outliers(df)
    df_normalized = remove_outliers(df_outlierless)
    return df_normalized

# Take every numeric value in the dataset and normalize it to a value between 0 and 1
def normalize_dataset(df) -> pd.DataFrame:
    # Drop the columns that dont need to be normalized. static_attributes stores the names of the attributes left out of normalization (strings and binary values)
    static_attributes = ["Unnamed: 0", "name", "status"]
    df_normalizable = df.drop(static_attributes, axis=1)
    
    # Prep the scaler. MinMaxScaler normalizes all the values to between 0 and 1, using the max and min from each attribute
    min_max_scaler = pre.MinMaxScaler((0, 1))
    # Apply the normalization
    df_normalized = min_max_scaler.fit_transform(df_normalizable)

    # Pack the returned numpy array into a DataFrame, making sure the original labels and indexing carry over
    df_normalized = pd.DataFrame(df_normalized, columns=df_normalizable.columns, index=df_normalizable.index)
    # Merge the normalized dataset with the attributes left out of normalization. This does change the ordering of the attributes, with the ones left out appearing at the front.
    df_normalized = pd.concat([df[static_attributes], df_normalized], axis=1)
    return df_normalized

# Remove the outliers from the dataset
def remove_outliers(df) -> pd.DataFrame:
    
    return df