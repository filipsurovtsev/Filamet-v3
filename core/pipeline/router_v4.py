def route_job(job):
    """
    Минимальный V4 router для задач Telegram.
    Позволяет выполнять задачи вида:
    { "type": "TELEGRAM_POST_V4", "payload": {...} }
    """
    job_type = job.get("type")

    # Telegram V4 task
    if job_type == "TELEGRAM_POST_V4":
        from core.pipeline.tasks.telegram_post_v4 import run_telegram_post_v4
        return run_telegram_post_v4(job.get("payload", {}))

    return {"status": "error", "error": "unknown_job_type_v4"}
