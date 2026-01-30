JOBSTORE = {}

def create_job(job_id, payload):
    JOBSTORE[job_id] = {
        "id": job_id,
        "payload": payload,
        "status": "PENDING"
    }
    return JOBSTORE[job_id]

def get_job(job_id):
    return JOBSTORE.get(job_id)

def update_status(job_id, status):
    if job_id in JOBSTORE:
        JOBSTORE[job_id] = {
            **JOBSTORE[job_id],
            "status": status
        }
    return JOBSTORE.get(job_id)
