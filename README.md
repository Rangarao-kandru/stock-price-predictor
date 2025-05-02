# Stock Price Predictor

This is a simple stock price predictor website that fetches real-time stock data from the IEX Cloud API and provides a basic stock price prediction.

## How to Run Locally

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the Flask app:
    ```
    python app.py
    ```

3. Open your browser and visit `http://127.0.0.1:5000`.

4. Use the form to enter a stock symbol (e.g., `RELIANCE.NS`) and see the current price and a simple predicted price.

## Deployment (Optional)

If you want to deploy this to Heroku:
1. Push this project to a GitHub repository.
2. Create a Heroku app and connect it to the GitHub repository.
3. Use the "Deploy" button on Heroku to deploy the app.

## Requirements
- Python 3.x
- Flask
- yfinance
- requests
