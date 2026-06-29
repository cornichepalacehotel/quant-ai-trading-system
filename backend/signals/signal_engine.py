def generate_signal(df):

    last = df.iloc[-1]

    buy = (
        last["ema20"] > last["ema50"]
        and last["macd"] > last["macd_signal"]
        and last["rsi"] < 70
    )

    sell = (
        last["ema20"] < last["ema50"]
        and last["macd"] < last["macd_signal"]
        and last["rsi"] > 30
    )

    if buy:
        return "BUY"

    if sell:
        return "SELL"

    return "HOLD"
