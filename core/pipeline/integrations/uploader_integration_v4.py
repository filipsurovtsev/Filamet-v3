from core.pipeline.router import route_job

def integrate_uploader_v4(job_id, render_result):
    upload_res = route_job({
        "type": "UPLOAD_V4",
        "job_id": job_id,
        "payload": {"source": "post_render_v4"}
    })
    return {
        "render": render_result,
        "upload": upload_res
    }
