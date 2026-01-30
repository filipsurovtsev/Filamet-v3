import json
import os
from core.viz.style_schema_v3 import validate_style_schema
from core.viz.layout_schema_v3 import validate_layout_schema

class VizContext:
    def __init__(self, style_name="Default", layout="1080x1920"):
        self.style_name = style_name
        self.layout_name = layout
        self.styleset = {}
        self.layout = {}
        self.load_styles()
        self.load_layout()

    def load_styles(self):
        path = os.path.join("core", "viz", "stylesets", "default_v3.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if self.style_name not in data:
            raise ValueError("style not found")
        style = data[self.style_name]
        validate_style_schema(style)
        self.styleset = style

    def load_layout(self):
        layout = {
            "resolution": self.layout_name,
            "safe_zone": {"left": 50, "right": 50, "top": 50, "bottom": 50},
            "alignment": "center"
        }
        validate_layout_schema(layout)
        self.layout = layout
