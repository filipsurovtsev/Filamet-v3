import os
import json
from datetime import datetime

def render_completion_hook_v4(job_id, session_path, outdir="logs/render_hooks_v4"):
    os.makedirs(outdir, exist_ok=True)

    event = {
        "job_id": job_id,
        "session_path": session_path,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "render_v4_completed"
    }

    path = os.path.join(outdir, f"{job_id}_completion.json")
    with open(path, "w") as f:
        json.dump(event, f, indent=2)

    return event
