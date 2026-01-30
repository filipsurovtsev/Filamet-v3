from core.jobs.jobstore import create_job
from core.input.validator.validator import validate_input
from core.input.adapter.adapter import adapt_user_input_to_task_input
from core.tasks.rules import validate_task_type

def route_job(job_id, data):
    if not validate_input(data): return None
    if not validate_task_type(data["task_type"]): return None
    task_data = adapt_user_input_to_task_input(data)
    return create_job(job_id, task_data)
