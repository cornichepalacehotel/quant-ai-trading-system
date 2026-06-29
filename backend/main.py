from data.binance_data import get_data
from indicators.technical import add_indicators
from signals.signal_engine import generate_signal
from news.news_engine import get_market_news, news_score


def print_header():
    print("=" * 50)
    print("🚀 QUANT AI TRADING SYSTEM v1.0")
    print("=" * 50)


def main():

    print_header()

    try:

        # Get Binance Market Data
        df = get_data()

        # Calculate Technical Indicators
        df = add_indicators(df)

        # Generate Trading Signal
        signal = generate_signal(df)

        # Get News Score
        news = get_market_news()
        score = news_score(news)

        # Latest Price
        latest_price = df["close"].iloc[-1]

        print(f"💰 Price        : {latest_price}")
        print(f"📈 Signal       : {signal}")
        print(f"📰 News Score   : {score}")

    except Exception as e:

        print("❌ ERROR")
        print(e)


if __name__ == "__main__":
    main()
