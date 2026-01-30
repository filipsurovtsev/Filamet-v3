class JobStore:
    def __init__(self):
        self.jobs = {}

    def create_job(self, job_id, payload):
        self.jobs[job_id] = {
            "id": job_id,
            "payload": payload,
            "status": "queued",
            "output": {},
        }
        return self.jobs[job_id]

    def update_job(self, job_id, fields):
        if job_id in self.jobs:
            self.jobs[job_id].update(fields)

    def load_job(self, job_id):
        return self.jobs.get(job_id)

    def exists(self, job_id):
        return job_id in self.jobs
