from autopost.telegram_v4.sender_real_v4 import TelegramSenderRealV4

TOKEN = "PUT-YOUR-TOKEN"
CHAT = "PUT-YOUR-CHAT-ID"

def run_smoke():
    sender = TelegramSenderRealV4(TOKEN, CHAT)
    r = sender.send_text("🔥 Telegram FIXED HTTP V4 — SMOKE OK")
    print(r)
    return r

if __name__ == "__main__":
    out = run_smoke()
    print("TELEGRAM_HTTP_V4_SMOKE_OK", out)
