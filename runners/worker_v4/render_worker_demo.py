import json, os
from core.render.engine_v4_stub import RenderEngineV4Stub

job_id = "render_worker_demo"
base = f"output/render/{job_id}"
os.makedirs(base, exist_ok=True)

plan = {"job_id": job_id, "media": {"path": "demo.mp4", "duration": 12.0}}
overlay = {"resolution": "1080x1920", "events": []}

plan_path = f"{base}/plan.json"
overlay_path = f"{base}/overlay.json"
session_path = f"{base}/session.json"

with open(plan_path, "w") as f:
    json.dump(plan, f, indent=2)
with open(overlay_path, "w") as f:
    json.dump(overlay, f, indent=2)

queue = "queue/render_v4"
os.makedirs(queue, exist_ok=True)
with open(f"{queue}/{job_id}.json", "w") as f:
    json.dump({
        "job_id": job_id,
        "plan_path": plan_path,
        "overlay_path": overlay_path,
        "session_path": session_path
    }, f, indent=2)

print("RENDER_WORKER_V4_JOB_QUEUED", job_id)
