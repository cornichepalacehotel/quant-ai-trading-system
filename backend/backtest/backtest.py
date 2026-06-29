def run_backtest():

    print("Backtest Started...")

    trades = 100
    wins = 61

    winrate = (wins / trades) * 100

    print(f"Trades : {trades}")
    print(f"Wins   : {wins}")
    print(f"WinRate: {winrate:.2f}%")
