from autopost.vk_v4.http_client_v4 import VkHttpClientV4

class VkSenderV4:
    def __init__(self, token: str, group_id: str):
        self.client = VkHttpClientV4(token)
        self.group_id = group_id

    def send_text(self, text: str):
        return self.client.call("wall.post", {
            "owner_id": f"-{self.group_id}",
            "message": text
        })
