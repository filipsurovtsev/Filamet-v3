from core.pipeline.segment.segment_task_v3 import SegmentTaskV3

def resolve_segment_v3(t):
    if t == "SEGMENT_V3":
        return SegmentTaskV3()
    return None
