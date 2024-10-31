import yfinance as yf


def current_price(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.history(period="1d")['Close'].iloc[-1]


print(current_price("MSFT"))
