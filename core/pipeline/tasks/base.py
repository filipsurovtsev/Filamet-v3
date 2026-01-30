class BaseTask:
    def __init__(self, job_id, payload):
        self.job_id = job_id
        self.payload = payload
    def prepare(self): pass
    def execute(self): pass
    def finalize(self): pass
