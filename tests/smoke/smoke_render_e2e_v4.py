from core.pipeline.orchestrators.render_e2e_v4 import RenderOrchestratorE2E_V4
orc = RenderOrchestratorE2E_V4()
res = orc.run("smoke_e2e_v4")
print("RENDER_E2E_V4_SMOKE_OK", res)
