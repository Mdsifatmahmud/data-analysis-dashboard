import streamlit as st

st.set_page_config(
    page_title="Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Analysis Dashboard")

st.markdown("""
Welcome to the **Data Analysis Dashboard**.

Use the sidebar to:

- 📂 Upload Dataset
- 📊 View Overview
- 🧹 Clean Data
- 🔍 Explore Data
- 📈 Create Visualizations
- 📥 Download Results

---
""")

st.info("Select a page from the left sidebar to get started.")