from typing import Any, Dict, List


def _ensure_keys(obj: Dict[str, Any], required: set, name: str) -> None:
    missing = required - set(obj.keys())
    if missing:
        raise ValueError(f"{name} missing keys: {', '.join(sorted(missing))}")


def _ensure_no_extra(obj: Dict[str, Any], allowed: set, name: str) -> None:
    extra = set(obj.keys()) - allowed
    if extra:
        raise ValueError(f"{name} has unexpected keys: {', '.join(sorted(extra))}")


def validate_overlay_plan(plan: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(plan, dict):
        raise ValueError("overlay_plan must be dict")

    top_required = {"resolution", "safe_zone", "events"}
    top_allowed = top_required
    _ensure_keys(plan, top_required, "overlay_plan")
    _ensure_no_extra(plan, top_allowed, "overlay_plan")

    resolution = plan["resolution"]
    if not isinstance(resolution, str) or "x" not in resolution:
        raise ValueError("overlay_plan.resolution must be 'WxH' string")

    safe_zone = plan["safe_zone"]
    if not isinstance(safe_zone, dict):
        raise ValueError("overlay_plan.safe_zone must be dict")
    sz_required = {"left", "right", "top", "bottom"}
    sz_allowed = sz_required
    _ensure_keys(safe_zone, sz_required, "overlay_plan.safe_zone")
    _ensure_no_extra(safe_zone, sz_allowed, "overlay_plan.safe_zone")
    for k in sz_required:
        if not isinstance(safe_zone[k], int) or safe_zone[k] < 0:
            raise ValueError(f"overlay_plan.safe_zone.{k} must be non-negative int")

    events = plan["events"]
    if not isinstance(events, list):
        raise ValueError("overlay_plan.events must be list")
    validated_events: List[Dict[str, Any]] = []
    for ev in events:
        if not isinstance(ev, dict):
            raise ValueError("overlay_plan.events item must be dict")
        ev_required = {"index", "start", "end", "style", "text"}
        ev_allowed = ev_required
        _ensure_keys(ev, ev_required, "overlay_plan.event")
        _ensure_no_extra(ev, ev_allowed, "overlay_plan.event")

        index = ev["index"]
        start = ev["start"]
        end = ev["end"]
        style = ev["style"]
        text = ev["text"]

        if not isinstance(index, int) or index < 0:
            raise ValueError("overlay_plan.event.index must be non-negative int")
        if not isinstance(start, (int, float)) or start < 0:
            raise ValueError("overlay_plan.event.start must be non-negative number")
        if not isinstance(end, (int, float)) or end < start:
            raise ValueError("overlay_plan.event.end must be >= start")
        if not isinstance(style, str) or not style:
            raise ValueError("overlay_plan.event.style must be non-empty str")
        if not isinstance(text, str):
            raise ValueError("overlay_plan.event.text must be str")

        validated_events.append(
            {
                "index": index,
                "start": float(start),
                "end": float(end),
                "style": style,
                "text": text,
            }
        )

    return {
        "resolution": resolution,
        "safe_zone": {
            "left": int(safe_zone["left"]),
            "right": int(safe_zone["right"]),
            "top": int(safe_zone["top"]),
            "bottom": int(safe_zone["bottom"]),
        },
        "events": validated_events,
    }
