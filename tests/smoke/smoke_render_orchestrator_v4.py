from core.pipeline.orchestrators.render_v4_orchestrator import RenderOrchestratorV4

orc = RenderOrchestratorV4()
res = orc.run("smoke_orchestrator_v4")
print("ORCHESTRATOR_V4_SMOKE_OK", res)
