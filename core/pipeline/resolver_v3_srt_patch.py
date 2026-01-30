from core.pipeline.srt.srt_task_v3 import SrtTaskV3

def patch_resolver(resolver, store):
    resolver["SRT_V3"] = SrtTaskV3(store)
    return resolver
