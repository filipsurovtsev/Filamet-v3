import os

from core.media.errors import (
    InvalidMediaPathError,
    InvalidMediaKindError,
    InvalidMediaSourceError,
    UnsafeMediaError,
)

ALLOWED_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".mkv",
    ".avi",
    ".mp3",
    ".wav",
    ".m4a",
}

ALLOWED_KINDS = {
    "video",
    "audio",
}

ALLOWED_SOURCES = {
    "local",
    "telegram",
    "upload",
    "youtube",
    "vk",
    "ok",
    "tiktok",
}


def ensure_safe_path(path):
    if path is None:
        return None
    if not isinstance(path, str):
        raise InvalidMediaPathError("path must be string or None")
    if path.startswith("/") or ".." in path.split("/"):
        raise InvalidMediaPathError("unsafe path form")
    _, ext = os.path.splitext(path)
    ext = ext.lower()
    if ext and ext not in ALLOWED_EXTENSIONS:
        raise InvalidMediaPathError("extension not allowed")
    return path


def validate_media_kind(kind):
    if kind is None:
        return None
    if kind not in ALLOWED_KINDS:
        raise InvalidMediaKindError("kind not allowed")
    return kind


def validate_media_source(source):
    if source is None:
        return None
    if source not in ALLOWED_SOURCES:
        raise InvalidMediaSourceError("source not allowed")
    return source


def ensure_media_safe(path=None, kind=None, source=None):
    try:
        safe_path = ensure_safe_path(path)
        safe_kind = validate_media_kind(kind)
        safe_source = validate_media_source(source)
    except (InvalidMediaPathError, InvalidMediaKindError, InvalidMediaSourceError) as e:
        raise UnsafeMediaError(str(e))
    return safe_path, safe_kind, safe_source
