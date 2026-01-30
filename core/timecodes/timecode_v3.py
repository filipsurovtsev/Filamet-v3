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
def _seconds_to_srt_time(value: float) -> str:
    total_ms = int(round(float(value) * 1000))
    if total_ms < 0:
        total_ms = 0
    h, rem = divmod(total_ms, 3600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def timecode_to_srt(timecode: dict) -> tuple[str, str]:
    start = float(timecode.get("start", 0.0))
    end = float(timecode.get("end", 0.0))
    if end < start:
        end = start
    return _seconds_to_srt_time(start), _seconds_to_srt_time(end)
