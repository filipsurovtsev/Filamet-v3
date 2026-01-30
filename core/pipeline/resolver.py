from typing import Dict, Type

from core.pipeline.tasks.base import BaseTask
from core.pipeline.tasks.utility import PingTask, EchoTask
from core.pipeline.tasks.transcribe import TranscribeTask
from core.pipeline.tasks.segment import SimpleSegmentTask
from core.pipeline.tasks.caption_v0 import PureCaptionTask

TASK_REGISTRY: Dict[str, Type[BaseTask]] = {
    "UTILITY_PING": PingTask,
    "UTILITY_ECHO": EchoTask,
    "TRANSCRIBE": TranscribeTask,
    "SEGMENT": SimpleSegmentTask,
    "CAPTION": PureCaptionTask,
}

def resolve_task(task_type: str) -> Type[BaseTask]:
    try:
        return TASK_REGISTRY[task_type]
    except KeyError as exc:
        raise ValueError(f"Unknown task type: {task_type}") from exc
