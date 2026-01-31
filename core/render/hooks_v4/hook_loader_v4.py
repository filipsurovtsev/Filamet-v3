import json

from core.render.hooks_v4.completion_hook_v4 import render_completion_hook_v4

def call_completion_hook_v4(job_id, session_path):
    return render_completion_hook_v4(job_id, session_path)
