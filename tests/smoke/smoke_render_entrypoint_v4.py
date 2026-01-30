from core.pipeline.entrypoints.render_entrypoint_v4 import RenderEntrypointV4

ep = RenderEntrypointV4()
res = ep.run("smoke_render_entry_v4")
print("RENDER_ENTRYPOINT_V4_SMOKE_OK", res)
