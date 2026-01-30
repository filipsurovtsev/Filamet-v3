from core.media.descriptors import MediaDescriptor

def build_media_descriptor(data):
    return MediaDescriptor(
        media_id=data.get("media_id"),
        path=data.get("path"),
        kind=data.get("kind"),
        source=data.get("source"),
        duration=data.get("duration"),
        fps=data.get("fps"),
        codec=data.get("codec"),
        meta=data.get("meta", {})
    )
