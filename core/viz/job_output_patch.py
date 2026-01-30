def apply_viz_defaults(job):
    if getattr(job, "output", None) is None:
        job.output = {}
    job.output["viz"] = {
        "style": "Default",
        "layout": "1080x1920",
        "schema": "v3.locked"
    }
