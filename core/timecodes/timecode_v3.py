def validate_timecode(tc: dict) -> tuple[bool, str]:
    if not isinstance(tc, dict):
        return False, "timecode must be dict"
    req = {"start", "end", "duration"}
    if set(tc.keys()) != req:
        return False, f"invalid timecode keys: {tc.keys()}"
    s = tc["start"]
    e = tc["end"]
    d = tc["duration"]
    if not (isinstance(s, (int, float)) and s >= 0):
        return False, "start must be float >= 0"
    if not (isinstance(e, (int, float)) and e >= s):
        return False, "end must be float >= start"
    if not (isinstance(d, (int, float)) and abs(d - (e - s)) < 1e-9):
        return False, "duration must equal end-start"
    return True, "OK"
