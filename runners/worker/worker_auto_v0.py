from core.jobs.jobstore import JobStore
from core.pipeline.auto_advance import auto_advance

store = JobStore()

def run_auto(job_id, payload):
    job = store.load_job(job_id)
    if not job:
        job = store.create_job(job_id, payload)

    return auto_advance(job)
