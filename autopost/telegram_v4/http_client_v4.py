import requests

class TelegramHTTPV4:
    """
    Исправленный HTTP-клиент Telegram Bot API.
    100% корректный формат URL.
    """

    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.base = f"https://api.telegram.org/bot{token}/"  # ← критично: / на конце!

    def _post(self, method: str, data: dict, files=None):
        url = f"{self.base}{method}"  # например .../sendMessage
        try:
            r = requests.post(url, data=data, files=files, timeout=10)
            return r.json()
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def send_text(self, text: str):
        return self._post("sendMessage", {
            "chat_id": self.chat_id,
            "text": text
        })

    def send_photo(self, path: str, caption: str = None):
        try:
            with open(path, "rb") as f:
                return self._post(
                    "sendPhoto",
                    {"chat_id": self.chat_id, "caption": caption or ""},
                    files={"photo": f}
                )
        except FileNotFoundError:
            return {"ok": False, "error": "file_not_found"}
