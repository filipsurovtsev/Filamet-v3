def autopost_dispatch_v3(payload):
    platform = payload.get("platform")
    text = payload.get("text")
    if not platform or not text:
        return {"status": "failed", "error": "missing platform or text"}
    return {"status": "ok", "platform": platform, "text": text}
