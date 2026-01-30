import os, json

class AssTaskV3:
    def __init__(self, store):
        self.store = store

    def _fmt_ass(self, x):
        h = int(x // 3600)
        m = int((x % 3600) // 60)
        s = int(x % 60)
        cs = int((x - int(x)) * 100)  # centiseconds
        return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"

    def run(self, job_id, payload):
        timings = payload.get("timings", [])
        if not timings:
            return {"status": "failed", "error": "no timings"}

        records = []
        for i, t in enumerate(timings):
            start = self._fmt_ass(t["time"]["start"])
            end = self._fmt_ass(t["time"]["end"])
            text = t.get("text", f"caption-{i}")

            records.append({
                "index": i,
                "start": start,
                "end": end,
                "text": text
            })

        from core.pipeline.ass.ass_schema_v3 import validate_ass_schema
        validate_ass_schema(records)

        outdir = f"output/subtitles/{job_id}"
        os.makedirs(outdir, exist_ok=True)
        path = f"{outdir}/subtitles_v3.ass"

        with open(path, "w") as f:
            f.write("[Script Info]\n")
            f.write("ScriptType: v4.00+\n")
            f.write("PlayResX: 1080\n")
            f.write("PlayResY: 1920\n\n")

            f.write("[V4+ Styles]\n")
            f.write("Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, "
                    "OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, "
                    "ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
                    "Alignment, MarginL, MarginR, MarginV, Encoding\n")
            f.write("Style: Default,Arial,60,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,"
                    "0,0,0,0,100,100,0,0,1,2,0,2,50,50,50,0\n\n")

            f.write("[Events]\n")
            f.write("Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")

            for rec in records:
                f.write(f"Dialogue: 0,{rec['start']},{rec['end']},Default,,0,0,0,,{rec['text']}\n")

        return {"status": "done", "job_id": job_id, "path": path}
