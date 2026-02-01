from core.pipeline.supervisors.render_supervisor_v4 import RenderSupervisorV4
def register(p):
    p["RENDER_SUPERVISOR_V4"] = RenderSupervisorV4
