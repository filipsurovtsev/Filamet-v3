import os
import json
from core.subtitles.ass_model_v3 import validate_ass_schema
from core.timecodes.timecode_v3 import timecode_to_ass

try:
    from core.pipeline.tasks.base import BaseTask
except ImportError:
    BaseTask = object

class AssTaskV0(BaseTask):
    task_type = "ASS"

    def __init__(self, context=None, job=None):
        self.context = context
        self.job = job

    def run(self):
        job = self.job
        job_id = str(getattr(job, "id", getattr(job, "job_id", "unknown")))
        captions_path = os.path.join("output", "captions", job_id, "captions.json")
        timings_path = os.path.join("output", "timings", job_id, "timings.json")
        subtitles_dir = os.path.join("output", "subtitles", job_id)
        os.makedirs(subtitles_dir, exist_ok=True)
        with open(captions_path, "r", encoding="utf-8") as f:
            captions = json.load(f)
        with open(timings_path, "r", encoding="utf-8") as f:
            timings = json.load(f)
        records = []
        for i, caption in enumerate(captions):
            timing = timings[i]
            start_str, end_str = timecode_to_ass(timing["time"])
            records.append(
                {
                    "index": i,
                    "start": start_str,
                    "end": end_str,
                    "text": caption["text"],
                }
            )
        validate_ass_schema(records)
        lines = []
        lines.append("[Script Info]")
        lines.append("ScriptType: v4.00+")
        lines.append("PlayResX: 1920")
        lines.append("PlayResY: 1080")
        lines.append("")
        lines.append("[V4+ Styles]")
        lines.append("Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding")
        lines.append("Style: Default,Arial,60,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,2,0,2,50,50,50,0")
        lines.append("")
        lines.append("[Events]")
        lines.append("Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text")
        for rec in records:
            line = f"Dialogue: 0,{rec['start']},{rec['end']},Default,,0,0,0,,{rec['text']}"
            lines.append(line)
        ass_path = os.path.join(subtitles_dir, "subtitles.ass")
        with open(ass_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        output = getattr(job, "output", None)
        if isinstance(output, dict):
            output.setdefault("subtitles_ass", {})
            output["subtitles_ass"].update(
                {
                    "path": ass_path,
                    "method": "v0_ass",
                    "count": len(records),
                }
            )
            output.setdefault("schemas", {})
            output["schemas"]["ass"] = "v3.locked"
        return job
