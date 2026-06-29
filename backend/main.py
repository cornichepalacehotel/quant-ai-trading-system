from data.binance_data import get_data
from indicators.technical import add_indicators
from signals.signal_engine import generate_signal

def main():

    print("🚀 Quant AI Trading System Started")

    df = get_data()

    df = add_indicators(df)

    signal = generate_signal(df)

    print(f"Latest Price : {df['close'].iloc[-1]}")
    print(f"Signal       : {signal}")

if __name__ == "__main__":
    main()
