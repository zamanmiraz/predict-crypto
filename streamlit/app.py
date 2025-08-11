import streamlit as st
import pandas as pd
import altair as alt

st.title("Time Series Forecasting Demo")
st.write("Interactive portfolio project showcasing exploratory data analysis and forecasting.")

# Example data
date_rng = pd.date_range(start="2024-01-01", end="2024-03-01", freq="D")
df = pd.DataFrame({
    'date': date_rng,
    'value': pd.Series(range(len(date_rng))) + pd.Series(range(len(date_rng))).apply(lambda x: x**0.5*5)
})

chart = alt.Chart(df).mark_line().encode(
    x='date',
    y='value'
).interactive()

st.altair_chart(chart, use_container_width=True)
