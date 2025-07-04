import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# 🔑 Path to the trained model
MODEL_PATH = "models/emission_model.pkl"

# --------------------------------
# Model Loading
# --------------------------------
def load_model():
    return joblib.load(MODEL_PATH)

# --------------------------------
# Country Forecasting (Placeholder Example)
# --------------------------------
def forecast_emissions(model, country, years):
    base_emission = {
        "USA": 5000,
        "China": 10000,
        "India": 2500,
        "Germany": 800,
        "UK": 600,
        "Brazil": 500,
        "Canada": 700
    }.get(country, 1000)

    # Simple growth factor (replace with model-based forecasting)
    forecast_data = pd.DataFrame({
        "Year": list(range(2025, 2025 + years)),
        "Emission": [base_emission * (1 + 0.02) ** i for i in range(years)]
    })

    return forecast_data

# --------------------------------
# Dashboard Data & Visualizations
# --------------------------------
def get_dashboard_data():
    years = list(range(2000, 2025))
    emissions = np.random.normal(loc=5000, scale=500, size=len(years))
    gdp = np.random.normal(loc=60000, scale=5000, size=len(years))
    data = pd.DataFrame({
        "Year": years,
        "Emissions": emissions,
        "GDP": gdp
    })
    return data

def plot_trends(data):
    fig, ax = plt.subplots()
    ax.plot(data["Year"], data["Emissions"], label="Emissions")
    ax.plot(data["Year"], data["GDP"], label="GDP")
    ax.set_xlabel("Year")
    ax.set_ylabel("Value")
    ax.set_title("Emissions and GDP Trend")
    ax.legend()
    st.pyplot(fig)

def plot_correlation(data):
    corr = data.drop("Year", axis=1).corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# --------------------------------
# Manual Input Prediction
# --------------------------------
def manual_predict(model, input_features):
    df = pd.DataFrame([input_features])
    return model.predict(df)[0]

# --------------------------------
# Batch CSV Prediction
# --------------------------------
def batch_predict(model, input_df):
    predictions = model.predict(input_df)
    input_df['Predicted Emissions'] = predictions
    return input_df
