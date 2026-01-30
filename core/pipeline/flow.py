from core.jobs.jobstore import JobStore

store = JobStore()

def pipeline_start(job_id):
    store.update_job(job_id, {"status": "running"})
    return {"job_id": job_id, "stage": "pipeline_start"}

def pipeline_finish(job_id):
    store.update_job(job_id, {"status": "done"})
    return {"job_id": job_id, "stage": "pipeline_finish"}

def pipeline_fail(job_id, error):
    store.update_job(job_id, {"status": "failed"})
    return {"job_id": job_id, "stage": "pipeline_failed", "error": str(error)}
