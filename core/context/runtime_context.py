class RuntimeContext:
    def __init__(self, job, task_context):
        self.job = job
        self.task_context = task_context
        self.runtime = {}
    def set(self, k, v): self.runtime[k] = v
    def get(self, k): return self.runtime.get(k)
    def get_task_context(self): return self.task_context
