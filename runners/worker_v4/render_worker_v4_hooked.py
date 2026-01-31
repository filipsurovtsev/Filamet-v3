import os, json, uuid, datetime
from core.render.engine_v4_stub import render_stub_v4
from core.render.hooks_v4.completion_hook_v4 import run_completion_hook

def run_worker_v4_hooked(job):
    job_id = job.get("job_id") or job.get("id") or str(uuid.uuid4())

    outdir = f"output/render/{job_id}"
    os.makedirs(outdir, exist_ok=True)

    # 1. Рендерим
    render_stub_v4(job_id)

    # 2. Путь до session.json
    session_path = f"{outdir}/session.json"

    # 3. Выполнить хуки (создаст файл если его нет)
    session = run_completion_hook(job_id, session_path)

    return {
        "job_id": job_id,
        "session_path": session_path,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "status": "render_v4_completed_hooked"
    }
