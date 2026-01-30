def validate_timecode(tc: dict):
    if not isinstance(tc, dict): return False, "timecode must be dict"
    req = ["start", "end", "duration"]
    if set(tc.keys()) != set(req):
        return False, "timecode keys mismatch"
    try:
        start = float(tc["start"])
        end = float(tc["end"])
        duration = float(tc["duration"])
    except Exception:
        return False, "timecode values must be float-castable"
    if start < 0: return False, "start < 0"
    if end < start: return False, "end < start"
    if abs((end - start) - duration) > 0.0001:
        return False, "duration mismatch"
    return True, None
