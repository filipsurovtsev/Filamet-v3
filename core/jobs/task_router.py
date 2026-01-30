from typing import Dict, Any
from . import task_types as tt
from .task_rules import TASK_RULES


def validate_task_type(task_type: str) -> None:
    if task_type not in TASK_RULES:
        raise ValueError(f"Unknown task type: {task_type}")


def route_task(payload: Dict[str, Any]) -> Dict[str, Any]:
    task_type = payload.get("task_type")
    validate_task_type(task_type)
    return payload
