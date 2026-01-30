from core.jobs.jobrouter import route_job
from core.utils.log import log
from core.context.link import build_context
from core.pipeline.resolver import resolve_pipeline
from core.pipeline.execution.bridge import worker_bridge_v0
from core.jobs.jobrouter import route_job
from core.utils.log import log
from core.context.link import build_context
from core.pipeline.resolver import resolve_pipeline
from core.pipeline.execution.bridge import worker_bridge_v0

def create_and_run(job_id: str, task_type: str, payload: dict):
    data = {"job_id": job_id, "task_type": task_type, "payload": payload}
    job = route_job(job_id, data)
    if not job:
        log(f"{job_id}: invalid input")
        return

    ctx = build_context(job_id)
    if not ctx:
        log(f"{job_id}: context build failed")

    task = resolve_pipeline(job)
    if not task:
        log(f"{job_id}: no task resolved")
        return

    result = worker_bridge_v0(task)
    log(f"{job_id}: result={result}")

def main():
    create_and_run("job_utility_ping_v3", "UTILITY_PING", {})
    create_and_run("job_utility_echo_v3", "UTILITY_ECHO", {"message": "hello v3 utility"})

if __name__ == "__main__":
    main()
