import streamlit as st
from utils.utils import load_model, get_dashboard_data, plot_trends, plot_correlation

st.title("📊 Emission Dashboard")

model = load_model()

st.write("### Emissions Trends")
trend_data = get_dashboard_data()
plot_trends(trend_data)

st.write("### Correlation Heatmap")
plot_correlation(trend_data)
