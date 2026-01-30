import json
import os
import subprocess
from core.render.interface_v3 import RenderEngine

class FFMpegRenderEngineV4(RenderEngine):
    def __init__(self, job_id, plan_path, overlay_path, output_path, profile=None):
        self.job_id = job_id
        self.plan_path = plan_path
        self.overlay_path = overlay_path
        self.output_path = output_path
        self.profile = profile or {
            "resolution": "1080x1920",
            "fps": 30,
            "codec": "h264",
            "bitrate": "8M"
        }
        self.plan = None
        self.overlay = None

    def load_plan(self):
        with open(self.plan_path, "r") as f:
            self.plan = json.load(f)

    def load_overlay(self):
        if os.path.exists(self.overlay_path):
            with open(self.overlay_path, "r") as f:
                self.overlay = json.load(f)
        else:
            self.overlay = None

    def prepare_session(self):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

    def run(self):
        if not self.plan:
            raise RuntimeError("plan not loaded")

        media = self.plan.get("media", {})
        input_path = media.get("path")
        if not input_path:
            raise RuntimeError("media.path missing in render_plan")

        resolution = self.profile.get("resolution", "1080x1920")
        try:
            width_str, height_str = resolution.lower().split("x")
            width = int(width_str)
            height = int(height_str)
        except Exception as e:
            raise RuntimeError(f"invalid resolution: {resolution}") from e

        fps = int(self.profile.get("fps", 30))
        codec = self.profile.get("codec", "h264")
        bitrate = self.profile.get("bitrate", "8M")

        vf_chain = []
        subtitles_cfg = self.plan.get("subtitles") or {}
        subs_path = subtitles_cfg.get("path")
        if subs_path:
            vf_chain.append(f"subtitles={subs_path}")
        vf_chain.append(f"scale={width}:{height}")
        vf = ",".join(vf_chain)

        cmd = [
            "ffmpeg",
            "-y",
            "-i", input_path,
            "-vf", vf,
            "-r", str(fps),
            "-c:v", codec,
            "-b:v", bitrate,
            "-c:a", "copy",
            self.output_path,
        ]

        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if result.returncode != 0:
            return {
                "status": "failed",
                "job_id": self.job_id,
                "code": result.returncode,
                "stderr": result.stderr[-1000:],
            }

        return {
            "status": "ok",
            "job_id": self.job_id,
            "output": self.output_path,
        }
