class BaseContext:
    def __init__(self, job):
        self.job = job
    def get_job(self): return self.job
