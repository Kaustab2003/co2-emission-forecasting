# pages/6_data_exploration.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from statsmodels.tsa.seasonal import seasonal_decompose

st.title("📊 CO₂ Emissions Data Exploration")

# Upload data
uploaded_file = st.file_uploader("Upload your CSV data file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data", df)

    # Basic stats
    st.write("### Summary Statistics")
    st.write(df.describe())

    # Correlation heatmap
    st.write("### Correlation Heatmap")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    st.pyplot(plt)

    # Clustering Example
    if st.checkbox("Run KMeans Clustering on first 2 numeric columns"):
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if len(numeric_cols) >= 2:
            X = df[numeric_cols[:2]].dropna()
            kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
            st.write("Cluster Centers:", kmeans.cluster_centers_)

            plt.figure(figsize=(8, 5))
            plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=kmeans.labels_, cmap='viridis')
            plt.xlabel(numeric_cols[0])
            plt.ylabel(numeric_cols[1])
            plt.title("KMeans Clustering")
            st.pyplot(plt)

    # Time Series Decomposition
    if st.checkbox("Decompose First Time Series Column"):
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        if numeric_cols:
            column_to_decompose = numeric_cols[0]
            try:
                decomposition = seasonal_decompose(df[column_to_decompose].dropna(), period=12)
                fig = decomposition.plot()
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error in decomposition: {e}")
