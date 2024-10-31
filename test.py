import requests
from api_key import ALPHA_VANTAGE_API_KEY
from dotenv import load_dotenv
import os


def get_stock_price(symbol):
    load_dotenv()
    api_key = os.getenv("VANTAGE_KEY")
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': api_key
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if 'Time Series (1min)' in data:
        latest_time = list(data['Time Series (1min)'].keys())[0]
        latest_close = data['Time Series (1min)'][latest_time]['4. close']
        return float(latest_close)
    else:
        return None

if __name__ == "__main__":
    symbol = input("Enter the stock symbol: ")
    price = get_stock_price(symbol)
    if price:
        print(f"The current price of {symbol} is ${price:.2f}")
    else:
        print("Failed to retrieve the stock price.")