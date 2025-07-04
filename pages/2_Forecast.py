import streamlit as st
from utils.utils import load_model, forecast_emissions
import matplotlib.pyplot as plt

st.title("📈 Forecast CO₂ Emissions")

model = load_model()

country = st.selectbox("Select a Country:", ["USA", "China", "India", "Germany", "UK", "Brazil", "Canada"])
years = st.slider("Forecast for next N years:", min_value=1, max_value=30, value=20)

st.write(f"Forecasting CO₂ emissions for **{country}** over the next **{years}** years.")

if st.button("Generate Forecast"):
    forecast_df = forecast_emissions(model, country, years)

    st.write("### Emissions Forecast Data")
    st.dataframe(forecast_df)

    st.write("### Forecast Graph")
    fig, ax = plt.subplots()
    ax.plot(forecast_df['Year'], forecast_df['Emission'], marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("CO₂ Emissions (Mt)")
    ax.set_title(f"Emission Forecast for {country}")
    st.pyplot(fig)
