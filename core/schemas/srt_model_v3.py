import re
from typing import List, Dict, Any

_TIME_RE = re.compile(r"^\d{2}:\d{2}:\d{2},\d{3}$")

class SrtSchemaError(ValueError):
    pass

def _validate_srt_record(record: Dict[str, Any], expected_index: int) -> None:
    required = {"index", "start", "end", "text"}
    if set(record.keys()) != required:
        raise SrtSchemaError("invalid keys")
    if not isinstance(record["index"], int):
        raise SrtSchemaError("index must be int")
    if record["index"] != expected_index:
        raise SrtSchemaError("index sequence broken")
    if not isinstance(record["start"], str) or not _TIME_RE.match(record["start"]):
        raise SrtSchemaError("invalid start")
    if not isinstance(record["end"], str) or not _TIME_RE.match(record["end"]):
        raise SrtSchemaError("invalid end")
    if not isinstance(record["text"], str) or not record["text"].strip():
        raise SrtSchemaError("text empty")

def validate_srt_schema(records: List[Dict[str, Any]]) -> None:
    if not isinstance(records, list):
        raise SrtSchemaError("payload must be list")
    for expected, rec in enumerate(records):
        if not isinstance(rec, dict):
            raise SrtSchemaError("record must be dict")
        _validate_srt_record(rec, expected)
