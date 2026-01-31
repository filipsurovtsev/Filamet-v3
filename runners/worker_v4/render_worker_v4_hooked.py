import time
import json
import os
from core.render.engine_v4_stub import RenderEngineV4Stub
from core.render.hooks_v4.hook_loader_v4 import call_completion_hook_v4

def main():
    worker_id = "render_worker_v4_hooked"
    print(f"[{worker_id}] started")

    inbox = "queue/render_v4"
    os.makedirs(inbox, exist_ok=True)

    while True:
        jobs = [f for f in os.listdir(inbox) if f.endswith(".json")]
        if not jobs:
            time.sleep(1)
            continue

        for jfile in jobs:
            path = os.path.join(inbox, jfile)
            with open(path, "r") as f:
                job = json.load(f)

            job_id = job["job_id"]
            plan = job["plan_path"]
            overlay = job["overlay_path"]
            session = job["session_path"]

            engine = RenderEngineV4Stub(job_id, plan, overlay, session)
            engine.load_plan()
            engine.load_overlay()
            engine.prepare_session()
            result = engine.run()

            call_completion_hook_v4(job_id, session)

            os.remove(path)

        time.sleep(0.2)

if __name__ == "__main__":
    main()
