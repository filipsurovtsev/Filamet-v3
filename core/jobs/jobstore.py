class JobStore:
    def __init__(self):
        self.jobs = {}

    def create_job(self, job_id, payload):
        job = {
            "id": job_id,
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
        job.update(fields)
        return job

    def load_job(self, job_id):
        return self.jobs.get(job_id)

    def exists(self, job_id):
        return job_id in self.jobs
