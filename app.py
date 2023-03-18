import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
# from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
plt.style.use('fivethirtyeight')
import datetime as dt
from keras.models import load_model
import streamlit as st

import yfinance as yf

start=dt.datetime(2010,1,1)
end=dt.datetime(2017,1,1)

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter the stock ticker','AAPL')
df = yf.download(tickers=[user_input], start=start, end=end)

#describing data
st.subheader('Data from 2010 - 2017')
st.write(df.describe())

# Visualization
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize= (12,6))
plt.plot(df.Close)
st.pyplot(fig)