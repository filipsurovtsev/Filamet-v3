from typing import List, Set, Optional

class RenderQueueV4:
    def __init__(self, max_concurrent: int = 1):
        self.max_concurrent = max_concurrent
        self._pending: List[str] = []
        self._running: Set[str] = set()

    def enqueue(self, job_id: str) -> None:
        if not isinstance(job_id, str) or not job_id:
            raise ValueError("job_id must be non-empty string")
        self._pending.append(job_id)

    def can_start(self) -> bool:
        return len(self._running) < self.max_concurrent and len(self._pending) > 0

    def start_next(self) -> Optional[str]:
        if not self.can_start():
            return None
        job_id = self._pending.pop(0)
        self._running.add(job_id)
        return job_id

    def finish(self, job_id: str) -> None:
        if job_id in self._running:
            self._running.remove(job_id)

    def stats(self) -> dict:
        return {
            "pending": list(self._pending),
            "running": list(self._running),
            "max_concurrent": self.max_concurrent,
        }
