import uuid

REQUIRED_FIELDS = {"segment_id", "index", "text", "meta"}
META_REQUIRED = {"length", "lang", "source"}


def validate_segments_schema(segments: list[dict]) -> tuple[bool, str]:
    if not isinstance(segments, list):
        return False, "segments must be a list"

    seen_ids = set()
    expected_index = 0

    for seg in segments:
        if not isinstance(seg, dict):
            return False, "each segment must be dict"

        keys = set(seg.keys())
        if keys != REQUIRED_FIELDS:
            return False, f"segment has invalid keys: {keys}"

        # segment_id
        sid = seg.get("segment_id")
        if not isinstance(sid, str):
            return False, "segment_id must be str"
        if sid in seen_ids:
            return False, "segment_id must be unique"
        seen_ids.add(sid)

        # index
        idx = seg.get("index")
        if not isinstance(idx, int):
            return False, "index must be int"
        if idx != expected_index:
            return False, f"index sequence broken at {idx}, expected {expected_index}"
        expected_index += 1

        # text
        if not isinstance(seg.get("text"), str):
            return False, "text must be str"
        if len(seg["text"].strip()) == 0:
            return False, "text cannot be empty"

        # meta
        meta = seg.get("meta")
        if not isinstance(meta, dict):
            return False, "meta must be dict"

        mkeys = set(meta.keys())
        if mkeys != META_REQUIRED:
            return False, f"invalid meta keys: {mkeys}"

        if not isinstance(meta["length"], int) or meta["length"] < 0:
            return False, "meta.length must be non-negative int"

        if meta["lang"] is not None and not isinstance(meta["lang"], str):
            return False, "meta.lang must be str or None"

        if not isinstance(meta["source"], str):
            return False, "meta.source must be str"

    return True, "OK"
