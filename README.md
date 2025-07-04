A Streamlit app for forecasting CO₂ emissions and exploring environmental data with machine learning and visualizations.

🚀 Features
Multi-page Streamlit app: Forecast, Dashboard, Manual Input, Batch Upload, Data Exploration.

Forecast CO₂ emissions using Population, GDP, Energy Use.

Visualize trends with interactive graphs.

Advanced EDA: pair plots, regression plots, clustering, time-series decomposition.

Generate automated EDA reports (Sweetviz/ydata-profiling).

Clean datasets and save as CSV.

📁 Project Structure
bash
Copy
Edit
carbon_emiision/
├── app.py                  # Main app entrypoint
├── models/emission_model.pkl
├── utils/utils.py           # Helper functions
├── sample_emissions.csv     # Test dataset
└── pages/
    ├── 1_Home.py
    ├── 2_Forecast.py
    ├── 3_Dashboard.py
    ├── 4_Manual_Prediction.py
    ├── 5_Batch_Upload.py
    └── 6_Data_Exploration.py
⚙️ Quick Start
bash
Copy
Edit
# Create environment
python -m venv venv
venv\Scripts\activate    # On Windows
pip install -r requirements.txt

# Run the app
streamlit run app.py
Visit: http://localhost:8501

🛠️ Tech Stack
Streamlit · Scikit-learn · Pandas · Seaborn · Sweetviz · YData Profiling