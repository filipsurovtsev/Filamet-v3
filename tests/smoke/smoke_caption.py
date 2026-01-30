from core.jobs.jobrouter import route_job
from runners.worker.worker_loop_v0 import safe_task_run

segments = [
    {"id": "s1", "index": 0, "text": "Hello world", "meta": {"length": 11}},
    {"id": "s2", "index": 1, "text": "Second block", "meta": {"length": 12}}
]

job = route_job({
    "type": "CAPTION_V3",
    "payload": {"segments": segments}
})

res = safe_task_run(job["id"], job["payload"])
print("CAPTION_SMOKE_OK", res)
