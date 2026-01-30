from core.pipeline.tasks.base import BaseTask
from core.utils.log import log

class UtilityTask(BaseTask):
    def log(self, message: str):
        log(f"[UtilityTask][{self.job_id}] {message}")

class PingTask(UtilityTask):
    def execute(self):
        self.log("ping")

class EchoTask(UtilityTask):
    def execute(self):
        message = None
        if isinstance(self.payload, dict):
            inner = self.payload.get("payload", {})
            if isinstance(inner, dict):
                message = inner.get("message")
        self.log(f"echo: {message}")
