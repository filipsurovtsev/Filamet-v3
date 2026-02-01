from core.pipeline.router import route_job

print("RESOLVER_V4_SMOKE:", route_job({
    "type": "TELEGRAM_POST_V4",
    "job_id": "resolver_test",
    "payload": {"text": "resolver-v4-smoke", "token": "TEST", "chat_id": "TEST"}
}))
