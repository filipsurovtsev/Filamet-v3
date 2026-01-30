import json, uuid, os
from core.jobs.jobstore import JobStore
from core.jobs.jobrouter import route_job
from runners.worker.worker_loop_v0 import safe_task_run

job_id = str(uuid.uuid4())
store = JobStore()

job = store.create_job({
    "type": "UTILITY_PING",
    "payload": {"message": "ping"}
})
route_job(job)
safe_task_run(job["id"], store)

job2 = store.create_job({
    "type": "UTILITY_ECHO",
    "payload": {"message": "echo-test"}
})
route_job(job2)
safe_task_run(job2["id"], store)

job3 = store.create_job({
    "type": "TRANSCRIBE",
    "payload": {
        "media": {
            "path": "tests/smoke/demo.mp4",
            "kind": "video",
            "source": "local"
        }
    }
})
route_job(job3)
safe_task_run(job3, store)

job4 = store.create_job({
    "type": "SEGMENT",
    "payload": {"source_job_id": job3.job_id}
})
route_job(job4)
safe_task_run(job4, store)

job5 = store.create_job({
    "type": "CAPTION",
    "payload": {"source_job_id": job4.job_id}
})
route_job(job5)
safe_task_run(job5, store)

job6 = store.create_job({
    "type": "TIMING",
    "payload": {"source_job_id": job5.job_id}
})
route_job(job6)
safe_task_run(job6, store)

job7 = store.create_job({
    "type": "SRT",
    "payload": {"source_job_id": job6.job_id}
})
route_job(job7)
safe_task_run(job7, store)

job8 = store.create_job({
    "type": "ASS",
    "payload": {"source_job_id": job6.job_id}
})
route_job(job8)
safe_task_run(job8, store)

job9 = store.create_job({
    "type": "RENDER_PREP",
    "payload": {"source_job_id": job6.job_id}
})
route_job(job9)
safe_task_run(job9, store)

job10 = store.create_job({
    "type": "RENDER",
    "payload": {"source_job_id": job9.job_id}
})
route_job(job10)
safe_task_run(job10, store)

report = {
    "ping": job.status,
    "echo": job2.status,
    "transcribe": job3.status,
    "segment": job4.status,
    "caption": job5.status,
    "timing": job6.status,
    "srt": job7.status,
    "ass": job8.status,
    "render_prep": job9.status,
    "render": job10.status
}

with open("logs/smoke/health_report.json","w") as f:
    json.dump(report,f,indent=2)
