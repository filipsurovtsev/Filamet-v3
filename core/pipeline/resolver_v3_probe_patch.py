from core.tasks.probe_task_v0 import ProbeTaskV0

def resolve_task_v3(t):
    if t == "PROBE":
        return ProbeTaskV0()
    return None
