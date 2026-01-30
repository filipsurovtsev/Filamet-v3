class MediaDescriptor:
    def __init__(self, *, media_id=None, path=None, kind=None, source=None,
                 duration=None, fps=None, codec=None, meta=None, safe=False):
        self.media_id = media_id
        self.path = path
        self.kind = kind
        self.source = source
        self.duration = duration
        self.fps = fps
        self.codec = codec
        self.meta = meta or {}
        self.safe = bool(safe)

    def to_dict(self):
        return {
            "media_id": self.media_id,
            "path": self.path,
            "kind": self.kind,
            "source": self.source,
            "duration": self.duration,
            "fps": self.fps,
            "codec": self.codec,
            "meta": self.meta,
            "safe": self.safe,
        }
