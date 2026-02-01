from core.pipeline.router import route_job
res = route_job({"type": "RENDER_V4", "job_id": "smoke_uploader_integration_v4"})
print("UPLOADER_INTEGRATION_V4_SMOKE_OK", res)
