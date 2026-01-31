from core.jobs.jobrouter import route_job
import time
from core.render.queue_v4 import RenderQueueV4
from core.jobs.jobrouter import route_job
from core.jobs.jobstore import JobStore

store = JobStore()
queue = RenderQueueV4(max_concurrent=1)

class RenderQueueDaemonV4:
    def __init__(self, queue, interval=1.0):
        self.queue = queue
        self.interval = interval

    def tick(self):
        if self.queue.can_start():
            job_id = self.queue.start_next()
            if job_id:
                route_job({
                    "type": "RENDER_V4",
                    "job_id": job_id,
                    "payload": {}
                })

        stats = self.queue.stats()
        running = stats["running"]
        for jid in running:
            job = store.load_job(jid)
            if job and job.get("status") in ("done", "failed"):
                self.queue.finish(jid)

        return self.queue.stats()

    def run(self, steps=5):
        out = []
        for _ in range(steps):
            out.append(self.tick())
            time.sleep(self.interval)
        return out
