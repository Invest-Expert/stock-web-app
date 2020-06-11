import yfinance as yf
import streamlit as st

st.write("""
# Your First Stock Price Simple App
Shown Google stock volume, and closing price!
""")

# https://investexpert.co/how-to-get-stock-data-using-python
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-6-8', end='2020-6-8')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)