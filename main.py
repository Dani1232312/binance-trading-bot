import asyncio
import sys
from binance import Client
from BollingerBands import *


api_key = "ZlfXtBHk2cyhpFJGatdPLHzU7WHbR8uvkYLvqUcetEuETfgTUiCsp5o4iMU1AyT4"
api_secret = "tv0DViJB2DCGABLNfLKs5QQQsCzVfAn2R3GfVOja08aKwms06tnUEjFdc6iEv7NS"
client = Client(api_key, api_secret)
symbol = False


async def start(ticker: str):
    # get market information
    depth = client.get_order_book(symbol=ticker)
    global symbol
    symbol = ticker
    trade_logic()


if __name__ == "__main__":
    asyncio.run(start(sys.argv[1]))


def get_data():
    starttime = '3 days ago UTC'  # to start for 1 day ago
    interval = '5m'
    bars = client.get_historical_klines(symbol, interval, starttime)  # get information about the chart in the interval
    for line in bars:  # Keep only first 5 columns, "date" "open" "high" "low" "close"
        del line[5:]
    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])  # 2 dimensional tabular data
    return df
