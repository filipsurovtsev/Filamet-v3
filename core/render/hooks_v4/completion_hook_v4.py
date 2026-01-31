import os, json, datetime

def run_completion_hook(job_id, session_path):
    os.makedirs(os.path.dirname(session_path), exist_ok=True)

    # Если нет сессии — создаём пустую
    if not os.path.exists(session_path):
        data = {
            "job_id": job_id,
            "created_at": datetime.datetime.utcnow().isoformat() + "Z",
            "status": "created_by_hook_fallback"
        }
        with open(session_path, "w") as f:
            json.dump(data, f, indent=2)
        return data

    # Если есть — обновляем
    with open(session_path, "r") as f:
        data = json.load(f)

    data["hook_timestamp"] = datetime.datetime.utcnow().isoformat() + "Z"

    with open(session_path, "w") as f:
        json.dump(data, f, indent=2)

    return data
