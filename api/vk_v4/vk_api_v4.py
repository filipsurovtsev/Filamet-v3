from core.pipeline.router import route_job

def handle_vk_post_v4(request: dict):
    job_id = request.get("job_id")
    payload = request.get("payload", {})
    return route_job({
        "type": "VK_POST_V4",
        "job_id": job_id,
        "payload": payload
    })
