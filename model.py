import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import yfinance as yf

def recommend_strategy(symbol='BTC-USD', start='2020-01-01', end='2025-01-01'):
    # Download data
    data = yf.download(symbol, start=start, end=end)

    # Add features: Moving Averages, RSI, etc.
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()

    # Target variable: Predict if price will go up (1) or down (0)
    data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)

    # Features
    features = ['SMA_50', 'SMA_200']
    target = 'Target'

    # Train model
    model = DecisionTreeClassifier()
    model.fit(data[features].dropna(), data[target].dropna())
    prediction = model.predict(data[features].dropna())[-1]

    # Return recommended strategy
    if prediction == 1:
        return "Momentum"
    else:
        return "Mean Reversion"
