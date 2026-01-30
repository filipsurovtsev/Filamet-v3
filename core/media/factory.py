from core.media.descriptors import MediaDescriptor
from core.media.safety import ensure_media_safe
from core.media.errors import UnsafeMediaError


def build_media_descriptor(data):
    if data is None:
        return None
    if not isinstance(data, dict):
        raise UnsafeMediaError("media descriptor data must be dict or None")
    path = data.get("path")
    kind = data.get("kind")
    source = data.get("source")
    safe_path, safe_kind, safe_source = ensure_media_safe(
        path=path,
        kind=kind,
        source=source,
    )
    return MediaDescriptor(
        media_id=data.get("media_id"),
        path=safe_path,
        kind=safe_kind,
        source=safe_source,
        duration=data.get("duration"),
        fps=data.get("fps"),
        codec=data.get("codec"),
        meta=data.get("meta", {}),
        safe=True,
    )
