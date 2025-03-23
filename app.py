import streamlit as st
import pandas as pd
import numpy as np
from dataset import load_voice_dataset

df = load_voice_dataset()

st.title("Data Analytics: Parkinson's Voice Dataset")

st.dataframe(df)

