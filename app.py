import streamlit as st
from utils.loader import load_data

st.set_page_config(
    page_title="Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Analysis Dashboard")
if "df" in st.session_state:

    df = st.session_state["df"]

    rows = df.shape[0]
    cols = df.shape[1]
    missing = int(df.isnull().sum().sum())
    duplicates = int(df.duplicated().sum())

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", rows)
    c2.metric("Columns", cols)
    c3.metric("Missing", missing)
    c4.metric("Duplicates", duplicates)

st.sidebar.title("Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    df = load_data(uploaded_file)

    st.session_state["df"] = df

    st.sidebar.success("Dataset Loaded")

else:

    st.sidebar.info("Upload a dataset")

st.markdown("""
# Welcome 👋

This dashboard lets you

- Upload CSV/Excel
- Clean Data
- Explore Data
- Visualize Data
- Download Results

Use the sidebar to navigate.
""")