import streamlit as st
import pandas as pd

st.title("🧹 Data Cleaning")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"].copy()

st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.divider()

# ======================================
# Missing Values
# ======================================

st.header("1️⃣ Missing Values")

missing = df.isnull().sum()
missing = missing[missing > 0]

if len(missing) == 0:
    st.success("No missing values found.")
else:
    st.dataframe(
        missing.reset_index().rename(
            columns={"index": "Column", 0: "Missing Values"}
        ),
        use_container_width=True,
    )

st.divider()

# ======================================
# Remove Missing Values
# ======================================

st.header("2️⃣ Remove Missing Values")

if st.button("Remove Missing Rows"):
    df = df.dropna()
    st.session_state["df"] = df
    st.success("Missing rows removed successfully.")

st.divider()

# ======================================
# Fill Missing Values
# ======================================

st.header("3️⃣ Fill Missing Values")

numeric_columns = df.select_dtypes(include="number").columns.tolist()

if numeric_columns:

    col = st.selectbox(
        "Select Numeric Column",
        numeric_columns,
        key="fill_column"
    )

    method = st.selectbox(
        "Fill Method",
        ["Mean", "Median", "Mode"],
        key="fill_method"
    )

    if st.button("Fill Missing Values"):

        if method == "Mean":
            df[col].fillna(df[col].mean(), inplace=True)

        elif method == "Median":
            df[col].fillna(df[col].median(), inplace=True)

        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

        st.session_state["df"] = df

        st.success("Missing values filled successfully.")

else:
    st.info("No numeric columns found.")

st.divider()

# ======================================
# Duplicate Rows
# ======================================

st.header("4️⃣ Duplicate Rows")

duplicates = df.duplicated().sum()

st.write(f"Duplicate Rows : **{duplicates}**")

if st.button("Remove Duplicate Rows"):

    df = df.drop_duplicates()

    st.session_state["df"] = df

    st.success("Duplicate rows removed.")

st.divider()

# ======================================
# Drop Columns
# ======================================

st.header("5️⃣ Drop Columns")

drop_cols = st.multiselect(
    "Select Columns",
    df.columns
)

if st.button("Drop Selected Columns"):

    if drop_cols:

        df = df.drop(columns=drop_cols)

        st.session_state["df"] = df

        st.success("Columns dropped.")

st.divider()

# ======================================
# Rename Column
# ======================================

st.header("6️⃣ Rename Column")

old_name = st.selectbox(
    "Select Column",
    df.columns,
    key="rename_old"
)

new_name = st.text_input(
    "New Column Name"
)

if st.button("Rename Column"):

    if new_name.strip():

        df.rename(
            columns={old_name: new_name},
            inplace=True
        )

        st.session_state["df"] = df

        st.success("Column renamed.")

st.divider()

# ======================================
# Data Types
# ======================================

st.header("7️⃣ Change Data Type")

column = st.selectbox(
    "Column",
    df.columns,
    key="dtype_col"
)

dtype = st.selectbox(
    "New Data Type",
    ["int", "float", "str"],
)

if st.button("Convert Data Type"):

    try:

        if dtype == "int":
            df[column] = df[column].astype(int)

        elif dtype == "float":
            df[column] = df[column].astype(float)

        else:
            df[column] = df[column].astype(str)

        st.session_state["df"] = df

        st.success("Data type converted.")

    except Exception as e:

        st.error(e)

st.divider()

# ======================================
# Cleaned Dataset
# ======================================

st.header("Updated Dataset")

st.dataframe(
    st.session_state["df"],
    use_container_width=True
)