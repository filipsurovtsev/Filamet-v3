REQUIRED_FIELDS = {"caption_id", "index", "text", "meta"}
META_REQUIRED = {"length", "source_segment_id"}

def validate_captions_schema(captions: list[dict]) -> tuple[bool, str]:
    if not isinstance(captions, list):
        return False, "captions must be a list"

    seen_ids = set()
    expected_index = 0

    for cap in captions:
        if not isinstance(cap, dict):
            return False, "each caption must be dict"

        keys = set(cap.keys())
        if keys != REQUIRED_FIELDS:
            return False, f"invalid caption keys: {keys}"

        cid = cap.get("caption_id")
        if not isinstance(cid, str):
            return False, "caption_id must be str"
        if cid in seen_ids:
            return False, "caption_id must be unique"
        seen_ids.add(cid)

        idx = cap.get("index")
        if not isinstance(idx, int):
            return False, "index must be int"
        if idx != expected_index:
            return False, f"index sequence broken at {idx}, expected {expected_index}"
        expected_index += 1

        text = cap.get("text")
        if not isinstance(text, str) or len(text.strip()) == 0:
            return False, "text must be non-empty str"

        meta = cap.get("meta")
        if not isinstance(meta, dict):
            return False, "meta must be dict"

        mkeys = set(meta.keys())
        if mkeys != META_REQUIRED:
            return False, f"invalid meta keys: {mkeys}"

        if not isinstance(meta["length"], int) or meta["length"] < 0:
            return False, "meta.length must be non-negative int"

        if not isinstance(meta["source_segment_id"], str):
            return False, "meta.source_segment_id must be str"

    return True, "OK"
