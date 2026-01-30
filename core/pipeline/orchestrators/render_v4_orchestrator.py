from core.jobs.jobrouter import route_job

class RenderOrchestratorV4:
    def run(self, job_id):
        steps = [
            {"type": "PROBE_V3", "job_id": job_id},
            {"type": "SEGMENT_V3", "job_id": job_id},
            {"type": "CAPTION_V3", "job_id": job_id},
            {"type": "TIMING_V3", "job_id": job_id},
            {"type": "SRT_V3", "job_id": job_id},
            {"type": "ASS_V3", "job_id": job_id},
            {"type": "RENDERPREP_V3", "job_id": job_id},
            {"type": "OVERLAY_V3", "job_id": job_id},
            {"type": "RENDER_V4", "job_id": job_id}
        ]
        res = None
        for s in steps:
            res = route_job(s)
        return res
