from core.tasks.rules import allowed_status_for

def validate_job_status(job):
    if not job: return False
    t = job.get("payload", {}).get("type")
    st = job.get("status")
    return st in allowed_status_for(t)
