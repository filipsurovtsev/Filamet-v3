import os
import json
import uuid

from core.pipeline.tasks.base import BaseTask
from core.schemas.captions_timings_v3 import validate_timings_schema
from core.context.task_context import TaskContext
from core.media.io.base_reader import media_probe, media_exists

def _job_id(ctx: TaskContext) -> str:
    job = getattr(ctx, "job", None)
    if job:
        return getattr(job, "id", None) or getattr(job, "job_id", "unknown_job")
    return getattr(ctx, "job_id", "unknown_job")

def _read_captions(job_id: str) -> list:
    path = os.path.join("output", "captions", job_id, "captions.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _ensure(job_id: str) -> str:
    d = os.path.join("output", "timings", job_id)
    os.makedirs(d, exist_ok=True)
    return d

class TimingTask(BaseTask):
    task_type = "TIMING"

    def fail_job(self, ctx: TaskContext, logger, reason: str):
        job = getattr(ctx, "job", None)
        if job:
            job.status = "FAILED"
            out = getattr(job, "output", None) or {}
            out["timing_error"] = reason
            job.output = out
        if logger and hasattr(logger, "error"):
            logger.error(f"TimingTask FAILED: {reason}")

    def run(self, context: TaskContext, logger=None):
        job_id = _job_id(context)

        job = getattr(context, "job", None)
        if not job:
            raise RuntimeError("TaskContext missing job")

        desc = getattr(context.media_context, "descriptor", None)
        if not desc:
            self.fail_job(context, logger, "media descriptor missing")
            raise RuntimeError("media descriptor missing")

        media_path = desc.path
        if not media_exists(media_path):
            self.fail_job(context, logger, "media not found")
            raise FileNotFoundError("media not found")

        probe = media_probe(media_path)
        media_dur = float(probe.get("duration", 0.0))
        if media_dur <= 0:
            self.fail_job(context, logger, "invalid media duration")
            raise RuntimeError("invalid media duration")

        try:
            caps = _read_captions(job_id)
        except Exception as exc:
            self.fail_job(context, logger, f"cannot read captions.json: {exc}")
            raise

        n = len(caps)
        if n == 0:
            self.fail_job(context, logger, "no captions found")
            raise RuntimeError("no captions")

        step = media_dur / n
        timings = []

        for i, cap in enumerate(caps):
            start = step * i
            end = step * (i + 1)
            duration = end - start

            timings.append({
                "caption_id": str(uuid.uuid4()),
                "index": i,
                "time": {
                    "start": start,
                    "end": end,
                    "duration": duration
                },
                "meta": {
                    "source_caption_id": cap["caption_id"]
                }
            })

        ok, msg = validate_timings_schema(timings)
        if not ok:
            self.fail_job(context, logger, f"timing schema failed: {msg}")
            raise RuntimeError(f"timing schema failed: {msg}")

        out_dir = _ensure(job_id)
        out_path = os.path.join(out_dir, "timings.json")
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(timings, f, ensure_ascii=False, indent=2)
        except Exception as exc:
            self.fail_job(context, logger, f"save failed: {exc}")
            raise

        out = getattr(job, "output", None) or {}
        out["timings"] = {
            "count": len(timings),
            "path": out_path,
            "method": "v0_uniform",
        }
        if "schemas" not in out:
            out["schemas"] = {}
        out["schemas"]["timings"] = "v3.locked"
        job.output = out

        return {
            "status": "OK",
            "job_id": job_id,
            "timings_count": len(timings),
            "timings_path": out_path,
        }
