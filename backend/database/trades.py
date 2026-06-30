import sqlite3

class TradeDatabase:

    def __init__(self):

        self.conn = sqlite3.connect("trades.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS trades(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            symbol TEXT,

            signal TEXT,

            entry REAL,

            exit REAL,

            profit REAL

        )
        """)

        self.conn.commit()

    def add_trade(self, symbol, signal, entry):

        self.cursor.execute(
            "INSERT INTO trades(symbol, signal, entry) VALUES (?, ?, ?)",
            (symbol, signal, entry)
        )

        self.conn.commit()

    def close(self):
        self.conn.close()
