import backtrader as bt

class MomentumStrategy(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=15)

    def next(self):
        if self.data.close > self.sma:
            self.buy()
        elif self.data.close < self.sma:
            self.sell()

class MeanReversionStrategy(bt.Strategy):
    def __init__(self):
        self.mean = bt.indicators.SimpleMovingAverage(self.data.close, period=30)

    def next(self):
        if self.data.close < self.mean:
            self.buy()
        elif self.data.close > self.mean:
            self.sell()

class TrendFollowingStrategy(bt.Strategy):
    def __init__(self):
        self.sma_short = bt.indicators.SimpleMovingAverage(self.data.close, period=50)
        self.sma_long = bt.indicators.SimpleMovingAverage(self.data.close, period=200)

    def next(self):
        if self.sma_short > self.sma_long:
            self.buy()
        elif self.sma_short < self.sma_long:
            self.sell()
