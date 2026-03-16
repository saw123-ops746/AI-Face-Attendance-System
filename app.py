import streamlit as st
import pandas as pd

st.title("AI Face Attendance Dashboard")

df = pd.read_excel("attendance.xlsx")

st.subheader("Attendance Data")

st.dataframe(df)

st.subheader("Attendance Count")

st.bar_chart(df["Name"].value_counts())