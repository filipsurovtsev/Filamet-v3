from autopost.youtube_v4.yt_refresh_client_v4 import YTRefreshClientV4

client = YTRefreshClientV4()
token = client.refresh_token()

print("YT_UPLOAD_SMOKE_V4:", {
    "ok": token.get("ok"),
    "access_token_present": bool(token.get("access_token"))
})
