from core.render.hooks_v4.completion_hook_v4 import run_completion_hook

def call_completion_hook_v4(job_id, session_path):
    return run_completion_hook(job_id, session_path)
