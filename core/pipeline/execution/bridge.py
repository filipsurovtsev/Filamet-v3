from core.pipeline.execution.executor import execute_task

def worker_bridge_v0(task):
    return execute_task(task)
