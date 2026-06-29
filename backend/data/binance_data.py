from binance.client import Client
import pandas as pd
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)

def get_data():

    klines = client.get_klines(
        symbol=SYMBOL,
        interval=INTERVAL,
        limit=LIMIT
    )

    df = pd.DataFrame(
        klines,
        columns=[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_asset_volume",
            "number_of_trades",
            "taker_buy_base_asset_volume",
            "taker_buy_quote_asset_volume",
            "ignore"
        ]
    )

    numeric = ["open","high","low","close","volume"]

    for col in numeric:
        df[col] = df[col].astype(float)

    return df
