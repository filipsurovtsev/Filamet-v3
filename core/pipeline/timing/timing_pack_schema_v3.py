from core.pipeline.timing.timing_entry_schema_v3 import validate_timing_entry

def validate_timing_pack(pack):
    if not isinstance(pack, list):
        return False, "pack must be list"
    if len(pack) == 0:
        return False, "empty pack"
    for i, entry in enumerate(pack):
        ok, err = validate_timing_entry(entry)
        if not ok: return False, f"entry[{i}] invalid: {err}"
    idxs = [e["index"] for e in pack]
    if idxs != list(range(len(pack))):
        return False, "index sequence mismatch"
    cids = [e["caption_id"] for e in pack]
    if len(cids) != len(set(cids)):
        return False, "duplicate caption_id"
    return True, None
