from api.vk_v4.vk_api_v4 import handle_vk_post_v4

def run_smoke():
    req = {
        "job_id": "demo_vk_v4",
        "payload": {
            "text": "V4 VK pipeline test",
            "token": "VK_TOKEN_HERE",
            "group_id": "VK_GROUP_ID_HERE"
        }
    }
    return handle_vk_post_v4(req)

if __name__ == "__main__":
    print("VK_POST_V4_SMOKE_OK", run_smoke())
