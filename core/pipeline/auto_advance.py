from core.jobs.jobstore import JobStore
from core.pipeline.flow import pipeline_start, pipeline_finish, pipeline_fail

store = JobStore()

TASK_SEQUENCE = [
    "TRANSCRIBE",
    "SEGMENT",
    "CAPTION",
    "TIMING",
    "SRT",
    "ASS",
    "RENDER_PREP",
    "RENDER"
]

def next_task(current_type):
    if current_type not in TASK_SEQUENCE:
        return None
    idx = TASK_SEQUENCE.index(current_type)
    if idx + 1 < len(TASK_SEQUENCE):
        return TASK_SEQUENCE[idx + 1]
    return None

def auto_advance(job):
    job_id = job["id"]
    t = job["type"]

    try:
        pipeline_start(job_id)

        nt = next_task(t)
        if nt:
            store.update_job(job_id, {"type": nt})
        else:
            pipeline_finish(job_id)

        return {
            "job_id": job_id,
            "current": t,
            "next": nt,
            "status": store.load_job(job_id)["status"]
        }

    except Exception as e:
        pipeline_fail(job_id, e)
        return {"job_id": job_id, "status": "failed", "error": str(e)}
