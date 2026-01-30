import json
import os
from typing import Any, Dict, List

from core.schemas.srt_model_v3 import validate_srt_schema
from core.timecodes.timecode_v3 import timecode_to_srt

class SrtTaskError(Exception):
    pass

class SrtTask:
    def __init__(self, ctx: Any) -> None:
        self.ctx = ctx

    def _get_job_id(self) -> str:
        job = getattr(self.ctx, "job", None)
        if job is None:
            return "unknown_job"
        for k in ("id", "job_id", "uid"):
            if isinstance(job, dict) and k in job:
                return str(job[k])
            if hasattr(job, k):
                return str(getattr(job, k))
        return "unknown_job"

    def _get_output_root(self) -> str:
        if hasattr(self.ctx, "output_root"):
            return str(self.ctx.output_root)
        if hasattr(self.ctx, "paths") and hasattr(self.ctx.paths, "output_root"):
            return str(self.ctx.paths.output_root)
        return "output"

    def _load_json(self, path: str) -> Any:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_srt_file(self, srt_path: str, records: List[Dict[str, Any]]) -> None:
        os.makedirs(os.path.dirname(srt_path), exist_ok=True)
        with open(srt_path, "w", encoding="utf-8") as f:
            for i, rec in enumerate(records, start=1):
                f.write(f"{i}\n")
                f.write(f"{rec['start']} --> {rec['end']}\n")
                f.write(f"{rec['text']}\n\n")

    def run(self) -> None:
        job_id = self._get_job_id()
        output_root = self._get_output_root()

        captions_path = os.path.join(output_root, "captions", job_id, "captions.json")
        timings_path = os.path.join(output_root, "timings", job_id, "timings.json")
        srt_path = os.path.join(output_root, "subtitles", job_id, "subtitles.srt")

        captions = self._load_json(captions_path)
        timings = self._load_json(timings_path)

        if len(captions) != len(timings):
            raise SrtTaskError("length mismatch")

        records = []
        for idx, (cap, tim) in enumerate(zip(captions, timings)):
            tc = tim["time"]
            start_str, end_str = timecode_to_srt(tc)
            records.append({
                "index": idx,
                "start": start_str,
                "end": end_str,
                "text": cap["text"],
            })

        validate_srt_schema(records)
        self._save_srt_file(srt_path, records)

        job = getattr(self.ctx, "job", None)
        if isinstance(job, dict):
            out = job.setdefault("output", {})
            sub = out.setdefault("subtitles", {})
            sub.update({
                "path": srt_path,
                "method": "v0_srt",
                "count": len(records)
            })
            sch = out.setdefault("schemas", {})
            sch["srt"] = "v3.locked"
        elif job is not None and hasattr(job, "output"):
            if job.output is None:
                job.output = {}
            sub = job.output.setdefault("subtitles", {})
            sub.update({
                "path": srt_path,
                "method": "v0_srt",
                "count": len(records)
            })
            sch = job.output.setdefault("schemas", {})
            sch["srt"] = "v3.locked"
