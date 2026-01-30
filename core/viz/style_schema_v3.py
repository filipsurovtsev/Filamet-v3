def validate_style_schema(style):
    required = {
        "name", "font", "size", "color",
        "outline", "shadow", "alignment",
        "margin_v", "margin_h"
    }
    if not isinstance(style, dict):
        raise ValueError("style must be dict")
    if set(style.keys()) != required:
        raise ValueError("invalid style keys")
    if not isinstance(style["name"], str):
        raise ValueError("name must be str")
    if not isinstance(style["font"], str):
        raise ValueError("font must be str")
    if not isinstance(style["size"], int):
        raise ValueError("size must be int")
    if not isinstance(style["color"], str) or not style["color"].startswith("#") or len(style["color"]) != 7:
        raise ValueError("color must be '#RRGGBB'")
    if not isinstance(style["outline"], int):
        raise ValueError("outline must be int")
    if not isinstance(style["shadow"], int):
        raise ValueError("shadow must be int")
    if not isinstance(style["alignment"], str):
        raise ValueError("alignment must be str")
    if not isinstance(style["margin_v"], int):
        raise ValueError("margin_v must be int")
    if not isinstance(style["margin_h"], int):
        raise ValueError("margin_h must be int")
