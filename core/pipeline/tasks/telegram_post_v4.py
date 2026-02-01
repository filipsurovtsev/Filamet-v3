from core.env.universal_secrets_loader_v4 import get
from autopost.telegram_v4.sender_real_v4 import TelegramSenderV4Real

def run_telegram_post_v4(payload):
    """
    Минимальная рабочая задача Telegram V4.
    Ожидает payload:
    {
        "text": "сообщение",
        "token": "...",
        "chat_id": "..."
    }
    """
    text = payload.get("text")
    token = payload.get("token")
    chat_id = payload.get("chat_id")

    if not token or not chat_id:
        return {"ok": False, "error": "missing_token_or_chat_id"}

    sender = TelegramSenderV4Real(token, chat_id)
    return sender.send_text(text or "V4 autopost default message")
