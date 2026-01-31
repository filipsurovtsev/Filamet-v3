from autopost.tasks.autopost_flow_v3 import run_autopost_flow_v3

def run_autoflow_v3():
    demo = {"platform": "telegram", "text": "Autopost v3 demo message"}
    return run_autopost_flow_v3(demo)
