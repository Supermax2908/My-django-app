import os

import requests

from dotenv import load_dotenv
load_dotenv()

token = os.getenv("7570242252:AAGGQTC4pAAV7Smq70JaL8F0Jw1-Hg_BGSY")


def send_telegram_message(user_id, message):
    resp = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage',
        json={
            'chat_id': user_id,
            'text': message
        }
    )

    print(resp.json())


def set_webhook():
    resp = requests.post(
        f'https://api.telegram.org/bot{token}/setWebhook',
        json={
            'url': 'https://2015-188-163-9-77.ngrok-free.app/telegram'
        }
    )

    print(resp.json())


if __name__ == "__main__":
    chat_id = -4205273963

    send_telegram_message(chat_id, "Hello, I'll spam you!")