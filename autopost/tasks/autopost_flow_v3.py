from autopost.core.dispatcher_v3 import autopost_dispatch_v3
from autopost.platforms.telegram_v3 import autopost_telegram_v3
from autopost.platforms.youtube_v3 import autopost_youtube_v3

def run_autopost_flow_v3(payload):
    d = autopost_dispatch_v3(payload)
    if d.get("status") != "ok":
        return d

    platform = d["platform"]
    text = d["text"]

    if platform == "telegram":
        return autopost_telegram_v3(text)
    if platform == "youtube":
        return autopost_youtube_v3(text)

    return {"status": "failed", "error": "unknown platform"}
