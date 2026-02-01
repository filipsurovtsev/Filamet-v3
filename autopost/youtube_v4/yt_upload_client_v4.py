import os
import requests
from autopost.youtube_v4.yt_refresh_client_v4 import YTRefreshClientV4

UPLOAD_URL = "https://www.googleapis.com/upload/youtube/v3/videos"

class YTUploadClientV4:
    def __init__(self):
        self.refresh = YTRefreshClientV4()

    def upload_video(self, video_path, title, description, tags=None, privacy="unlisted"):
        # 1. refresh token → get access token
        ref = self.refresh.refresh_token()
        if not ref.get("ok"):
            return {"ok": False, "step": "refresh_failed", "error": ref}

        access_token = ref["access_token"]

        # 2. metadata
        metadata = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags or []
            },
            "status": {
                "privacyStatus": privacy
            }
        }

        # 3. open video
        with open(video_path, "rb") as f:
            video_data = f.read()

        # 4. upload request
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/octet-stream"
        }

        params = {
            "uploadType": "multipart",
            "part": "snippet,status"
        }

        # Multipart: metadata + video
        boundary = "filamet_v4_boundary"
        sep = f"--{boundary}"
        end = f"--{boundary}--"

        body = (
            f"{sep}\r\n"
            "Content-Type: application/json; charset=UTF-8\r\n\r\n"
            f"{metadata}\r\n"
            f"{sep}\r\n"
            "Content-Type: video/mp4\r\n\r\n"
        ).encode("utf-8") + video_data + f"\r\n{end}\r\n".encode("utf-8")

        headers["Content-Type"] = f"multipart/related; boundary={boundary}"

        resp = requests.post(UPLOAD_URL, headers=headers, params=params, data=body)

        try:
            data = resp.json()
        except:
            data = {"raw": resp.text}

        if resp.status_code in (200, 201):
            return {"ok": True, "response": data}

        return {"ok": False, "status": resp.status_code, "response": data}
