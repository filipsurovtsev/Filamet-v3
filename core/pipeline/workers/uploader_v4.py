class UploaderV4:
    def handle(self, job):
        job_id = job.get("job_id")
        return {
            "job_id": job_id,
            "status": "upload_ok_v4"
        }
