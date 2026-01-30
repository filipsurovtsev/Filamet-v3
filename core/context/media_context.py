from core.media.factory import build_media_descriptor

class MediaContext:
    def __init__(self, descriptor_data=None):
        self.descriptor = None
        if descriptor_data:
            self.descriptor = build_media_descriptor(descriptor_data)

    def set_descriptor(self, data):
        self.descriptor = build_media_descriptor(data)

    def get_descriptor(self):
        return self.descriptor
