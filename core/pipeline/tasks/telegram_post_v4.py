import os
from autopost.telegram_v4.sender_real_v4 import TelegramSenderRealV4

class TelegramPostTaskV4:
    def __init__(self, store):
        self.store = store
        self.token = os.getenv("TG_API_TOKEN_V4")
        self.chat_id = os.getenv("TG_CHAT_ID_V4")

    def run(self, job_id: str, payload: dict):
        if not self.token or not self.chat_id:
            return {
                "status": "failed",
                "error": "Missing TG_API_TOKEN_V4 or TG_CHAT_ID_V4"
            }

        text = payload.get("text", "")
        photo = payload.get("photo")

        sender = TelegramSenderRealV4(self.token, self.chat_id)

        if photo:
            res = sender.send_photo(photo, caption=text)
        else:
            res = sender.send_text(text)

        job = self.store.get(job_id)
        job["output"]["telegram_post_v4"] = res
        if not res.get("ok"):
            job["status"] = "failed"
            return {"status": "failed", "result": res}

        job["status"] = "done"
        return {"status": "done", "result": res}
