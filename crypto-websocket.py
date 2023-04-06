from alpaca.data.live import CryptoDataStream

client = CryptoDataStream("API-KEY", "SECRET-KEY")


# Get quote
async def quote_data_handler(data):
    print("quote", data)


# Get trade
async def trade_data_handler(data):
    print("trade", data)


client.subscribe_quotes(quote_data_handler, "BTC/USD")

client.subscribe_trades(trade_data_handler, "BTC/USD")

client.run()
