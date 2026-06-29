import pandas as pd

def generate_signal(df):

    if len(df) < 2:
        return "HOLD"

    last = df["close"].iloc[-1]
    previous = df["close"].iloc[-2]

    if last > previous:
        return "BUY"

    elif last < previous:
        return "SELL"

    return "HOLD"
