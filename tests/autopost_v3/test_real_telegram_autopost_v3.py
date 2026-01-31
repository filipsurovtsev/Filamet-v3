from autopost.tasks.autopost_telegram_flow_v3 import run_autopost_telegram_flow_v3

res = run_autopost_telegram_flow_v3({"text": "smoke test — real telegram v3"})
print("REAL_TELEGRAM_AUTOPOST_V3_SMOKE", res)
