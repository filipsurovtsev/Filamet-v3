VALID_STATUSES = [
    "queued",
    "running",
    "done",
    "failed"
]

def ensure_status(value):
    if value not in VALID_STATUSES:
        raise ValueError(f"Invalid job status: {value}")
    return value
