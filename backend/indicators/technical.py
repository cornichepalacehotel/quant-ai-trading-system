import ta

def add_indicators(df):

    df["rsi"] = ta.momentum.RSIIndicator(
        df["close"]
    ).rsi()

    df["ema20"] = ta.trend.EMAIndicator(
        df["close"],
        window=20
    ).ema_indicator()

    df["ema50"] = ta.trend.EMAIndicator(
        df["close"],
        window=50
    ).ema_indicator()

    macd = ta.trend.MACD(df["close"])

    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()

    return df
