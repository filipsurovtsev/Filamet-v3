from autopost.core.dispatcher_telegram_v3 import autopost_dispatch_telegram_v3
from autopost.platforms.telegram_real_v3 import telegram_real_autopost_v3

def run_autopost_telegram_flow_v3(payload):
    d = autopost_dispatch_telegram_v3(payload)
    if d.get("status") != "ok":
        return d
    text = d["text"]
    return telegram_real_autopost_v3(text)
