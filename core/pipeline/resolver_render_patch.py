from core.pipeline.tasks.render_v0 import RenderTaskV0

def resolve_render(job):
    return RenderTaskV0(job)
