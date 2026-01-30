from core.jobs.jobstore import JobStore

store = JobStore()

def route_job(job_id, payload):
    return store.create(job_id, payload)
