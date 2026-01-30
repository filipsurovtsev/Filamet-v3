from core.jobs.jobstore import JobStore
from core.pipeline.auto_advance import next_task
from core.pipeline.flow import pipeline_start, pipeline_finish, pipeline_fail

store = JobStore()

SUBTITLE_CHAIN = [
    "CAPTION",
    "TIMING",
    "SRT",
    "ASS"
]

def is_subtitles_task(t):
    return t in SUBTITLE_CHAIN

def next_subtask(t):
    if t not in SUBTITLE_CHAIN:
        return None
    idx = SUBTITLE_CHAIN.index(t)
    if idx + 1 < len(SUBTITLE_CHAIN):
        return SUBTITLE_CHAIN[idx + 1]
    return None

def run_subtitles_orchestrator(job):
    job_id = job["id"]
    t = job["type"]

    if not is_subtitles_task(t):
        return {"job_id": job_id, "error": "not_subtitles_task"}

    try:
        pipeline_start(job_id)
        nxt = next_subtask(t)

        if nxt:
            store.update_job(job_id, {"type": nxt})
        else:
            pipeline_finish(job_id)

        return {
            "job_id": job_id,
            "current": t,
            "next": nxt,
            "status": store.load_job(job_id)["status"]
        }

    except Exception as e:
        pipeline_fail(job_id, e)
        return {"job_id": job_id, "status": "failed", "error": str(e)}
