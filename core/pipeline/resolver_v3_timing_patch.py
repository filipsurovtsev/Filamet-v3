from core.pipeline.timing.timing_task_v3 import TimingTaskV3

def patch_resolver(resolver, store):
    resolver["TIMING_V3"] = TimingTaskV3(store)
    return resolver
