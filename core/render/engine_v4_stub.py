import json
import os
from datetime import datetime

class RenderEngineV4Stub:
    def __init__(self, job_id, plan_path, overlay_path, session_path):
        self.job_id = job_id
        self.plan_path = plan_path
        self.overlay_path = overlay_path
        self.session_path = session_path

    def load_plan(self):
        with open(self.plan_path, "r") as f:
            self.plan = json.load(f)

    def load_overlay(self):
        with open(self.overlay_path, "r") as f:
            self.overlay = json.load(f)

    def prepare_session(self):
        os.makedirs(os.path.dirname(self.session_path), exist_ok=True)
        session = {
            "job_id": self.job_id,
            "plan": self.plan_path,
            "overlay": self.overlay_path,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "status": "v4_prepared"
        }
        with open(self.session_path, "w") as f:
            json.dump(session, f, indent=2)

    def run(self):
        with open(self.session_path, "r") as f:
            session = json.load(f)
        session["status"] = "v4_stub_running"
        with open(self.session_path, "w") as f:
            json.dump(session, f, indent=2)
        return session
