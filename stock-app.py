import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of GOOGLE
""")

st.write('Select One Symbol')
tickerSymbol = st.selectbox("Choose Stock",('GOOGL','AAPL','TSLA','NDAQ','^BSESN','BTC-USD','ETH-USD'))
try:
    if not tickerSymbol:
        st.error('Please select one Symbol')
    else:
        tickerData = yf.Ticker(tickerSymbol)
        tickerDf = tickerData.history(period='1d',start='2010-5-31',end='2022-1-1')
        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
except:
    st.error("Please Select Atleast One Symbol")