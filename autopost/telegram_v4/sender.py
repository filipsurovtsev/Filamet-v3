class TelegramSenderV4:
    """
    V4 stub — никаких реальных HTTP-запросов.
    Только интерфейс + возврат мок-ответа.
    """

    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id

    def send_text(self, text: str):
        if not isinstance(text, str) or not text.strip():
            return {"status": "error", "error": "empty_text"}

        return {
            "status": "ok",
            "token": self.token,
            "chat_id": self.chat_id,
            "text": text,
            "mode": "stub"
        }

    def send_photo(self, path: str):
        return {
            "status": "ok",
            "mode": "stub_photo",
            "path": path
        }
