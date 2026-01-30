from core.context.media_context import MediaContext

class TaskContext:
    def __init__(self, job):
        self.job = job
        self.media = MediaContext()
        self.data = {}
    def set(self, k, v): self.data[k] = v
    def get(self, k): return self.data.get(k)
    def get_media(self): return self.media
