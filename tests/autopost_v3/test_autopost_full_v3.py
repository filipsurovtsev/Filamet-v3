from autopost.tasks.autopost_flow_v3 import run_autopost_flow_v3

res = run_autopost_flow_v3({"platform": "telegram", "text": "smoke"})
print("AUTOPOST_FULL_V3_OK", res)
