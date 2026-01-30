from typing import Any, Dict

DEFAULT_RENDER_PROFILE: Dict[str, Any] = {
    "resolution": "1080x1920",
    "fps": 30,
    "codec": "h264",
    "bitrate": "8M",
}


def validate_render_profile(profile: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(profile, dict):
        raise ValueError("render_profile must be dict")
    required = {"resolution", "fps", "codec", "bitrate"}
    allowed = required
    missing = required - set(profile.keys())
    if missing:
        raise ValueError(f"render_profile missing keys: {', '.join(sorted(missing))}")
    extra = set(profile.keys()) - allowed
    if extra:
        raise ValueError(f"render_profile has unexpected keys: {', '.join(sorted(extra))}")

    resolution = profile["resolution"]
    fps = profile["fps"]
    codec = profile["codec"]
    bitrate = profile["bitrate"]

    if not isinstance(resolution, str) or "x" not in resolution:
        raise ValueError("render_profile.resolution must be 'WxH' string")
    if not isinstance(fps, int) or fps <= 0:
        raise ValueError("render_profile.fps must be positive int")
    if not isinstance(codec, str) or not codec:
        raise ValueError("render_profile.codec must be non-empty str")
    if not isinstance(bitrate, str) or not bitrate:
        raise ValueError("render_profile.bitrate must be non-empty str")

    return {
        "resolution": resolution,
        "fps": int(fps),
        "codec": codec,
        "bitrate": bitrate,
    }
