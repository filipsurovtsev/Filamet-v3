import os
import json
import uuid
from core.pipeline.segment.segment_schema_v3 import validate_segments_schema

class SegmentTaskV3:
    def run(self, job_id, job, store):
        raw = job["payload"].get("text", "")
        blocks = [b.strip() for b in raw.split("\n\n") if b.strip()]

        segs = []
        for idx, b in enumerate(blocks):
            segs.append({
                "id": str(uuid.uuid4()),
                "index": idx,
                "text": b,
                "meta": {"length": len(b)}
            })

        validate_segments_schema(segs)

        outdir = f"output/segments/{job_id}"
        os.makedirs(outdir, exist_ok=True)
        outfile = f"{outdir}/segments.json"

        with open(outfile, "w") as f:
            json.dump(segs, f, indent=2)

        store.update_job(job_id, {
            "output": {
                **job.get("output", {}),
                "segments": {
                    "path": outfile,
                    "count": len(segs),
                    "schema": "v3.locked",
                    "method": "v3_segment"
                }
            }
        })

        return {"job_id": job_id, "status": "done"}
