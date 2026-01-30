import os, json

class TimingTaskV3:
    def __init__(self, store):
        self.store = store

    def run(self, job_id, payload):
        job = self.store.load_job(job_id)
        caps = payload.get("mock_captions", [])
        duration = float(payload.get("mock_probe", 1.0))
        n = len(caps)
        if n == 0:
            return {"status": "failed", "error": "no captions"}
        step = duration / n
        pack = []
        for i, cap in enumerate(caps):
            start = i * step
            end = (i+1) * step
            pack.append({
                "index": i,
                "caption_id": cap["caption_id"],
                "time": {
                    "start": start,
                    "end": end,
                    "duration": end - start
                },
                "meta": {
                    "source_caption_id": cap["caption_id"]
                }
            })
        from core.pipeline.timing.timing_pack_schema_v3 import validate_timing_pack
        ok, err = validate_timing_pack(pack)
        if not ok:
            return {"status": "failed", "error": err}
        outdir = f"output/timings/{job_id}"
        os.makedirs(outdir, exist_ok=True)
        path = f"{outdir}/timings_v3.json"
        with open(path, "w") as f:
            json.dump(pack, f, indent=2)
        return {"status": "done", "job_id": job_id}
