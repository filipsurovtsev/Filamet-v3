from core.pipeline.overlay.overlay_task_v3_strict import OverlayTaskV3Strict

def patch_resolver(resolver, store):
    resolver["OVERLAY_V3"] = OverlayTaskV3Strict(store)
    return resolver
