import requests
from config import *

def send_message(message):

    if TELEGRAM_BOT_TOKEN == "" or TELEGRAM_CHAT_ID == "":
        print("Telegram not configured")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
    )
