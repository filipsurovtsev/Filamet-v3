def validate_caption(item):
    if not isinstance(item, dict):
        raise ValueError("Caption must be dict")

    required = ["id", "index", "text", "meta"]
    for r in required:
        if r not in item:
            raise ValueError(f"Missing field {r}")

    if not isinstance(item["id"], str):
        raise ValueError("id must be str")

    if not isinstance(item["index"], int):
        raise ValueError("index must be int")

    if not isinstance(item["text"], str) or not item["text"].strip():
        raise ValueError("text must be non-empty str")

    if not isinstance(item["meta"], dict):
        raise ValueError("meta must be dict")

    if "length" not in item["meta"] or not isinstance(item["meta"]["length"], int):
        raise ValueError("Invalid meta.length")

    if "source_segment_id" not in item["meta"] or not isinstance(item["meta"]["source_segment_id"], str):
        raise ValueError("Invalid meta.source_segment_id")

    return True


def validate_captions_schema(data):
    if not isinstance(data, list):
        raise ValueError("Captions must be list")

    ids = set()

    for i, cap in enumerate(data):
        validate_caption(cap)

        if cap["index"] != i:
            raise ValueError("Indices must be sequential")

        if cap["id"] in ids:
            raise ValueError("Duplicate caption id")
        ids.add(cap["id"])

    return True
