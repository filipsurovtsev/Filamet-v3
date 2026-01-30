class MediaIOError(Exception):
    pass

class MediaFileNotFoundError(MediaIOError):
    pass

class MediaProbeError(MediaIOError):
    pass

class UnsafeMediaAccessError(MediaIOError):
    pass
