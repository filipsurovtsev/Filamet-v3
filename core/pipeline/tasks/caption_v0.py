import os
import json
import uuid
from typing import Any, Dict, List, Optional
from core.pipeline.tasks.base import BaseTask
from core.context.task_context import TaskContext

from core.schemas.captions_v3 import validate_captions_schema


def _get_job_id(context: TaskContext) -> str:
    job = getattr(context, "job", None)
    if job is not None:
        return getattr(job, "id", None) or getattr(job, "job_id", "unknown_job")
    return getattr(context, "job_id", "unknown_job")


def _read_segments(job_id: str) -> list:
    path = os.path.join("output", "segments", job_id, "segments.json")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"segments.json missing: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _ensure_output_dir(job_id: str) -> str:
    base_dir = os.path.join("output", "captions", job_id)
    os.makedirs(base_dir, exist_ok=True)
    return base_dir


def _build_captions(segments: list[dict]) -> list[dict]:
    out = []
    for idx, seg in enumerate(segments):
        text = seg["text"]
        out.append({
            "caption_id": str(uuid.uuid4()),
            "index": idx,
            "text": text,
            "meta": {
                "length": len(text),
                "source_segment_id": seg["segment_id"]
            }
        })
    return out


class PureCaptionTask(BaseTask):
    task_type = "CAPTION"

    def fail_job(self, context: TaskContext, logger, reason: str):
        job = getattr(context, "job", None)
        if job is not None:
            job.status = "FAILED"
            if getattr(job, "output", None) is None:
                job.output = {}
            job.output["captions_error"] = reason
        if logger and hasattr(logger, "error"):
            logger.error(f"PureCaptionTask FAILED: {reason}")

    def run(self, context: TaskContext, logger: Optional[Any] = None):
        job_id = _get_job_id(context)

        try:
            segments = _read_segments(job_id)
        except Exception as exc:
            self.fail_job(context, logger, f"cannot read segments.json: {exc}")
            raise

        captions = _build_captions(segments)

        valid, msg = validate_captions_schema(captions)
        if not valid:
            self.fail_job(context, logger, f"caption schema failed: {msg}")
            raise RuntimeError(f"caption schema failed: {msg}")

        out_dir = _ensure_output_dir(job_id)
        out_path = os.path.join(out_dir, "captions.json")

        try:
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(captions, f, ensure_ascii=False, indent=2)
        except Exception as exc:
            self.fail_job(context, logger, f"save failed: {exc}")
            raise

        job = getattr(context, "job", None)
        if job is not None:
            output = getattr(job, "output", None)
            if output is None:
                output = {}
                setattr(job, "output", output)

            cap_info = output.get("captions") or {}
            cap_info.update({
                "count": len(captions),
                "path": out_path,
                "method": "v0_pure_text",
            })
            output["captions"] = cap_info

            if "schemas" not in output:
                output["schemas"] = {}
            output["schemas"]["captions"] = "v3.locked"

        return {
            "status": "OK",
            "job_id": job_id,
            "captions_count": len(captions),
            "captions_path": out_path,
        }
