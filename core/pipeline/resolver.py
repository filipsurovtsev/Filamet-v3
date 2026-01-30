from typing import Type

from core.pipeline.tasks.utility import PingTask, EchoTask
from core.pipeline.tasks.transcribe_v0 import TranscribeTask
from core.pipeline.tasks.segment_v0 import SimpleSegmentTask
from core.pipeline.tasks.caption_v0 import PureCaptionTask
from core.pipeline.tasks.timing_v0 import TimingTask
from core.pipeline.tasks.srt_v0 import SrtTask
from core.pipeline.tasks.ass_v0 import AssTask
from core.pipeline.tasks.render_prep_v0 import RenderPrepTask
from core.pipeline.tasks.base import BaseTask


TASK_REGISTRY: dict[str, Type[BaseTask]] = {
    "UTILITY_PING": PingTask,
    "UTILITY_ECHO": EchoTask,
    "TRANSCRIBE": TranscribeTask,
    "SEGMENT": SimpleSegmentTask,
    "CAPTION": PureCaptionTask,
    "TIMING": TimingTask,
    "SRT": SrtTask,
    "ASS": AssTask,
    "RENDER_PREP": RenderPrepTask,
}


def resolve_task(task_type: str) -> Type[BaseTask]:
    if task_type not in TASK_REGISTRY:
        raise ValueError(f"Unknown task_type: {task_type}")
    return TASK_REGISTRY[task_type]
