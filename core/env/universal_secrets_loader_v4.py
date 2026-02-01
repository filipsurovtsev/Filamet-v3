import os

class SecretsV4:
    def __init__(self):
        self._env = {
            "tg": {
                "token": os.getenv("TG_API_TOKEN_V4"),
                "channel": os.getenv("TG_CHANNEL_ID_V4"),
            },
            "vk": {
                "token": os.getenv("VK_API_TOKEN_V4"),
                "group": os.getenv("VK_GROUP_ID_V4"),
            },
            "yt": {
                "api_key": os.getenv("YT_API_KEY_V4"),
                "client_id": os.getenv("YT_CLIENT_ID_V4"),
                "client_secret": os.getenv("YT_CLIENT_SECRET_V4"),
                "refresh_token": os.getenv("YT_REFRESH_TOKEN_V4"),
            },
            "ok": {
                "api_key": os.getenv("OK_API_KEY_V4"),
                "access": os.getenv("OK_ACCESS_TOKEN_V4"),
                "group": os.getenv("OK_GROUP_ID_V4"),
            },
            "rutube": {
                "token": os.getenv("RUTUBE_API_TOKEN_V4"),
                "channel": os.getenv("RUTUBE_CHANNEL_ID_V4"),
            },
            "system": {
                "env": os.getenv("FILAMET_ENV"),
                "version": os.getenv("FILAMET_VERSION"),
            }
        }

    def get(self, service: str, key: str):
        return self._env.get(service, {}).get(key)

    def get_service(self, service: str):
        return self._env.get(service, {})

    def all(self):
        return self._env
