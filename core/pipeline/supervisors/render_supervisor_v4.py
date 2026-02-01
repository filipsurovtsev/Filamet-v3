from core.pipeline.router import route_job

class RenderSupervisorV4:
    def supervise(self, job_id, payload=None):
        try:
            res = route_job({
                "type": "RENDER_ENTRYPOINT_V4",
                "job_id": job_id,
                "payload": payload or {}
            })
            return {
                "job_id": job_id,
                "status": "ok_v4",
                "result": res
            }
        except Exception as e:
            return {
                "job_id": job_id,
                "status": "fail_v4",
                "error": str(e)
            }
