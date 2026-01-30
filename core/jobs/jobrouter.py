from core.jobs.jobstore import JobStore

store = JobStore()

def route_job(job):
    if not isinstance(job, dict):
        raise ValueError("route_job expects dict {id?, type, payload}")

    job_id = job.get("id")
    return store.create_job(job_id, job)
