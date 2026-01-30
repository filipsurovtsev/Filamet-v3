from core.input.schemas.base import BASE_INPUT_SCHEMA
from core.input.schemas.task_payload import TASK_PAYLOAD_SCHEMAS
from core.input.validator.media_validator import validate_media_block

def validate_base(input_data):
    if not isinstance(input_data, dict): return False
    for key, t in BASE_INPUT_SCHEMA.items():
        if key not in input_data: return False
        if not isinstance(input_data[key], t): return False
    return True

def validate_payload(task_type, payload):
    schema = TASK_PAYLOAD_SCHEMAS.get(task_type)
    if not schema: return False
    for r in schema["required"]:
        if r not in payload: return False
    for k in payload.keys():
        if k not in schema["required"] and k not in schema["optional"]:
            return False
    media_block = payload.get("media")
    if not validate_media_block(media_block):
        return False
    return True

def validate_input(data):
    if not validate_base(data): return False
    t = data.get("task_type")
    p = data.get("payload", {})
    return validate_payload(t, p)
