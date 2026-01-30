import json
import os
from typing import Any, Dict, List, Optional

from core.pipeline.tasks.base import BaseTask
from core.schemas.render_plan_schema_v3 import validate_render_plan
from core.schemas.overlay_plan_v3 import validate_overlay_plan
from core.schemas.render_profile_v3 import DEFAULT_RENDER_PROFILE, validate_render_profile
from core.media.io.base_reader import media_exists, media_probe
from core.viz.context import VizContext


class RenderPrepTask(BaseTask):
    task_type = "RENDER_PREP"

    def _get_job_id(self, job: Any) -> str:
        if hasattr(job, "id"):
            return str(job.id)
        if isinstance(job, dict) and "id" in job:
            return str(job["id"])
        raise ValueError("Job must have id")

    def _get_job_output(self, job: Any) -> Dict[str, Any]:
        if hasattr(job, "output"):
            if getattr(job, "output") is None:
                setattr(job, "output", {})
            return getattr(job, "output")
        if isinstance(job, dict):
            job.setdefault("output", {})
            return job["output"]
        raise ValueError("Job must support output dict")

    def _set_job_output(self, job: Any, output: Dict[str, Any]) -> None:
        if hasattr(job, "output"):
            setattr(job, "output", output)
        elif isinstance(job, dict):
            job["output"] = output

    def _get_media_path(self, media_ctx: Any) -> str:
        descriptor = None
        if hasattr(media_ctx, "descriptor"):
            descriptor = media_ctx.descriptor
        elif isinstance(media_ctx, dict):
            descriptor = media_ctx.get("descriptor")
        if descriptor is None:
            raise ValueError("MediaContext has no descriptor")
        if hasattr(descriptor, "path"):
            return str(descriptor.path)
        if isinstance(descriptor, dict) and "path" in descriptor:
            return str(descriptor["path"])
        raise ValueError("MediaDescriptor has no path")

    def _update_descriptor_probe(self, media_ctx: Any, probe: Dict[str, Any]) -> None:
        descriptor = None
        if hasattr(media_ctx, "descriptor"):
            descriptor = media_ctx.descriptor
        elif isinstance(media_ctx, dict):
            descriptor = media_ctx.get("descriptor")
        if descriptor is not None and hasattr(descriptor, "update_with_probe"):
            descriptor.update_with_probe(probe)

    def _get_viz_style_layout(self, viz_ctx: Optional[VizContext]) -> Dict[str, str]:
        style = "Default"
        layout = "1080x1920"
        if viz_ctx is None:
            return {"style": style, "layout": layout}
        if hasattr(viz_ctx, "current_style_name") and viz_ctx.current_style_name:
            style = viz_ctx.current_style_name
        if hasattr(viz_ctx, "layout_name") and viz_ctx.layout_name:
            layout = viz_ctx.layout_name
        if isinstance(viz_ctx, dict):
            style = viz_ctx.get("style", style)
            layout = viz_ctx.get("layout", layout)
        return {"style": style, "layout": layout}

    def _get_subtitles_info(self, output: Dict[str, Any]) -> Dict[str, Any]:
        subs = output.get("subtitles_ass") or output.get("subtitles")
        if not subs:
            raise ValueError("Subtitles info is missing for render preparation")
        if not isinstance(subs, dict):
            raise ValueError("Subtitles info must be dict")
        return subs

    def _load_json_file(self, path: str) -> Any:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _build_overlay_events(
        self,
        style_name: str,
        timings_path: Optional[str],
        captions_path: Optional[str],
    ) -> List[Dict[str, Any]]:
        if not timings_path or not captions_path:
            return []
        if not os.path.exists(timings_path) or not os.path.exists(captions_path):
            return []
        timings = self._load_json_file(timings_path)
        captions = self._load_json_file(captions_path)
        events: List[Dict[str, Any]] = []
        for t, c in zip(timings, captions):
            index = int(t.get("index", 0))
            time_data = t.get("time", {}) or {}
            start = float(time_data.get("start", 0.0))
            end = float(time_data.get("end", start))
            text = c.get("text", "")
            events.append(
                {
                    "index": index,
                    "start": start,
                    "end": end,
                    "style": style_name,
                    "text": text,
                }
            )
        return events

    def run(self, context: Any) -> Dict[str, Any]:
        job = context.job
        job_id = self._get_job_id(job)
        output = self._get_job_output(job)

        media_ctx = context.media
        viz_ctx = getattr(context, "viz", None)

        media_path = self._get_media_path(media_ctx)
        if not media_exists(media_path):
            raise RuntimeError(f"Media not found for render prep: {media_path}")

        probe = media_probe(media_path)
        duration = float(probe.get("duration", 0.0))
        self._update_descriptor_probe(media_ctx, probe)

        viz = self._get_viz_style_layout(viz_ctx)
        style_name = viz["style"]
        layout_name = viz["layout"]

        subtitles_info = self._get_subtitles_info(output)
        subs_format = subtitles_info.get("format")
        if not subs_format:
            path = subtitles_info.get("path", "")
            if path.endswith(".ass"):
                subs_format = "ass"
            else:
                subs_format = "srt"

        render_plan = {
            "job_id": job_id,
            "media": {"path": media_path, "duration": duration},
            "style": style_name,
            "layout": layout_name,
            "subtitles": {
                "format": subs_format,
                "path": subtitles_info.get("path"),
                "count": int(subtitles_info.get("count", 0)),
            },
        }
        render_plan = validate_render_plan(render_plan)

        render_profile = validate_render_profile(dict(DEFAULT_RENDER_PROFILE))

        timings_info = output.get("timings", {}) or {}
        captions_info = output.get("captions", {}) or {}
        timings_path = timings_info.get("path")
        captions_path = captions_info.get("path")
        events = self._build_overlay_events(style_name, timings_path, captions_path)

        overlay_plan = {
            "resolution": render_profile["resolution"],
            "safe_zone": {"left": 0, "right": 0, "top": 0, "bottom": 0},
            "events": events,
        }
        overlay_plan = validate_overlay_plan(overlay_plan)

        base_dir = os.path.join("output", "render", str(job_id))
        os.makedirs(base_dir, exist_ok=True)
        render_plan_path = os.path.join(base_dir, "render_plan.json")
        overlay_plan_path = os.path.join(base_dir, "overlay_plan.json")

        with open(render_plan_path, "w", encoding="utf-8") as f:
            json.dump(render_plan, f, ensure_ascii=False, indent=2)
        with open(overlay_plan_path, "w", encoding="utf-8") as f:
            json.dump(overlay_plan, f, ensure_ascii=False, indent=2)

        render_output = output.get("render") or {}
        render_output.update(
            {
                "plan_path": render_plan_path,
                "overlay_path": overlay_plan_path,
                "schema": "v3.locked",
                "profile": render_profile,
            }
        )
        output["render"] = render_output
        self._set_job_output(job, output)

        return {
            "render_plan_path": render_plan_path,
            "overlay_plan_path": overlay_plan_path,
        }
