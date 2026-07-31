import streamlit as st
import plotly.express as px

st.title("📈 Data Visualization")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

numeric_columns = df.select_dtypes(include="number").columns.tolist()
all_columns = df.columns.tolist()

if len(all_columns) < 1:
    st.error("Dataset has no columns.")
    st.stop()

# ---------------------------
# Chart Selection
# ---------------------------

chart_type = st.selectbox(
    "Select Chart",
    [
        "Line Chart",
        "Bar Chart",
        "Scatter Plot",
        "Histogram",
        "Box Plot",
        "Violin Plot",
        "Pie Chart"
    ]
)

x = st.selectbox("X Axis", all_columns)

y = None

if chart_type != "Histogram":
    y = st.selectbox(
        "Y Axis",
        numeric_columns if numeric_columns else all_columns
    )

color = st.selectbox(
    "Color",
    ["None"] + all_columns
)

color = None if color == "None" else color

fig = None

# ---------------------------
# Line
# ---------------------------

if chart_type == "Line Chart":

    fig = px.line(
        df,
        x=x,
        y=y,
        color=color,
        title="Line Chart"
    )

# ---------------------------
# Bar
# ---------------------------

elif chart_type == "Bar Chart":

    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        title="Bar Chart"
    )

# ---------------------------
# Scatter
# ---------------------------

elif chart_type == "Scatter Plot":

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        title="Scatter Plot"
    )

# ---------------------------
# Histogram
# ---------------------------

elif chart_type == "Histogram":

    fig = px.histogram(
        df,
        x=x,
        color=color,
        title="Histogram"
    )

# ---------------------------
# Box Plot
# ---------------------------

elif chart_type == "Box Plot":

    fig = px.box(
        df,
        x=x,
        y=y,
        color=color,
        title="Box Plot"
    )

# ---------------------------
# Violin Plot
# ---------------------------

elif chart_type == "Violin Plot":

    fig = px.violin(
        df,
        x=x,
        y=y,
        color=color,
        box=True,
        title="Violin Plot"
    )

# ---------------------------
# Pie Chart
# ---------------------------

elif chart_type == "Pie Chart":

    fig = px.pie(
        df,
        names=x,
        title="Pie Chart"
    )

# ---------------------------
# Show Chart
# ---------------------------

if fig is not None:

    fig.update_layout(
        template="plotly_white",
        height=600
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Download HTML
    html = fig.to_html()

    st.download_button(
        "📥 Download Chart (HTML)",
        data=html,
        file_name="chart.html",
        mime="text/html"
    )