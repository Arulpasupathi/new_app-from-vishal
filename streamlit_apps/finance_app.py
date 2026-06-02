import yfinance as yf
import streamlit as st

st.title("Stock Dashboard")

tab1, tab2, tab3 = st.tabs(["Overview","Price chart","Volume"])

comp = st.text_input("Enter stock ticker",value="AAPL").upper()

data = yf.Ticker(comp)
df = data.history(start = "2019-01-01", end="2023-01-01")

with tab1:
    st.header("Stock Overview")
    st.dataframe(df)

with tab2:
    st.subheader("Closing Price Chart")
    st.line_chart(df["Close"])

with tab3:
    st.subheader("Volume Chart")
    st.bar_chart(df["Volume"])

