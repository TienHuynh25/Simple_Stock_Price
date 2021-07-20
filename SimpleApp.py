import yfinance as yf
import streamlit as st
from datetime import date

companies = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'GOOGL', 'FB', 'TSLA', 'NVDA', 'NKE', 'ADBE', 'ORCL', 'VZ','INTC', 'PEP']
today = date.today()

st.write("""
# Simple Stock Price App  

Shown are the stock closing price, volume, calender and recommendation  of selected company!  

""")
st.markdown("### **Select Company**")

tickerSymbol = st.selectbox('', companies)

startDate = st.date_input("Pick start date",max_value=today)
if startDate:
    endDate = st.date_input("Pick end date",min_value=startDate,max_value=today)


tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=startDate, end=endDate)


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

