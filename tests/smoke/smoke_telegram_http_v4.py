from autopost.telegram_v4.sender_real_v4 import TelegramSenderV4Real

def run_smoke():
    sender = TelegramSenderV4Real(
        token="8156830593:AAEy6cj4xie776SUlu-LUsgUxGGHZFbj1Zs",
        chat_id="-1001513285361"
    )
    return sender.send_text("V4 real HTTP test")

if __name__ == "__main__":
    out = run_smoke()
    print("TELEGRAM_HTTP_V4_SMOKE_OK", out)
