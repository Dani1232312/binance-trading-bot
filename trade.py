import pandas as pd

from main import client


def buy_or_sell(df):
    buy_list  = pd.to_numeric(df['buy'], downcast='float')
    sell_list = pd.to_numeric(df['sell'], downcast='float')
    for i in range(len(buy_list)):
         # get current price of the symbol
        current_price = client.get_symbol_ticker(symbol =symbol)
        if float(current_price['price']) >= sell_list[i]:  # sell order
            print("sell sell sell...")
            sell_order = client.order_market_sell(symbol=symbol, quantity=0.01)
            print(sell_order)
        elif float(current_price['price']) <= buy_list[i]:  # buy order
            print("buy buy buy...")
            buy_order = client.order_market_buy(symbol=symbol, quantity=0.001)
            print(buy_order)
        else:
            print("...do nothing...")
