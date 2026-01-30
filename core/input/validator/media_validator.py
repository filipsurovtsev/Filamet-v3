from core.input.schemas.media_schema import MEDIA_SCHEMA

def validate_media_block(media):
    if media is None:
        return True
    if not isinstance(media, dict):
        return False
    for key, allowed in MEDIA_SCHEMA.items():
        if key in media and not isinstance(media[key], allowed):
            return False
    return True
