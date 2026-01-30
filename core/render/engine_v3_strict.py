import json
import os
from datetime import datetime
from core.render.interface_v3 import RenderEngine

class StrictRenderEngine(RenderEngine):
    def __init__(self, job_id, plan_path, overlay_path, session_path):
        self.job_id = job_id
        self.plan_path = plan_path
        self.overlay_path = overlay_path
        self.session_path = session_path
        self.plan = None
        self.overlay = None
        self.session = None

    def load_plan(self):
        with open(self.plan_path, "r") as f:
            self.plan = json.load(f)

    def load_overlay(self):
        with open(self.overlay_path, "r") as f:
            self.overlay = json.load(f)

    def prepare_session(self):
        self.session = {
            "job_id": self.job_id,
            "plan_path": self.plan_path,
            "overlay_path": self.overlay_path,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "status": "prepared_strict"
        }
        os.makedirs(os.path.dirname(self.session_path), exist_ok=True)
        with open(self.session_path, "w") as f:
            json.dump(self.session, f, indent=2)

    def run(self):
        if not self.session:
            raise RuntimeError("Session not prepared")
        self.session["status"] = "pending_strict"
        with open(self.session_path, "w") as f:
            json.dump(self.session, f, indent=2)
        return {"status": "pending_strict", "job_id": self.job_id}
