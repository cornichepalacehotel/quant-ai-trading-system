from flask import Flask, jsonify
from data.binance_data import get_data
from indicators.technical import add_indicators
from signals.signal_engine import generate_signal

app = Flask(__name__)

@app.route("/status")
def status():

    df = get_data()
    df = add_indicators(df)

    signal = generate_signal(df)

    return jsonify({
        "symbol": "BTCUSDT",
        "price": float(df["close"].iloc[-1]),
        "signal": signal,
        "status": "ONLINE"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
