from core.jobs.jobstore import create_job, get_job, update_status

def route_job(job_id, payload):
    return create_job(job_id, payload)

def read_job(job_id):
    return get_job(job_id)

def set_status(job_id, status):
    return update_status(job_id, status)
