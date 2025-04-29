import streamlit as st
import pandas as pd
import joblib
from dataset import load_voice_dataset, preprocess_dataset

def main():
    st.title("Parkinson's Voice Analysis Demo")
    st.markdown(
        """
        This simple demo lets you explore the Parkinson’s voice dataset,
        view summary statistics, see basic plots, and run the trained model.
        """
    )

    # Sidebar controls
    st.sidebar.header("Controls")
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    show_stats = st.sidebar.checkbox("Show summary statistics", value=False)
    show_plot = st.sidebar.checkbox("Show histogram of a feature", value=False)
    run_prediction = st.sidebar.checkbox("Run model predictions", value=False)

    # Load data
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        df = load_voice_dataset()

    # Display data
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10))

    # Summary statistics
    if show_stats:
        st.subheader("Summary Statistics")
        st.write(df.describe())

    # Histogram
    if show_plot:
        st.subheader("Feature Histogram")
        feature = st.selectbox("Select feature", df.columns, index=0)
        # Use a safe column name for Altair encoding
        df_plot = df[[feature]].rename(columns={feature: 'value'})
        st.bar_chart(df_plot)

    # Model predictions
    if run_prediction:
        try:
            model = joblib.load("src/artifacts/model.joblib")
            st.subheader("Predictions vs Actual")
            # Drop non-numeric columns before prediction
            df_features = df.select_dtypes(include=["number"])
            # Ensure we apply the same preprocessing pipeline (e.g., scaling/outlier handling)
            try:
                df_processed = preprocess_dataset(df_features)
            except Exception:
                # Fallback to raw numeric columns if preprocessing fails
                df_processed = df_features
            preds = model.predict(df_processed)
            # Build a results DataFrame with predictions
            results = pd.DataFrame({"predicted": preds}, index=df_processed.index)
            if "status" in df.columns:
                results["actual"] = df["status"].loc[df_processed.index]
            st.dataframe(results.head(10))
        except FileNotFoundError:
            st.error("Model file not found. Have you trained the model and placed 'model.joblib' in /artifacts?")

if __name__ == "__main__":
    main()