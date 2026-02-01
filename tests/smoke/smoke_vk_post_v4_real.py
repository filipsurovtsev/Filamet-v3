from api.vk_v4.vk_api_v4 import handle_vk_post_v4

req = {
    "job_id": "vk_real_test",
    "payload": {
        "text": "🔥 REAL VK TEST (CLIPS) — Filamet V4"
    }
}

print("VK_REAL_SMOKE:", handle_vk_post_v4(req))
