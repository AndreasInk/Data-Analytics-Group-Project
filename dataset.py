import kagglehub 
import pandas as pd
import os

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