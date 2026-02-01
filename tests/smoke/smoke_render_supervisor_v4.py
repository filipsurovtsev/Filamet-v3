from core.pipeline.supervisors.render_supervisor_v4 import RenderSupervisorV4
sup = RenderSupervisorV4()
res = sup.supervise("smoke_supervisor_v4")
print("RENDER_SUPERVISOR_V4_SMOKE_OK", res)
