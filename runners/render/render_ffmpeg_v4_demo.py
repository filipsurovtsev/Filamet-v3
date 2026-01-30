import os
import json
from core.render.ffmpeg_engine_v4 import FFMpegRenderEngineV4

def main():
    job_id = "render_v4_demo"
    base = f"output/render/{job_id}"
    os.makedirs(base, exist_ok=True)

    media_path = "tests/smoke/demo.mp4"

    plan_path = os.path.join(base, "render_plan_v4_demo.json")
    overlay_path = os.path.join(base, "overlay_plan_v4_demo.json")
    output_path = os.path.join(base, "render_v4_demo.mp4")

    plan = {
        "job_id": job_id,
        "media": {
            "path": media_path,
            "duration": 12.0
        },
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

    engine = FFMpegRenderEngineV4(
        job_id=job_id,
        plan_path=plan_path,
        overlay_path=overlay_path,
        output_path=output_path,
    )

    engine.load_plan()
    engine.load_overlay()
    engine.prepare_session()
    res = engine.run()

    print("FFMPEG_V4_RENDER_SMOKE_OK", res)

if __name__ == "__main__":
    main()
