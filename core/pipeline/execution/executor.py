from core.pipeline.execution.lifecycle import lifecycle_run
from core.pipeline.execution.errors import PipelineError
from core.utils.safe import safe_run

def execute_task(task):
    result = safe_run(lambda: lifecycle_run(task))
    if isinstance(result, dict) and "error" in result:
        return {"status": "FAILED", "error": result["error"]}
    return {"status": "DONE"}
