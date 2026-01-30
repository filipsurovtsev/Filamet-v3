def validate_layout_schema(layout):
    required = {"resolution", "safe_zone", "alignment"}
    if not isinstance(layout, dict):
        raise ValueError("layout must be dict")
    if set(layout.keys()) != required:
        raise ValueError("invalid layout keys")
    if not isinstance(layout["resolution"], str) or "x" not in layout["resolution"]:
        raise ValueError("invalid resolution format")
    sz = layout["safe_zone"]
    if not isinstance(sz, dict):
        raise ValueError("safe_zone must be dict")
    for k in ("left", "right", "top", "bottom"):
        if k not in sz or not isinstance(sz[k], int):
            raise ValueError("safe_zone fields must be int")
    if not isinstance(layout["alignment"], str):
        raise ValueError("alignment must be str")
