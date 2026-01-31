import requests
import json
import os

def telegram_real_autopost_v3(text):
    token = os.getenv("TG_API_TOKEN_V3")
    chat_id = os.getenv("TG_CHAT_ID_V3")

    if not token or not chat_id:
        return {"status": "failed", "error": "missing TG_API_TOKEN_V3 or TG_CHAT_ID_V3"}

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code != 200:
            return {"status": "failed", "error": f"tg_http_{r.status_code}", "body": r.text}
        data = r.json()
        if not data.get("ok"):
            return {"status": "failed", "error": "tg_api_error", "body": data}
        return {"status": "posted", "platform": "telegram", "text": text}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
