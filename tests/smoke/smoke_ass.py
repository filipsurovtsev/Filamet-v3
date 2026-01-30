from core.jobs.jobrouter import route_job
from runners.worker.worker_loop_v0 import safe_task_run

job = route_job({
    "type": "ASS_V3",
    "payload": {
        "timings": [
            {"time": {"start": 0, "end": 1, "duration": 1}, "text": "hello"},
            {"time": {"start": 1, "end": 2, "duration": 1}, "text": "world"}
        ]
    }
})

res = safe_task_run(job["id"], job["payload"])
print("ASS_V3_SMOKE_OK", res)
