import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Global CO₂ Emissions Dashboard")

df = pd.read_csv("data/co2.csv")

country = st.selectbox("Select Country", df["country"].unique())
filtered = df[df["country"] == country]

fig = px.line(filtered, x="year", y="co2", title=f"CO₂ Emissions in {country}")
st.plotly_chart(fig)
