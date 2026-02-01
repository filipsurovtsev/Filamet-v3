import requests
import os

class YTRefreshClientV4:
    TOKEN_URL = "https://oauth2.googleapis.com/token"

    def __init__(self):
        self.client_id = os.getenv("YT_CLIENT_ID_V4")
        self.client_secret = os.getenv("YT_CLIENT_SECRET_V4")
        self.refresh = os.getenv("YT_REFRESH_TOKEN_V4")

    def refresh_token(self):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh,
            "grant_type": "refresh_token"
        }
        r = requests.post(self.TOKEN_URL, data=data)
        try:
            js = r.json()
        except:
            return {"ok": False, "error": "json_error", "raw": r.text}

        if "access_token" not in js:
            return {"ok": False, "error": js}

        return {"ok": True, "access_token": js["access_token"]}
