from core.pipeline.timing.timecode_v3_strict import validate_timecode

def validate_timing_entry(entry: dict):
    if not isinstance(entry, dict):
        return False, "entry must be dict"
    req = ["index", "caption_id", "time", "meta"]
    if set(entry.keys()) != set(req):
        return False, "timing entry keys mismatch"
    if not isinstance(entry["index"], int):
        return False, "index must be int"
    if not isinstance(entry["caption_id"], str):
        return False, "caption_id must be str"
    ok, err = validate_timecode(entry["time"])
    if not ok: return False, "invalid timecode: " + err
    meta = entry["meta"]
    if not isinstance(meta, dict): return False, "meta must be dict"
    if set(meta.keys()) != {"source_caption_id"}:
        return False, "meta keys mismatch"
    if not isinstance(meta["source_caption_id"], str):
        return False, "source_caption_id must be str"
    return True, None
