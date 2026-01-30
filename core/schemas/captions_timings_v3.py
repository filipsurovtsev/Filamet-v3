REQUIRED_FIELDS = {"caption_id", "index", "time", "meta"}
META_REQUIRED = {"source_caption_id"}

from core.timecodes.timecode_v3 import validate_timecode

def validate_timings_schema(timings: list[dict]) -> tuple[bool, str]:
    if not isinstance(timings, list):
        return False, "timings must be a list"

    seen = set()
    expected = 0

    for t in timings:
        if not isinstance(t, dict):
            return False, "each timing must be dict"
        if set(t.keys()) != REQUIRED_FIELDS:
            return False, f"invalid timing keys: {t.keys()}"

        cid = t["caption_id"]
        if not isinstance(cid, str):
            return False, "caption_id must be str"
        if cid in seen:
            return False, "caption_id must be unique"
        seen.add(cid)

        idx = t["index"]
        if not isinstance(idx, int):
            return False, "index must be int"
        if idx != expected:
            return False, f"index sequence broken at {idx}, expected {expected}"
        expected += 1

        tc = t["time"]
        ok, msg = validate_timecode(tc)
        if not ok:
            return False, f"timecode invalid: {msg}"

        meta = t["meta"]
        if not isinstance(meta, dict):
            return False, "meta must be dict"
        if set(meta.keys()) != META_REQUIRED:
            return False, f"invalid meta keys: {meta.keys()}"
        if not isinstance(meta["source_caption_id"], str):
            return False, "source_caption_id must be str"

    return True, "OK"
