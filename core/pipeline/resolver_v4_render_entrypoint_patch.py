from core.pipeline.entrypoints.render_entrypoint_v4 import RenderEntrypointV4

def register(p):
    p["RENDER_ENTRYPOINT_V4"] = RenderEntrypointV4
