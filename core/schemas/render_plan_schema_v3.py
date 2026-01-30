from typing import Any, Dict


ALLOWED_SUBTITLE_FORMATS = {"ass", "srt"}


def _ensure_keys(obj: Dict[str, Any], required: set, name: str) -> None:
    missing = required - set(obj.keys())
    if missing:
        raise ValueError(f"{name} missing keys: {', '.join(sorted(missing))}")


def _ensure_no_extra(obj: Dict[str, Any], allowed: set, name: str) -> None:
    extra = set(obj.keys()) - allowed
    if extra:
        raise ValueError(f"{name} has unexpected keys: {', '.join(sorted(extra))}")


def validate_render_plan(plan: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(plan, dict):
        raise ValueError("render_plan must be a dict")

    top_required = {"job_id", "media", "style", "layout", "subtitles"}
    top_allowed = top_required
    _ensure_keys(plan, top_required, "render_plan")
    _ensure_no_extra(plan, top_allowed, "render_plan")

    job_id = plan["job_id"]
    if not isinstance(job_id, str) or not job_id:
        raise ValueError("render_plan.job_id must be non-empty str")

    media = plan["media"]
    if not isinstance(media, dict):
        raise ValueError("render_plan.media must be dict")
    media_required = {"path", "duration"}
    media_allowed = media_required
    _ensure_keys(media, media_required, "render_plan.media")
    _ensure_no_extra(media, media_allowed, "render_plan.media")
    if not isinstance(media["path"], str) or not media["path"]:
        raise ValueError("render_plan.media.path must be non-empty str")
    if not isinstance(media["duration"], (int, float)) or media["duration"] < 0:
        raise ValueError("render_plan.media.duration must be non-negative number")

    style = plan["style"]
    layout = plan["layout"]
    if not isinstance(style, str) or not style:
        raise ValueError("render_plan.style must be non-empty str")
    if not isinstance(layout, str) or not layout:
        raise ValueError("render_plan.layout must be non-empty str")

    subtitles = plan["subtitles"]
    if not isinstance(subtitles, dict):
        raise ValueError("render_plan.subtitles must be dict")
    subs_required = {"format", "path", "count"}
    subs_allowed = subs_required
    _ensure_keys(subtitles, subs_required, "render_plan.subtitles")
    _ensure_no_extra(subtitles, subs_allowed, "render_plan.subtitles")

    fmt = subtitles["format"]
    if not isinstance(fmt, str) or fmt not in ALLOWED_SUBTITLE_FORMATS:
        raise ValueError("render_plan.subtitles.format must be 'ass' or 'srt'")
    if not isinstance(subtitles["path"], str) or not subtitles["path"]:
        raise ValueError("render_plan.subtitles.path must be non-empty str")
    if not isinstance(subtitles["count"], int) or subtitles["count"] < 0:
        raise ValueError("render_plan.subtitles.count must be non-negative int")

    return {
        "job_id": job_id,
        "media": {
            "path": media["path"],
            "duration": float(media["duration"]),
        },
        "style": style,
        "layout": layout,
        "subtitles": {
            "format": fmt,
            "path": subtitles["path"],
            "count": int(subtitles["count"]),
        },
    }
