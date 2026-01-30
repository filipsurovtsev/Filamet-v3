import os
import json
from core.render.engine_v3_strict import StrictRenderEngine

def main():
    job_id = "render_demo_v3_strict"
    base = f"output/render/{job_id}"
    os.makedirs(base, exist_ok=True)

    plan_path = os.path.join(base, "render_plan_demo.json")
    overlay_path = os.path.join(base, "overlay_plan_demo.json")
    session_path = os.path.join(base, "render_session_demo.json")

    plan = {
        "job_id": job_id,
        "media": {"path": "tests/smoke/demo.mp4", "duration": 12.0},
        "style": "Default",
        "layout": "1080x1920",
        "subtitles": {
            "format": "ass",
            "path": "output/subtitles/demo/subtitles.ass",
            "count": 3
        }
    }
    overlay = {
        "resolution": "1080x1920",
        "safe_zone": {"left": 50, "right": 50, "top": 100, "bottom": 200},
        "events": [
            {"index": 0, "start": 0.0, "end": 4.0, "style": "Default", "text": "one"},
            {"index": 1, "start": 4.0, "end": 8.0, "style": "Default", "text": "two"},
            {"index": 2, "start": 8.0, "end": 12.0, "style": "Default", "text": "three"},
        ]
    }

    with open(plan_path, "w") as f:
        json.dump(plan, f, indent=2)
    with open(overlay_path, "w") as f:
        json.dump(overlay, f, indent=2)

    engine = StrictRenderEngine(job_id, plan_path, overlay_path, session_path)
    engine.load_plan()
    engine.load_overlay()
    engine.prepare_session()
    res = engine.run()

    print("RENDERENGINE_V3_STRICT_SMOKE_OK", res)

if __name__ == "__main__":
    main()
