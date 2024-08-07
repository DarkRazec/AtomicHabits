import requests
from config.settings import TG_BOT_TOKEN, TELEGRAM_URL


def send_tg_message(chat_id: str, message: str) -> None:
    """
    Sending message to tg chat
    :param chat_id: telegram's chat id
    :param message: message to send
    """
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{TELEGRAM_URL}{TG_BOT_TOKEN}/sendMessage', params=params)
