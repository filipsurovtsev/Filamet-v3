from typing import Optional
from core.media.descriptor import MediaDescriptor
from core.media.io.base_reader import media_exists, media_probe
from core.media.io.errors import MediaFileNotFoundError, MediaProbeError, UnsafeMediaAccessError

class MediaContext:
    def __init__(self, descriptor: MediaDescriptor):
        self.descriptor = descriptor
        self._safe_described: bool = bool(getattr(descriptor, "safe", False))
        self.probe_error: Optional[str] = None

    def is_safe(self) -> bool:
        return bool(self._safe_described and getattr(self.descriptor, "safe", False))

    def mark_unsafe(self, reason: str) -> None:
        self._safe_described = False
        self.probe_error = reason

    def probe_media(self, logger=None) -> bool:
        if not self.is_safe():
            self.mark_unsafe("unsafe_descriptor")
            if logger and hasattr(logger, "warning"):
                logger.warning("MediaContext: unsafe descriptor, probe blocked")
            return False
        try:
            if not media_exists(self.descriptor.path):
                raise MediaFileNotFoundError(self.descriptor.path)
            probe_data = media_probe(self.descriptor.path)
            self.descriptor.update_with_probe(probe_data)
            return True
        except (MediaFileNotFoundError, MediaProbeError) as exc:
            self.probe_error = str(exc)
            if logger and hasattr(logger, "error"):
                logger.error(f"MediaContext: media probe failed: {exc}")
            return False
        except UnsafeMediaAccessError as exc:
            self.mark_unsafe(str(exc))
            if logger and hasattr(logger, "error"):
                logger.error(f"MediaContext: unsafe media access: {exc}")
            return False
