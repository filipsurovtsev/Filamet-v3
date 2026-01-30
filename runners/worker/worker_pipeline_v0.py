from core.jobs.jobstore import JobStore
from core.pipeline.flow import pipeline_start, pipeline_finish, pipeline_fail

store = JobStore()

def run_pipeline(job_id, payload):
    try:
        pipeline_start(job_id)
        pipeline_finish(job_id)
        return {"job_id": job_id, "status": "done"}
    except Exception as e:
        pipeline_fail(job_id, e)
        return {"job_id": job_id, "status": "failed", "error": str(e)}
