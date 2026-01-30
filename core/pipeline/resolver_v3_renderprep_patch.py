from core.pipeline.renderprep.renderprep_task_v3_strict import RenderPrepStrictTaskV3

def patch_resolver(resolver, store):
    resolver["RENDERPREP_V3"] = RenderPrepStrictTaskV3(store)
    return resolver
