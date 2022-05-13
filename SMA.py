def sma(data, window):
    sma = data.rolling(window = window).mean()
    return sma

tsla['sma_20'] = sma(tsla['close'], 20)
tsla.tail()