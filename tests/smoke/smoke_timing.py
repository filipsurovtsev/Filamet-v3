from core.jobs.jobrouter import route_job
from runners.worker.worker_loop_v0 import safe_task_run

job = route_job({
    "type": "TIMING_V3",
    "payload": {
        "mock_probe": 10.0,
        "mock_captions": [
            {"caption_id": "c1", "text": "one"},
            {"caption_id": "c2", "text": "two"},
            {"caption_id": "c3", "text": "three"}
        ]
    }
})

res = safe_task_run(job["id"], job["payload"])
print("TIMING_SMOKE_OK", res)
