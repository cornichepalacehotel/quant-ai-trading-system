from flask import Blueprint, jsonify

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/health")
def health():

    return jsonify({
        "status": "ONLINE",
        "version": "2.0",
        "system": "Quant AI Trading System"
    })
