from api.telegram_v4.telegram_api_v4 import handle_telegram_post_v4

def run_smoke():
    req = {
        "job_id": "demo_telegram_v4",
        "payload": {
            "text": "V4 pipeline post",
            "token": "8156830593:AAEy6cj4xie776SUlu-LUsgUxGGHZFbj1Zs",
            "chat_id": "-1003487859711"
        }
    }
    return handle_telegram_post_v4(req)

if __name__ == "__main__":
    out = run_smoke()
    print("TELEGRAM_POST_V4_SMOKE_OK", out)
