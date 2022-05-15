import numpy as np
import pandas as pd
from binance.exceptions import BinanceAPIException

from main import get_data
from matplotlib import pyplot as plt


def plot_graph(symbol_df):
    df = symbol_df.astype(float)
    df[['close', 'sma', 'upper', 'lower']].plot()
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close price', fontsize=18)
    x_axis = df.index
    plt.fill_between(x_axis, df['lower'], df['upper'], color='grey', alpha=0.30)

    plt.scatter(df.index, df['buy'], color='purple', label='Buy', marker='^', alpha=1)  # purple = buy
    plt.scatter(df.index, df['sell'], color='red', label='Sell', marker='v', alpha=1)  # red = sell

    plt.show()


def trade_logic():
    # get the information of the ticker
    try:
        symbol_df = get_data()
        # standard bolingerbands calculation.
        period = 20
        # small-time Moving average. calculate 20 moving average using Pandas over close price
        symbol_df['sma'] = symbol_df['close'].rolling(period).mean()
        # Get standard deviation
        symbol_df['std'] = symbol_df['close'].rolling(period).std()
        # Calculate Upper Bollinger band
        symbol_df['upper'] = symbol_df['sma'] + (2 * symbol_df['std'])
        # Calculate Lower Bollinger band
        symbol_df['lower'] = symbol_df['sma'] - (2 * symbol_df['std'])

        # To print in human-readable date and time (from timestamp)
        symbol_df.set_index('date', inplace=True)
        symbol_df.index = pd.to_datetime(symbol_df.index, unit='ms')  # index set to first column = date_and_time

        # prepare buy and sell signals. The lists prepared are still panda dataframes with float nos
        close_list = pd.to_numeric(symbol_df['close'], downcast='float')
        upper_list = pd.to_numeric(symbol_df['upper'], downcast='float')
        lower_list = pd.to_numeric(symbol_df['lower'], downcast='float')
        symbol_df['buy'] = np.where(close_list < lower_list, symbol_df['close'], np.NaN)
        symbol_df['sell'] = np.where(close_list > upper_list, symbol_df['close'], np.NaN)

        with open('output.txt', 'w') as f:
            f.write(
                symbol_df.to_string()
            )

        plot_graph(symbol_df)
    except BinanceAPIException as e:
        pass

