from flask import Flask, jsonify

from data.binance_data import get_data
from indicators.technical import add_indicators
from signals.signal_engine import generate_signal
from news.news_engine import get_market_news, news_score

app = Flask(__name__)


@app.route("/")
def home():

    return jsonify({
        "project": "Quant AI Trading System",
        "status": "Running",
        "version": "1.0"
    })


@app.route("/signal")
def signal():

    try:

        df = get_data()

        df = add_indicators(df)

        trade_signal = generate_signal(df)

        news = get_market_news()

        score = news_score(news)

        price = float(df["close"].iloc[-1])

        return jsonify({

            "symbol": "BTCUSDT",

            "price": price,

            "signal": trade_signal,

            "news_score": score,

            "status": "ONLINE"

        })

    except Exception as e:

        return jsonify({

            "status": "ERROR",

            "message": str(e)

        })


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
