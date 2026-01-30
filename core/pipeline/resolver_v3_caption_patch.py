from core.pipeline.caption.caption_task_v3 import CaptionTaskV3

def resolve_caption_v3(t):
    if t == "CAPTION_V3":
        return CaptionTaskV3()
    return None
