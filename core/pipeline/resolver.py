from core.pipeline.tasks.utility import PingTask, EchoTask

def resolve_pipeline(job):
    payload = job.get("payload", {}) if isinstance(job, dict) else {}
    task_type = payload.get("task_type")
    job_id = job.get("id") if isinstance(job, dict) else None
    if not job_id and isinstance(payload, dict):
        job_id = payload.get("job_id")

    if task_type == "UTILITY_PING":
        return PingTask(job_id, payload)
    if task_type == "UTILITY_ECHO":
        return EchoTask(job_id, payload)
    return None
