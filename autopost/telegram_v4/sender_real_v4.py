from autopost.telegram_v4.http_client_v4 import TelegramHTTPV4

class TelegramSenderRealV4:
    """
    Прямой отправитель сообщений в Telegram через HTTP v4.
    """

    def __init__(self, token: str, chat_id: str):
        self.client = TelegramHTTPV4(token, chat_id)

    def send_text(self, text: str):
        return self.client.send_text(text)

    def send_photo(self, path: str, caption=None):
        return self.client.send_photo(path, caption)
