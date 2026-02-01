STORE = {}

def get(job_id: str):
    if job_id not in STORE:
        STORE[job_id] = {
            "id": job_id,
            "status": "created",
            "output": {}
        }
    return STORE[job_id]

def set_output(job_id: str, key: str, value):
    job = get(job_id)
    job["output"][key] = value
    return job

def set_status(job_id: str, status: str):
    job = get(job_id)
    job["status"] = status
    return job
