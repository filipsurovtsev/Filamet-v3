class MediaContext:
    def __init__(self, source=None, meta=None):
        self.source = source
        self.meta = meta or {}
    def get_source(self): return self.source
    def get_meta(self): return self.meta
    def set_meta(self, k, v): self.meta[k] = v
