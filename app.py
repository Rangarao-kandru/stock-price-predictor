from flask import Flask, jsonify, request
import yfinance as yf
import requests

app = Flask(__name__)

API_KEY = 'your_iex_api_key'  # Replace with your own IEX Cloud API Key

@app.route('/')
def index():
    return "Welcome to the Stock Price Predictor API"

@app.route('/predict', methods=['POST'])
def predict():
    stock_symbol = request.json['symbol']
    
    # Fetch real-time data from IEX Cloud API
    url = f'https://cloud.iexapis.com/stable/stock/{stock_symbol}/quote?token={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    current_price = data['latestPrice']
    
    # Return a simple prediction (this is a placeholder - you can replace it with an actual model)
    prediction = current_price * 1.01  # Simple placeholder prediction: current price + 1%

    return jsonify({
        'stock_symbol': stock_symbol,
        'current_price': current_price,
        'predicted_price': prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
