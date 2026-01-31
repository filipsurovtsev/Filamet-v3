from autopost.telegram_v4.sender import TelegramSenderV4

def run_smoke():
    sender = TelegramSenderV4(token="TEST_TOKEN", chat_id="TEST_CHAT")
    
    res1 = sender.send_text("hello v4")
    res2 = sender.send_photo("/tmp/test.jpg")

    return {
        "text_result": res1,
        "photo_result": res2
    }

if __name__ == "__main__":
    out = run_smoke()
    print("TELEGRAM_V4_SENDER_STUB_SMOKE_OK", out)
