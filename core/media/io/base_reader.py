import os
from typing import Dict, Any
from .errors import MediaFileNotFoundError, MediaProbeError, UnsafeMediaAccessError

def media_exists(path: str) -> bool:
    if not path:
        return False
    return os.path.isfile(path)

def media_probe(path: str) -> Dict[str, Any]:
    if not media_exists(path):
        raise MediaFileNotFoundError(f"Media not found: {path}")
    try:
        stat = os.stat(path)
    except OSError as exc:
        raise MediaProbeError(f"Failed to probe media: {path}") from exc
    return {
        "path": path,
        "size": stat.st_size,
        "duration": None,
        "codec": None,
        "streams": None,
    }
