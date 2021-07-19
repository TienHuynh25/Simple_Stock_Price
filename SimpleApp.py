import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple Stock Price App  

Shown are the stock closing price and volume of Apple!  

""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-05-02', end='2020-7-18')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)
st.write("""
### Calendar
""")
st.dataframe(tickerData.calendar)

st.write("""
### Recommendation
""")
st.dataframe(tickerData.recommendations)


