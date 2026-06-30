from binance import ThreadedWebsocketManager

class BinanceSocket:

    def __init__(self, api_key="", api_secret=""):
        self.twm = ThreadedWebsocketManager(
            api_key=api_key,
            api_secret=api_secret
        )

    def start(self):
        self.twm.start()

    def stop(self):
        self.twm.stop()

    def handle_message(self, msg):
        try:
            candle = msg["k"]

            print(
                f"Price : {candle['c']} | Closed : {candle['x']}"
            )

        except Exception as e:
            print(e)

    def run(self):

        self.start()

        self.twm.start_kline_socket(
            callback=self.handle_message,
            symbol="btcusdt"
        )

        self.twm.join()
