from autopost.tasks.autopost_telegram_flow_v3 import run_autopost_telegram_flow_v3

def run_autoflow_v3():
    demo = {"text": "Autopost v3 — real Telegram demo message"}
    return run_autopost_telegram_flow_v3(demo)
