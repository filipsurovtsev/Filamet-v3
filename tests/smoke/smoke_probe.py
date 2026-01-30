from core.jobs.jobrouter import route_job
from runners.worker.worker_loop_v0 import safe_task_run

job = route_job({
    "type": "PROBE",
    "payload": {"input": "dummy.mp4"}
})

res = safe_task_run(job["id"], job["payload"])
print("SMOKE_PROBE_OK", res)
