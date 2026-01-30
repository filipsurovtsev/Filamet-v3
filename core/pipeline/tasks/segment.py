import os
import json
import uuid
from typing import Any, Dict, List, Optional
from core.pipeline.tasks.base import BaseTask
from core.context.task_context import TaskContext


def _get_job_id(context: TaskContext) -> str:
    job = getattr(context, "job", None)
    if job is not None:
        return getattr(job, "id", None) or getattr(job, "job_id", "unknown_job")
    return getattr(context, "job_id", "unknown_job")


def _ensure_output_dir(job_id: str) -> str:
    base_dir = os.path.join("output", "segments", job_id)
    os.makedirs(base_dir, exist_ok=True)
    return base_dir


def _read_raw_transcript(job_id: str) -> str:
    path = os.path.join("output", "transcripts", job_id, "raw_transcript.txt")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"raw transcript missing: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _linear_segment_text(text: str) -> List[Dict[str, Any]]:
    blocks = []
    raw_blocks = text.split("\n\n")
    for idx, blk in enumerate(raw_blocks):
        t = blk.strip()
        if not t:
            continue
        blocks.append({
            "segment_id": str(uuid.uuid4()),
            "index": idx,
            "text": t
        })
    return blocks


class SimpleSegmentTask(BaseTask):
    task_type = "SEGMENT"

    def run(self, context: TaskContext, logger: Optional[Any] = None) -> Dict[str, Any]:
        job_id = _get_job_id(context)
        if logger and hasattr(logger, "info"):
            logger.info(f"SimpleSegmentTask: reading raw transcript for {job_id}")

        raw_text = _read_raw_transcript(job_id)
        segments = _linear_segment_text(raw_text)

        out_dir = _ensure_output_dir(job_id)
        out_path = os.path.join(out_dir, "segments.json")

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(segments, f, ensure_ascii=False, indent=2)

        job = getattr(context, "job", None)
        if job is not None:
            output = getattr(job, "output", None)
            if output is None:
                output = {}
                setattr(job, "output", output)
            seg_info = output.get("segments") or {}
            seg_info.update({
                "count": len(segments),
                "path": out_path,
                "method": "v0_linear"
            })
            output["segments"] = seg_info

        if logger and hasattr(logger, "info"):
            logger.info(f"SimpleSegmentTask: {len(segments)} segments saved to {out_path}")

        return {
            "status": "OK",
            "job_id": job_id,
            "segments_count": len(segments),
            "segments_path": out_path,
        }
