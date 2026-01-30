from core.input.schemas.media_schema import MEDIA_SCHEMA
from core.media.safety import ensure_media_safe
from core.media.errors import UnsafeMediaError, InvalidMediaPathError, InvalidMediaKindError, InvalidMediaSourceError


def validate_media_block(media):
    if media is None:
        return True
    if not isinstance(media, dict):
        return False
    for key, allowed in MEDIA_SCHEMA.items():
        if key in media and not isinstance(media[key], allowed):
            return False
    try:
        ensure_media_safe(
            path=media.get("path"),
            kind=media.get("kind"),
            source=media.get("source"),
        )
    except (UnsafeMediaError, InvalidMediaPathError, InvalidMediaKindError, InvalidMediaSourceError):
        return False
    return True
