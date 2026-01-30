import os
import json
from core.media.probe_mocker_v3 import probe_media
from core.media.probe_schema_v3 import validate_probe_schema

class ProbeTaskV0:
    def run(self, job_id, job, store):
        path = job["payload"].get("input")
        result = probe_media(path)
        validate_probe_schema(result)

        outdir = f"output/media/{job_id}"
        os.makedirs(outdir, exist_ok=True)
        outfile = f"{outdir}/probe.json"

        with open(outfile, "w") as f:
            json.dump(result, f, indent=2)

        store.update_job(job_id, {
            "output": {
                **job.get("output", {}),
                "probe": {
                    "path": outfile,
                    "schema": "v3.locked"
                }
            }
        })

        return {"job_id": job_id, "status": "done"}
