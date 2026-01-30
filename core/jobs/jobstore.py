class JobStore:
    def __init__(self):
        self.jobs = {}

    def create(self, job_id, payload):
        self.jobs[job_id] = {
            "id": job_id,
            "payload": payload,
            "status": "queued",
            "output": {},
        }
        return self.jobs[job_id]

    def update_status(self, job_id, status):
        if job_id in self.jobs:
            self.jobs[job_id]["status"] = status

    def get(self, job_id):
        return self.jobs.get(job_id)

    def exists(self, job_id):
        return job_id in self.jobs
