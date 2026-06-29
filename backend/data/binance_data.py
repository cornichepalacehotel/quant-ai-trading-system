from binance.client import Client
import pandas as pd

client = Client()

def get_data(symbol="BTCUSDT", interval="1m", limit=100):

    klines = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )

    df = pd.DataFrame(
        klines,
        columns=[
            "time","open","high","low","close","volume",
            "close_time","quote_asset_volume",
            "number_of_trades",
            "taker_buy_base_asset_volume",
            "taker_buy_quote_asset_volume",
            "ignore"
        ]
    )

    df["close"] = df["close"].astype(float)

    return df
