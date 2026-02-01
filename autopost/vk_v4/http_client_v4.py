import requests

class VkHttpClientV4:
    def __init__(self, token: str):
        self.token = token
        self.base = "https://api.vk.com/method"

    def call(self, method: str, params: dict):
        params["access_token"] = self.token
        params["v"] = "5.199"
        try:
            r = requests.post(f"{self.base}/{method}", data=params, timeout=10)
            return r.json()
        except Exception as e:
            return {"ok": False, "error": str(e)}
