from core.pipeline.orchestrators.render_v4_orchestrator import RenderOrchestratorV4

def register(p):
    p["RENDER_ORCHESTRATOR_V4"] = RenderOrchestratorV4
