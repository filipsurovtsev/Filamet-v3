from core.jobs.jobstore import get_job
from core.context.task_context import TaskContext
from core.context.runtime_context import RuntimeContext

def build_context(job_id):
    job = get_job(job_id)
    if not job: return None
    task_ctx = TaskContext(job)
    return RuntimeContext(job, task_ctx)
