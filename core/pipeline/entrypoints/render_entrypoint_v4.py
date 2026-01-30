from core.pipeline.router import route_job

class RenderEntrypointV4:
    def run(self, job_id, payload=None):
        job = {
            "type": "RENDER_V4",
            "job_id": job_id,
            "payload": payload or {}
        }
        return route_job(job)
