from core.tasks.rules import validate_task_type
from core.jobs.jobstore import create_job

def route_task(job_id, task_type, payload):
    if not validate_task_type(task_type):
        return None
    return create_job(job_id, {"type": task_type, "payload": payload})
