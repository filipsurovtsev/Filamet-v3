import datetime

def validate_render_session(s):
    required = {"job_id","plan_path","overlay_path","created_at","status"}
    if set(s.keys()) != required:
        raise ValueError("invalid render_session keys")
    if not isinstance(s["job_id"], str):
        raise ValueError("job_id must be str")
    if not isinstance(s["plan_path"], str):
        raise ValueError("plan_path must be str")
    if not isinstance(s["overlay_path"], str):
        raise ValueError("overlay_path must be str")
    if not isinstance(s["created_at"], str):
        raise ValueError("created_at must be str")
    if s["status"] not in ("prepared","pending","skipped"):
        raise ValueError("invalid status")

def make_render_session(job_id, plan_path, overlay_path):
    return {
        "job_id": job_id,
        "plan_path": plan_path,
        "overlay_path": overlay_path,
        "created_at": datetime.datetime.utcnow().isoformat(),
        "status": "prepared"
    }
