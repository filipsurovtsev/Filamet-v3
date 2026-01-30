def validate_segment(item):
    if not isinstance(item, dict):
        raise ValueError("Segment must be dict")
    required = ["id", "index", "text", "meta"]
    for r in required:
        if r not in item:
            raise ValueError(f"Missing field {r}")
    if not isinstance(item["id"], str):
        raise ValueError("id must be str")
    if not isinstance(item["index"], int):
        raise ValueError("index must be int")
    if not isinstance(item["text"], str):
        raise ValueError("text must be str")
    if not isinstance(item["meta"], dict):
        raise ValueError("meta must be dict")
    if "length" not in item["meta"] or not isinstance(item["meta"]["length"], int):
        raise ValueError("Invalid meta.length")
    return True

def validate_segments_schema(data):
    if not isinstance(data, list):
        raise ValueError("Segments must be list")
    ids = set()
    for i, seg in enumerate(data):
        validate_segment(seg)
        if seg["index"] != i:
            raise ValueError("Indices must be sequential")
        if seg["id"] in ids:
            raise ValueError("Duplicate segment id")
        ids.add(seg["id"])
    return True
