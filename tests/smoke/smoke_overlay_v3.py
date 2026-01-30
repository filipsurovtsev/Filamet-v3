from core.jobs.jobrouter import route_job
from runners.worker.worker_loop_v0 import safe_task_run

job = route_job({
    "type": "OVERLAY_V3",
    "payload": {}
})

res = safe_task_run(job["id"], job["payload"])
print("OVERLAY_V3_SMOKE_OK", res)
