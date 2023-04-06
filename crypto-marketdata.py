from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import (
    CryptoBarsRequest,
    CryptoLatestQuoteRequest,
    CryptoLatestTradeRequest,
    CryptoTradesRequest,
)
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

client = CryptoHistoricalDataClient()


# Get crypto bars
request_params = CryptoBarsRequest(
    symbol_or_symbols=["BTC/USD", "ETH/USD"],
    timeframe=TimeFrame.Day,
    start=datetime.strptime("2023-01-01", "%Y-%m-%d"),
)

bars = client.get_crypto_bars(request_params)
bars.df

print("bars", bars.df)


# Get crypto bars
request_params = CryptoTradesRequest(
    symbol_or_symbols=["BTC/USD", "ETH/USD"],
    start=datetime.strptime("2023-01-01", "%Y-%m-%d"),
    limit=1000,
)

trades = client.get_crypto_trades(request_params)
trades.df

print("trades", trades.df)


# Get latest crypto quote
request_params = CryptoLatestQuoteRequest(symbol_or_symbols=["BTC/USD", "ETH/USD"])
latest_quote = client.get_crypto_latest_quote(request_params)

# latest_quote["ETH/USD"].ask_price
# print("ETH/USD quote", latest_quote["ETH/USD"].ask_price)

print("quote", latest_quote)


# Get latest crypto trade
request_params = CryptoLatestTradeRequest(symbol_or_symbols=["BTC/USD", "ETH/USD"])
latest_trade = client.get_crypto_latest_trade(request_params)

# latest_trade["ETH/USD"].price
# print("ETH/USD trade", latest_trade["ETH/USD"].price)

print("trade", latest_trade)
