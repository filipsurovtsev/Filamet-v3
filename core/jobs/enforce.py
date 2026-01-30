def enforce_immutable(job):
    return dict(job) if job else None

def enforce_status(job, allowed):
    if job and job.get("status") in allowed:
        return True
    return False
