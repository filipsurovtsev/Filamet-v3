from dataclasses import dataclass, field
from typing import Optional, Dict, Any

@dataclass
class MediaDescriptor:
    id: str
    path: str
    kind: str
    source: str
    duration: Optional[float] = None
    size: Optional[int] = None
    codec: Optional[str] = None
    streams: Optional[Dict[str, Any]] = None
    meta: Dict[str, Any] = field(default_factory=dict)
    safe: bool = False
    probed: bool = False

    def update_with_probe(self, probe_data: Dict[str, Any]) -> None:
        if not probe_data:
            return
        if "duration" in probe_data:
            self.duration = probe_data["duration"]
        if "size" in probe_data:
            self.size = probe_data["size"]
        if "codec" in probe_data:
            self.codec = probe_data["codec"]
        if "streams" in probe_data:
            self.streams = probe_data["streams"]
        extra = {k: v for k, v in probe_data.items() if k not in {"duration","size","codec","streams"}}
        if extra:
            self.meta.update(extra)
        self.probed = True
