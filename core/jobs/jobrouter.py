from core.jobs.jobstore import JobStore

store = JobStore()

def route_job(job_id=None, payload=None):
    return store.create_job(job_id, payload)
