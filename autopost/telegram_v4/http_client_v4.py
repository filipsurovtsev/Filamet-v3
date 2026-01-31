import requests

BASE_URL = "https://api.telegram.org/bot{token}/{method}"

def send_text_v4(token: str, chat_id: str, text: str):
    url = BASE_URL.format(token=token, method="sendMessage")
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    r = requests.post(url, json=payload, timeout=10)
    try:
        return r.json()
    except:
        return {"ok": False, "error": "invalid_json", "status_code": r.status_code}
