from core.jobs.jobstore import JobStore

store = JobStore()

def safe_task_run(job_id, payload):
    try:
        job = store.load_job(job_id)
        if not job:
            job = store.create_job(job_id, {"type": "UTILITY_ECHO", "payload": payload})
        store.update_job(job_id, {"status": "done"})
        return {"job_id": job_id, "status": "done"}
    except Exception as e:
        store.update_job(job_id, {"status": "failed"})
        return {"job_id": job_id, "status": "failed", "error": str(e)}

def worker_loop_v0():
    return "worker_loop_v0_ready"
