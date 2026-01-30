from core.pipeline.renderprep.render_session_task_v3_strict import RenderSessionTaskV3Strict

def patch_resolver(resolver, store):
    resolver["RENDERSESSION_V3"] = RenderSessionTaskV3Strict(store)
    return resolver
