import os
from autopost.vk_v4.sender_v4 import VkSenderV4

class VkPostTaskV4:
    def __init__(self, store):
        self.store = store
        self.token = os.getenv("VK_API_TOKEN_V4")
        self.group_id = os.getenv("VK_GROUP_ID_V4")

    def run(self, job_id: str, payload: dict):
        if not self.token or not self.group_id:
            return {
                "status": "failed",
                "error": "Missing VK_API_TOKEN_V4 or VK_GROUP_ID_V4"
            }

        text = payload.get("text", "")
        sender = VkSenderV4(self.token, self.group_id)
        res = sender.send_text(text)

        job = self.store.get(job_id)
        job["output"]["vk_post_v4"] = res

        if "error" in res or ("error" in res.get("response", {})):
            job["status"] = "failed"
            return {"status": "failed", "result": res}

        job["status"] = "done"
        return {"status": "done", "result": res}
