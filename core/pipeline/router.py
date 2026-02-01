from core.pipeline.resolver import TYPE_MAP, STORE

def route_job(job: dict):
    job_type = job.get("type")
    if job_type not in TYPE_MAP:
        return {"status": "error", "error": f"Unknown job type: {job_type}"}

    task = TYPE_MAP[job_type]
    job_id = job.get("job_id", "no_job_id")
    payload = job.get("payload", {})

    STORE[job_id] = {
        "input": payload,
        "output": {},
        "status": "pending"
    }

    return task.run(job_id, payload)
