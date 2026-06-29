from data.binance_data import get_data
from indicators.technical import add_indicators
from signals.signal_engine import generate_signal

# ⬇️ මේ line එක import section එකේ දාන්න
from news.news_engine import get_market_news, news_score


def main():

    print("🚀 Quant AI Trading System Started")

    df = get_data()

    df = add_indicators(df)

    signal = generate_signal(df)

    # ⬇️ මේ code එක main() function එක ඇතුළේ දාන්න
    news = get_market_news()
    score = news_score(news)

    print(f"Latest Price : {df['close'].iloc[-1]}")
    print(f"Signal       : {signal}")
    print(f"News Score   : {score}")


if __name__ == "__main__":
    main()
