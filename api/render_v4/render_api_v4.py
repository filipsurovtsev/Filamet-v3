from core.pipeline.router import route_job

def handle_render_request_v4(request):
    job_id = request.get("job_id")
    payload = request.get("payload", {})
    return route_job({
        "type": "RENDER_ENTRYPOINT_V4",
        "job_id": job_id,
        "payload": payload
    })
