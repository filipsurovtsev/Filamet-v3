def validate_probe_schema(data):
    if not isinstance(data, dict):
        raise ValueError("Probe schema: root must be dict")

    if "duration" not in data or not isinstance(data["duration"], (int, float)) or data["duration"] < 0:
        raise ValueError("Invalid duration")

    if "streams" not in data or not isinstance(data["streams"], dict):
        raise ValueError("Invalid streams block")

    vs = data["streams"].get("video")
    if not isinstance(vs, dict):
        raise ValueError("Invalid video stream")

    for k in ["codec", "width", "height", "fps"]:
        if k not in vs:
            raise ValueError("Invalid video stream schema")

    if not isinstance(vs["codec"], str):
        raise ValueError("Invalid video codec")
    if not isinstance(vs["width"], int):
        raise ValueError("Invalid video width")
    if not isinstance(vs["height"], int):
        raise ValueError("Invalid video height")
    if not isinstance(vs["fps"], (int, float)):
        raise ValueError("Invalid video fps")

    as_ = data["streams"].get("audio")
    if not isinstance(as_, dict):
        raise ValueError("Invalid audio stream")
    if "codec" not in as_ or not isinstance(as_["codec"], str):
        raise ValueError("Invalid audio codec")

    if "container" not in data or not isinstance(data["container"], str):
        raise ValueError("Invalid container")

    return True
