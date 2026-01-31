import json
import os

from core.render.hooks_v4.hook_loader_v4 import call_completion_hook_v4

job_id = "hook_demo_v4"
session_path = "output/render/hook_demo_v4/session.json"
os.makedirs("output/render/hook_demo_v4", exist_ok=True)

with open(session_path, "w") as f:
    json.dump({"status": "prepared"}, f)

event = call_completion_hook_v4(job_id, session_path)
print("HOOK_V4_SMOKE_OK", event)
