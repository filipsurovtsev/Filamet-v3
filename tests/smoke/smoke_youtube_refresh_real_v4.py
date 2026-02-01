from autopost.youtube_v4.yt_refresh_client_v4 import YTRefreshClientV4

client = YTRefreshClientV4()
out = client.refresh_token()
print("YT_REFRESH_REAL_V4:", out)
