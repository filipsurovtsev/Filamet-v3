from api.telegram_v4.telegram_api_v4 import handle_telegram_post_v4

req = {
    "job_id": "smoke_telegram_post_v4",
    "payload": {"text": "🔥 TELEGRAM_POST_V4 SMOKE TEST OK"}
}

res = handle_telegram_post_v4(req)
print("TELEGRAM_POST_V4_SMOKE_OK", res)
