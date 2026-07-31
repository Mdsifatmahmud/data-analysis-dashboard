import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🔍 Exploratory Data Analysis (EDA)")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

# ============================
# Dataset Preview
# ============================

st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.divider()

# ============================
# Search Data
# ============================

st.header("🔍 Search Data")

search = st.text_input("Search any value")

if search:
    result = df[
        df.astype(str)
          .apply(lambda row: row.str.contains(search, case=False).any(), axis=1)
    ]

    st.write(f"Found {len(result)} matching rows")
    st.dataframe(result, use_container_width=True)

st.divider()

# ============================
# Filter Data
# ============================

st.header("🎯 Filter Dataset")

filter_column = st.selectbox(
    "Choose Column",
    df.columns,
    key="filter_column"
)

unique_values = df[filter_column].dropna().unique()

selected = st.multiselect(
    "Choose Value(s)",
    unique_values
)

if selected:
    filtered_df = df[df[filter_column].isin(selected)]
    st.dataframe(filtered_df, use_container_width=True)

st.divider()

# ============================
# Sort Data
# ============================

st.header("↕️ Sort Dataset")

sort_col = st.selectbox(
    "Sort By",
    df.columns,
    key="sort_column"
)

ascending = st.checkbox("Ascending", value=True)

sorted_df = df.sort_values(sort_col, ascending=ascending)

st.dataframe(sorted_df.head(20), use_container_width=True)

st.divider()

# ============================
# Value Counts
# ============================

st.header("📊 Value Counts")

vc_col = st.selectbox(
    "Select Column",
    df.columns,
    key="value_counts"
)

counts = df[vc_col].value_counts()

st.dataframe(counts)

fig, ax = plt.subplots(figsize=(8,4))
counts.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

st.divider()

# ============================
# Unique Values
# ============================

st.header("🔢 Unique Values")

unique_col = st.selectbox(
    "Select Column",
    df.columns,
    key="unique"
)

st.metric(
    "Unique Values",
    df[unique_col].nunique()
)

st.write(df[unique_col].unique())

st.divider()

# ============================
# Correlation Matrix
# ============================

st.header("🔥 Correlation Matrix")

numeric_df = df.select_dtypes(include="number")

if numeric_df.shape[1] > 1:

    corr = numeric_df.corr()

    st.dataframe(corr)

    fig, ax = plt.subplots(figsize=(8,6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

else:

    st.info("Not enough numeric columns.")

st.divider()

# ============================
# Dataset Profile
# ============================

st.header("📋 Dataset Profile")

profile = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing": df.isnull().sum(),
    "Unique": df.nunique(),
})

st.dataframe(profile, use_container_width=True)