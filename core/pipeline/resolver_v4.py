from core.pipeline.tasks.telegram_post_v4 import run_telegram_post_v4
from core.pipeline.tasks.vk_post_v4 import VkPostTaskV4

TYPE_MAP = {}

def register_all(store):
    TYPE_MAP["TELEGRAM_POST_V4"] = lambda job_id, payload: run_telegram_post_v4(payload)
    TYPE_MAP["VK_POST_V4"] = VkPostTaskV4(store)
    return TYPE_MAP
