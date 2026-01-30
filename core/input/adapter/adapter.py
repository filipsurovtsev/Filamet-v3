def adapt_user_input_to_task_input(data):
    payload = data["payload"]
    adapted = {
        "job_id": data["job_id"],
        "task_type": data["task_type"],
        "payload": {
            "media": payload.get("media"),
        }
    }
    for k, v in payload.items():
        if k != "media":
            adapted["payload"][k] = v
    return adapted
