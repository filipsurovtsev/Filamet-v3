import json
import os
from core.render.render_session_v3 import make_render_session, validate_render_session
from core.pipeline.tasks.render_prep_v0 import validate_render_plan_file, validate_overlay_plan_file

class RenderTaskV0:
    def __init__(self, job):
        self.job = job
        self.job_id = job.job_id

    def run(self):
        rp = os.path.join("output","render",self.job_id,"render_plan.json")
        op = os.path.join("output","render",self.job_id,"overlay_plan.json")

        validate_render_plan_file(rp)
        validate_overlay_plan_file(op)

        session = make_render_session(self.job_id, rp, op)
        validate_render_session(session)

        out_dir = os.path.join("output","render",self.job_id)
        os.makedirs(out_dir, exist_ok=True)

        session_path = os.path.join(out_dir,"render_session.json")
        with open(session_path,"w",encoding="utf-8") as f:
            json.dump(session,f,indent=2)

        if getattr(self.job,"output",None) is None:
            self.job.output = {}

        self.job.output["render"] = {
            "session": "prepared",
            "plan": rp,
            "overlay": op,
            "method": "v0_renderer_interface",
            "schema": "v3.locked"
        }
        return session_path
