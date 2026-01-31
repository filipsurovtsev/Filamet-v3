from autopost.telegram_v4.sender_real_v4 import TelegramSenderRealV4

TOKEN = "PUT-YOUR-REAL-TOKEN-HERE"
CHAT  = "PUT-YOUR-CHAT-ID-HERE"

def run_smoke():
    sender = TelegramSenderRealV4(TOKEN, CHAT)

    r1 = sender.send_text("🔥 Telegram V4 HTTP — SMOKE OK")
    return {"text": r1}

if __name__ == "__main__":
    out = run_smoke()
    print("TELEGRAM_HTTP_V4_SMOKE_OK", out)
