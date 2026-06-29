import pandas as pd

def add_indicators(df):
    # Simple Moving Averages
    df["sma20"] = df["close"].rolling(20).mean()
    df["sma50"] = df["close"].rolling(50).mean()

    return df
