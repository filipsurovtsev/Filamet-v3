from core.jobs.jobstore import JobStore
from core.pipeline.orchestrators.subtitles_v3 import run_subtitles_orchestrator

store = JobStore()

def run(job_id, payload):
    job = store.load_job(job_id)
    if not job:
        job = store.create_job(job_id, payload)
    return run_subtitles_orchestrator(job)
