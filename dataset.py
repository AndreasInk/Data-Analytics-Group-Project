import kagglehub 
import pandas as pd
import os
from sklearn import preprocessing

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

    return df

# Remove the outliers from the dataset
def remove_outliers(df) -> pd.DataFrame:
    
    return df