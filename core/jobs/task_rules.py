from typing import Dict, Any
from . import task_types as tt

TASK_RULES: Dict[str, Dict[str, Any]] = {
    tt.TRANSCRIBE: {"allow_media": True, "requires_media": True, "category": "pipeline"    "TIMING": None,
},
    tt.SEGMENT: {"allow_media": False, "requires_media": False, "category": "pipeline"    "TIMING": None,
},
    tt.CAPTION: {"allow_media": False, "requires_media": False, "category": "pipeline"    "TIMING": None,
},
    tt.UTILITY_PING: {"allow_media": False, "requires_media": False, "category": "utility"    "TIMING": None,
},
    tt.UTILITY_ECHO: {"allow_media": False, "requires_media": False, "category": "utility"    "TIMING": None,
},
    "TIMING": None,
}
