from fastapi import FastAPI
import yfinance as yf
import pandas as pd

app = FastAPI()

@app.get("/predict")
async def get_prediction(ticker: str):
    # Fetch stock data from Yahoo Finance
    data = yf.download(ticker, period="5d", interval="1h")
    # Predict the next price (for simplicity, let's use the last closing price)
    predicted_price = data['Close'].iloc[-1] * 1.01  # Predicted price increases by 1%
    volume = data['Volume'].iloc[-1]
    trend = (data['Close'].pct_change().mean() * 100)  # Market trend in percentage

    return {
        "predicted_price": predicted_price,
        "volume": volume,
        "trend": trend
    }
    