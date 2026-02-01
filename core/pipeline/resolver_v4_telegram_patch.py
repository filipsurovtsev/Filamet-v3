from core.pipeline.tasks.telegram_post_v4 import TelegramPostTaskV4

def register(p, store):
    p["TELEGRAM_POST_V4"] = TelegramPostTaskV4(store)
