from autopost.telegram_v4.http_client_v4 import send_text_v4

class TelegramSenderV4Real:
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id

    def send_text(self, text: str):
        return send_text_v4(self.token, self.chat_id, text)
