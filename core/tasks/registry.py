TASK_TYPES = {
    "noop": {"allowed_status": ["PENDING", "RUNNING", "DONE", "FAILED"]},
    "bootstrap": {"allowed_status": ["PENDING", "RUNNING", "DONE", "FAILED"]},
    "healthcheck": {"allowed_status": ["PENDING", "RUNNING", "DONE", "FAILED"]},
    "UTILITY_PING": {"allowed_status": ["PENDING", "RUNNING", "DONE", "FAILED"]},
    "UTILITY_ECHO": {"allowed_status": ["PENDING", "RUNNING", "DONE", "FAILED"]}
}
