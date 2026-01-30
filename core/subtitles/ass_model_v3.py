def validate_ass_schema(records):
    if not isinstance(records, list):
        raise ValueError("ASS records must be a list")
    expected_keys = {"index", "start", "end", "text"}
    seen_indexes = set()
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            raise ValueError("ASS record must be a dict")
        if set(rec.keys()) != expected_keys:
            raise ValueError(f"Invalid keys in ASS record: {rec.keys()}")
        index = rec.get("index")
        start = rec.get("start")
        end = rec.get("end")
        text = rec.get("text")
        if not isinstance(index, int):
            raise ValueError("index must be int")
        if index != i:
            raise ValueError("indexes must be continuous from 0..N-1")
        if index in seen_indexes:
            raise ValueError("duplicate index in ASS records")
        seen_indexes.add(index)
        if not isinstance(start, str) or not isinstance(end, str):
            raise ValueError("start and end must be strings")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text must be non-empty string")
