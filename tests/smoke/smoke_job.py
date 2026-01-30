from core.jobs.jobrouter import route_job
from runners.worker.worker_loop_v0 import safe_task_run

job = route_job({"type": "UTILITY_ECHO", "payload": {"text": "ok"}})
job_id = job["id"]

res = safe_task_run(job_id, job["payload"])
print("SMOKE_OK", res)
