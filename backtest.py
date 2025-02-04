import backtrader as bt
import yfinance as yf
from strategies import MomentumStrategy, MeanReversionStrategy, TrendFollowingStrategy

def run_backtest(strategy, symbol='BTC-USD', start='2020-01-01', end='2025-01-01'):
    # Fetch Bitcoin data
    data = yf.download(symbol, start=start, end=end)
    data_feed = bt.feeds.PandasData(dataname=data)

    # Set up Cerebro engine
    cerebro = bt.Cerebro()
    cerebro.adddata(data_feed)
    cerebro.addstrategy(strategy)

    # Set initial capital and commission
    cerebro.broker.set_cash(1000)
    cerebro.broker.set_commission(commission=0.001)

    # Run the backtest
    cerebro.run()
    final_value = cerebro.broker.getvalue()
    return final_value
