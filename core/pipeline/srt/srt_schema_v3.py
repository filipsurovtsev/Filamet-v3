def validate_srt_record(rec):
    if not isinstance(rec, dict):
        raise ValueError("SRT record must be dict")

    req = ["index", "start", "end", "text"]
    if set(rec.keys()) != set(req):
        raise ValueError("SRT record keys mismatch")

    if not isinstance(rec["index"], int):
        raise ValueError("index must be int")

    if not isinstance(rec["start"], str) or not rec["start"]:
        raise ValueError("start must be non-empty str")

    if not isinstance(rec["end"], str) or not rec["end"]:
        raise ValueError("end must be non-empty str")

    if not isinstance(rec["text"], str) or not rec["text"].strip():
        raise ValueError("text must be non-empty str")

    return True


def validate_srt_schema(data):
    if not isinstance(data, list):
        raise ValueError("SRT schema root must be list")

    for i, rec in enumerate(data):
        validate_srt_record(rec)
        if rec["index"] != i:
            raise ValueError("SRT index mismatch")

    return True
