import asyncio
import sys
import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from BollingerBands import trade_logic

api_key = "ZlfXtBHk2cyhpFJGatdPLHzU7WHbR8uvkYLvqUcetEuETfgTUiCsp5o4iMU1AyT4"
api_secret = "tv0DViJB2DCGABLNfLKs5QQQsCzVfAn2R3GfVOja08aKwms06tnUEjFdc6iEv7NS"
client = Client(api_key, api_secret)
symbol = False

async def start(ticker: str):
    # get market depth
    depth = client.get_order_book(symbol=ticker)
    pprint.pprint(client.get_account())
    global symbol
    symbol = ticker
    trade_logic()

if __name__ == "__main__":
    asyncio.run(start(sys.argv[1]))


def get_data():
    symbol = 'BTCUSDT'
    starttime = '2 days ago UTC'  # to start for 1 day ago
    interval = '5m'
    bars = client.get_historical_klines(symbol, interval, starttime)
    pprint.pprint(bars)
    for line in bars:  # Keep only first 5 columns, "date" "open" "high" "low" "close"
        del line[5:]
    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])  # 2 dimensional tabular data
    return df

