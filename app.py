import streamlit as st

# Set wide layout and page title
st.set_page_config(page_title="CO₂ Emissions Forecasting App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.success("Select a page from the sidebar.")

# Home page content
st.title("🌍 CO₂ Emissions Forecasting Dashboard")
st.markdown("""
Welcome to the multi-page CO₂ emissions forecasting app!

### 🚀 Available Features:
- 📈 Country-wise emission forecasting
- 📊 Dashboard for trends & correlations
- 🛠️ Manual prediction with custom values
- 📤 Batch upload for multiple predictions
""")

# Friendly footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
