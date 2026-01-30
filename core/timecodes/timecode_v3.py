def make_timecode(start, end):
    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise ValueError("start/end must be numbers")
    if start < 0 or end < start:
        raise ValueError("invalid start/end values")
    return {
        "start": float(start),
        "end": float(end),
        "duration": float(end) - float(start),
    }

def validate_timecode(tc):
    if not isinstance(tc, dict):
        raise ValueError("timecode must be dict")
    for key in ("start", "end", "duration"):
        if key not in tc:
            raise ValueError(f"missing '{key}' in timecode")
        if not isinstance(tc[key], (int, float)):
            raise ValueError(f"timecode field '{key}' must be number")
    if tc["start"] < 0:
        raise ValueError("timecode start must be >= 0")
    if tc["end"] < tc["start"]:
        raise ValueError("timecode end must be >= start")
    if abs((tc["end"] - tc["start"]) - tc["duration"]) > 1e-3:
        raise ValueError("timecode duration mismatch")

def _seconds_to_srt_timestamp(seconds):
    total_ms = int(round(seconds * 1000))
    if total_ms < 0:
        total_ms = 0
    hours = total_ms // 3600000
    remaining = total_ms % 3600000
    minutes = remaining // 60000
    remaining = remaining % 60000
    secs = remaining // 1000
    ms = remaining % 1000
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"

def timecode_to_srt(tc):
    validate_timecode(tc)
    start = _seconds_to_srt_timestamp(tc["start"])
    end = _seconds_to_srt_timestamp(tc["end"])
    return start, end

def _seconds_to_ass_timestamp(seconds):
    total_cs = int(round(seconds * 100))
    if total_cs < 0:
        total_cs = 0
    hours = total_cs // 360000
    remaining = total_cs % 360000
    minutes = remaining // 6000
    remaining = remaining % 6000
    secs = remaining // 100
    cs = remaining % 100
    return f"{hours:d}:{minutes:02d}:{secs:02d}.{cs:02d}"

def timecode_to_ass(tc):
    validate_timecode(tc)
    start = _seconds_to_ass_timestamp(tc["start"])
    end = _seconds_to_ass_timestamp(tc["end"])
    return start, end
