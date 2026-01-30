import os
import json
import uuid
from core.pipeline.caption.caption_schema_v3 import validate_captions_schema

class CaptionTaskV3:
    def run(self, job_id, job, store):
        segs = job["payload"].get("segments", [])
        caps = []

        for idx, seg in enumerate(segs):
            t = seg["text"]
            caps.append({
                "id": str(uuid.uuid4()),
                "index": idx,
                "text": t,
                "meta": {
                    "length": len(t),
                    "source_segment_id": seg["id"]
                }
            })

        validate_captions_schema(caps)

        outdir = f"output/captions/{job_id}"
        os.makedirs(outdir, exist_ok=True)
        outfile = f"{outdir}/captions.json"

        with open(outfile, "w") as f:
            json.dump(caps, f, indent=2)

        store.update_job(job_id, {
            "output": {
                **job.get("output", {}),
                "captions": {
                    "path": outfile,
                    "count": len(caps),
                    "schema": "v3.locked",
                    "method": "v3_caption"
                }
            }
        })

        return {"job_id": job_id, "status": "done"}
