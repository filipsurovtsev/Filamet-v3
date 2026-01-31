from autopost.telegram_v4.sender import TelegramSenderV4

sender = TelegramSenderV4(token="TEST_TOKEN", chat_id="TEST_CHAT")
res = sender.send_text("TELEGRAM_V4_SMOKE_POST")
print("TELEGRAM_V4_SMOKE_POST_OK", res)
