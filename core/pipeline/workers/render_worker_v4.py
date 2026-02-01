from core.pipeline.orchestrators.render_v4_orchestrator import RenderOrchestratorV4
from core.pipeline.hooks.render_completion_hook_v4 import render_completion_hook_v4
from core.pipeline.integrations.uploader_integration_v4 import integrate_uploader_v4

class RenderWorkerV4:
    def handle(self, job):
        job_id = job.get("job_id")
        orch = RenderOrchestratorV4()
        base_result = orch.run(job_id)
        completed = render_completion_hook_v4(job_id, base_result)
        return integrate_uploader_v4(job_id, completed)
