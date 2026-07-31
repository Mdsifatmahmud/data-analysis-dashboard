import streamlit as st
import pandas as pd

st.title("📥 Export Dataset")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

st.subheader("Preview")
st.dataframe(df.head(), use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Cleaned CSV",
    data=csv,
    file_name="cleaned_dataset.csv",
    mime="text/csv"
)

excel_file = "cleaned_dataset.xlsx"

with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    df.to_excel(writer, index=False)

with open(excel_file, "rb") as f:
    st.download_button(
        label="📥 Download Excel",
        data=f,
        file_name="cleaned_dataset.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )