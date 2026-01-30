import os, json

class SrtTaskV3:
    def __init__(self, store):
        self.store = store

    def run(self, job_id, payload):
        timings = payload.get("timings", [])
        if not timings:
            return {"status": "failed", "error": "no timings"}

        records = []
        for i, t in enumerate(timings):
            start = t["time"]["start"]
            end = t["time"]["end"]
            text = t.get("text", f"caption-{i}")

            def fmt(x):
                h = int(x // 3600)
                m = int((x % 3600) // 60)
                s = int(x % 60)
                ms = int((x - int(x)) * 1000)
                return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

            records.append({
                "index": i,
                "start": fmt(start),
                "end": fmt(end),
                "text": text
            })

        from core.pipeline.srt.srt_schema_v3 import validate_srt_schema
        validate_srt_schema(records)

        outdir = f"output/subtitles/{job_id}"
        os.makedirs(outdir, exist_ok=True)
        path = f"{outdir}/subtitles_v3.srt"

        with open(path, "w") as f:
            for rec in records:
                f.write(f"{rec['index']+1}\n")
                f.write(f"{rec['start']} --> {rec['end']}\n")
                f.write(f"{rec['text']}\n\n")

        return {"status": "done", "job_id": job_id, "path": path}
