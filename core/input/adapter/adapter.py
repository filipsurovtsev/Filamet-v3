def adapt_user_input_to_task_input(data):
    return {
        "job_id": data["job_id"],
        "task_type": data["task_type"],
        "payload": data["payload"]
    }
