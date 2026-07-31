import streamlit as st

st.title("📊 Dataset Overview")

if "df" not in st.session_state:

    st.warning("Please upload a dataset from the Home page.")

    st.stop()

df = st.session_state["df"]

# --------------------
# Metrics
# --------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Missing Values", int(df.isnull().sum().sum()))
c4.metric("Duplicate Rows", int(df.duplicated().sum()))

# --------------------
# Preview
# --------------------

st.subheader("Dataset Preview")

st.dataframe(df, use_container_width=True)

# --------------------
# Columns
# --------------------

st.subheader("Columns")

st.write(df.columns.tolist())

# --------------------
# Data Types
# --------------------

st.subheader("Data Types")

st.dataframe(df.dtypes.astype(str).reset_index().rename(
    columns={
        "index":"Column",
        0:"Data Type"
    }
))

# --------------------
# Missing Values
# --------------------

st.subheader("Missing Values")

missing = df.isnull().sum().reset_index()

missing.columns = ["Column","Missing"]

st.dataframe(missing)

# --------------------
# Statistics
# --------------------

st.subheader("Summary Statistics")

st.dataframe(df.describe(include="all"))