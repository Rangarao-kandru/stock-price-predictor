import streamlit as st
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

st.set_page_config(page_title="Stock Price Predictor", layout="centered")

st.title("📈 Simple Stock Price Predictor")
st.write("This app predicts the next day's closing price using the last 30 days of stock data.")

symbol = st.text_input("Enter NSE Stock Symbol (e.g., RELIANCE.NS):", "RELIANCE.NS")

@st.cache_data
def fetch_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="30d")
        return data
    except Exception as e:
        return pd.DataFrame()

def train_model(data):
    if data.empty or len(data) < 5:
        return None, None
    X = data[['Open', 'High', 'Low', 'Volume']]
    y = data['Close']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = LinearRegression()
    model.fit(X_scaled, y)
    return model, scaler

if symbol:
    data = fetch_data(symbol)
    if not data.empty:
        st.line_chart(data['Close'], use_container_width=True)
        model, scaler = train_model(data)
        if model:
            latest_features = data[['Open', 'High', 'Low', 'Volume']].iloc[-1:]
            scaled_features = scaler.transform(latest_features)
            prediction = model.predict(scaled_features)
            st.success(f"Predicted next closing price for {symbol}: ₹{prediction[0]:.2f}")
        else:
            st.warning("Not enough data to train the model.")
    else:
        st.error("Failed to fetch data. Please check the stock symbol.")
