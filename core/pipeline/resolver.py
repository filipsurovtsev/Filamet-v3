from core.pipeline.tasks.utility import UtilityPingTask, UtilityEchoTask
from core.pipeline.tasks.transcribe_v0 import TranscribeTaskV0
from core.pipeline.tasks.segment_v0 import SimpleSegmentTaskV0
from core.pipeline.tasks.caption_v0 import PureCaptionTaskV0
from core.pipeline.tasks.timing_v0 import TimingTaskV0
from core.pipeline.tasks.srt_v0 import SrtTaskV0
from core.pipeline.tasks.ass_v0 import AssTaskV0

TASK_REGISTRY = {
    "UTILITY_PING": UtilityPingTask,
    "UTILITY_ECHO": UtilityEchoTask,
    "TRANSCRIBE": TranscribeTaskV0,
    "SEGMENT": SimpleSegmentTaskV0,
    "CAPTION": PureCaptionTaskV0,
    "TIMING": TimingTaskV0,
    "SRT": SrtTaskV0,
    "ASS": AssTaskV0,
}

def resolve_task(task_type):
    if task_type not in TASK_REGISTRY:
        raise ValueError(f"Unknown task_type: {task_type}")
    return TASK_REGISTRY[task_type]
