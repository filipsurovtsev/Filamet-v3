import os, json, time
from core.pipeline.orchestrators.render_v4_orchestrator import RenderOrchestratorV4
from runners.queue_v4.renderqueue_daemon_v4 import RenderQueueDaemonV4, queue
from core.render.hooks_v4.hook_loader_v4 import call_completion_hook_v4

job_id = "full_render_v4_integration"

os.makedirs(f"output/render/{job_id}", exist_ok=True)
dummy_media = f"output/render/{job_id}/dummy.mp4"
with open(dummy_media, "w") as f:
    f.write("DUMMY")

orc = RenderOrchestratorV4()
pre = orc.run(job_id)

queue.enqueue(job_id)
daemon = RenderQueueDaemonV4(queue, interval=0.0)
daemon.run(steps=5)

session_path = f"output/render/{job_id}/session.json"
if os.path.exists(session_path):
    event = call_completion_hook_v4(job_id, session_path)
    print("FULL_RENDER_V4_INTEGRATION_OK", {
        "orchestrator": pre,
        "session_exists": True,
        "hook_event": event
    })
else:
    print("FULL_RENDER_V4_INTEGRATION_FAIL", {"error": "no session.json"})
