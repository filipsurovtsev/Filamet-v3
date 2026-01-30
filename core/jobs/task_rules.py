from typing import Dict, Any
from . import task_types as tt

TASK_RULES: Dict[str, Dict[str, Any]] = {
    tt.TRANSCRIBE: {"allow_media": True, "requires_media": True, "category": "pipeline"},
    tt.SEGMENT: {"allow_media": False, "requires_media": False, "category": "pipeline"},
    tt.CAPTION: {"allow_media": False, "requires_media": False, "category": "pipeline"},
    tt.UTILITY_PING: {"allow_media": False, "requires_media": False, "category": "utility"},
    tt.UTILITY_ECHO: {"allow_media": False, "requires_media": False, "category": "utility"},
}
