from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")

def home():

    return jsonify({
        "project": "Quant AI Trading System",
        "status": "Running",
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run(debug=True)
