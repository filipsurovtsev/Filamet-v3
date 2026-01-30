from core.pipeline.ass.ass_task_v3 import AssTaskV3

def patch_resolver(resolver, store):
    resolver["ASS_V3"] = AssTaskV3(store)
    return resolver
