import uuid
from core.jobs.status import ensure_status

class JobStore:
    def __init__(self):
        self.jobs = {}

    def create_job(self, data_or_id=None, payload=None):
        if isinstance(data_or_id, dict):
            d = data_or_id
            job_id = d.get("id") or str(uuid.uuid4())
            task_type = d["type"]
            payload = d.get("payload", {})
            return self._create(job_id, task_type, payload)

        if isinstance(payload, dict) and "type" in payload:
            job_id = data_or_id or str(uuid.uuid4())
            task_type = payload["type"]
            payload = payload.get("payload", {})
            return self._create(job_id, task_type, payload)

        raise ValueError("Invalid create_job input")

    def _create(self, job_id, task_type, payload):
        job = {
            "id": job_id,
            "type": task_type,
            "payload": payload,
            "status": "queued",
            "output": {}
        }
        self.jobs[job_id] = job
        return job

    def update_job(self, job_id, fields: dict):
        job = self.jobs.get(job_id)
        if not job:
            return None

        if "status" in fields:
            ensure_status(fields["status"])

        job.update(fields)
        return job

    def load_job(self, job_id):
        return self.jobs.get(job_id)

    def exists(self, job_id):
        return job_id in self.jobs
