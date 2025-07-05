import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils.utils import load_model

# Advanced visualization libraries
from sklearn.cluster import KMeans
from statsmodels.tsa.seasonal import seasonal_decompose

# ---------- Load Data ----------
def load_data(file_path):
    return pd.read_csv(file_path)

# ---------- Main ----------
def main():
    st.title("🔍 Advanced Data Exploration - CO₂ Emissions Dataset")

    file_path = "data/data_cleaned.csv"

    try:
        df = load_data(file_path)

        st.write("### 📂 Loaded Dataset")
        st.dataframe(df)

        # ---------- Summary ----------
        st.write("### 📝 Dataset Summary")
        st.write(df.describe())

        # ---------- Correlation Heatmap ----------
        st.write("### 🔥 Correlation Heatmap")
        corr = df.corr(numeric_only=True)
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        # ---------- Emissions Trend ----------
        st.write("### 📈 Emissions Over Years")
        if 'Year' in df.columns and 'Emissions' in df.columns:
            st.line_chart(df.set_index('Year')['Emissions'])

        # ---------- Feature Distribution ----------
        st.write("### 📊 Feature Distribution")
        num_cols = df.select_dtypes(include='number').columns
        selected_feature = st.selectbox("Feature to plot", num_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_feature], kde=True, ax=ax)
        ax.set_title(f"Distribution of {selected_feature}")
        st.pyplot(fig)

        # ---------- Scatter Plot ----------
        st.write("### 🔗 Scatter Plot - Feature Relationships")
        x_feature = st.selectbox("X-axis Feature", num_cols, key="x_feature")
        y_feature = st.selectbox("Y-axis Feature", num_cols, key="y_feature")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_feature, y=y_feature, ax=ax)
        ax.set_title(f"{x_feature} vs {y_feature}")
        st.pyplot(fig)

        # ---------- Regression Plot ----------
        st.write("### 📉 Regression Plot")
        x_reg = st.selectbox("X-axis (regression)", num_cols, key="reg_x")
        y_reg = st.selectbox("Y-axis (regression)", num_cols, key="reg_y")
        fig, ax = plt.subplots()
        sns.regplot(data=df, x=x_reg, y=y_reg, ax=ax)
        ax.set_title(f"Regression: {x_reg} vs {y_reg}")
        st.pyplot(fig)

        # ---------- Pair Plot ----------
        st.write("### 🔎 Pair Plot")
        if st.button("Generate Pair Plot"):
            fig = sns.pairplot(df[num_cols])
            st.pyplot(fig)

        # ---------- Time Series Decomposition ----------
        st.write("### ⏳ Time Series Decomposition")
        if 'Year' in df.columns and 'Emissions' in df.columns:
            try:
                ts = df.set_index('Year')['Emissions']
                result = seasonal_decompose(ts, model='additive', period=1)
                fig = result.plot()
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("➡️ Add 'Year' and 'Emissions' columns for time series analysis.")

        # ---------- Feature Importance ----------
        st.write("### 🧠 Feature Importance (Model-based)")
        try:
            model = load_model()
            importances = model.feature_importances_
            feature_names = df.select_dtypes(include='number').drop('Emissions', axis=1, errors='ignore').columns
            importance_df = pd.DataFrame({
                'Feature': feature_names,
                'Importance': importances
            }).sort_values(by='Importance', ascending=False)

            fig, ax = plt.subplots()
            sns.barplot(x='Importance', y='Feature', data=importance_df, ax=ax)
            ax.set_title("Feature Importances")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error loading model: {e}")

        # ---------- Clustering ----------
        st.write("### 🔍 KMeans Clustering")
        num_clusters = st.slider("Number of Clusters", 2, 10, 3)
        clustering_features = df.select_dtypes(include='number').drop('Emissions', axis=1, errors='ignore')
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        df['Cluster'] = kmeans.fit_predict(clustering_features)

        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=clustering_features.columns[0], y=clustering_features.columns[1], hue='Cluster', palette="tab10", ax=ax)
        ax.set_title("KMeans Clustering")
        st.pyplot(fig)

        # ---------- Cleaning Pipeline ----------
        st.write("### 🧹 Basic Data Cleaning")
        if st.checkbox("Drop missing values"):
            df = df.dropna()
            st.success("Missing values dropped.")
        if st.checkbox("Remove duplicate rows"):
            df = df.drop_duplicates()
            st.success("Duplicates removed.")

        # ---------- Save Cleaned Data ----------
        st.write("### ✅ Save Cleaned Data")
        if st.button("Save as cleaned_v2.csv"):
            df.to_csv("cleaned_v2.csv", index=False)
            st.success("Cleaned data saved as cleaned_v2.csv!")

        # ---------- CSV Export ----------
        st.write("### 📥 Export Current Data as CSV")
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv_data, file_name="explored_data.csv", mime="text/csv")

    except FileNotFoundError:
        st.error(f"❌ File not found: {file_path}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# ---------- Run ----------
if __name__ == "__main__":
    main()
