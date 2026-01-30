from core.media.factory import build_media_descriptor
from core.media.errors import UnsafeMediaError


class MediaContext:
    def __init__(self, descriptor_data=None):
        self.descriptor = None
        self.safe = False
        if descriptor_data:
            self.set_descriptor(descriptor_data)

    def set_descriptor(self, data):
        try:
            self.descriptor = build_media_descriptor(data)
            self.safe = self.descriptor.safe if self.descriptor else False
        except UnsafeMediaError:
            self.descriptor = None
            self.safe = False

    def get_descriptor(self):
        return self.descriptor

    def is_safe(self):
        return bool(self.safe)
