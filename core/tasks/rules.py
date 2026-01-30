from core.tasks.registry import TASK_TYPES

def validate_task_type(task_type):
    return task_type in TASK_TYPES

def allowed_status_for(task_type):
    return TASK_TYPES.get(task_type, {}).get("allowed_status", [])
