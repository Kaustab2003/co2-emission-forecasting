import streamlit as st
import pandas as pd
from utils.utils import load_model, batch_predict

st.title("📤 Batch Upload for CO₂ Emissions Prediction")

st.write("""
Upload a CSV file containing the required input features.  
The app will run batch predictions and display the results.
""")

# Example template download
with st.expander("ℹ️ Expected CSV Format"):
    st.write("The CSV should have columns like:")
    st.code("Population,GDP,Energy Use", language='csv')

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.write("### Uploaded Data")
        st.dataframe(df)

        # Load model and predict
        model = load_model()
        results = batch_predict(model, df)

        st.write("### Batch Predictions")
        st.dataframe(results)

        # Download CSV
        csv = results.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv,
            file_name="batch_predictions.csv",
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Upload a CSV file to get started.")
