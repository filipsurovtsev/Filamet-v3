from core.jobs.jobrouter import route_job
from runners.worker.worker_loop_v0 import safe_task_run

job = route_job({
    "type": "SEGMENT_V3",
    "payload": {
        "text": "hello world\n\nsecond block"
    }
})

res = safe_task_run(job["id"], job["payload"])
print("SEGMENT_SMOKE_OK", res)
