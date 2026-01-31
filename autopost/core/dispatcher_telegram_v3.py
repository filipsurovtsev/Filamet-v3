def autopost_dispatch_telegram_v3(payload):
    text = payload.get("text")
    if not text:
        return {"status": "failed", "error": "missing text"}
    return {"status": "ok", "text": text}
