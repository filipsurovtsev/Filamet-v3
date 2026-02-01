from autopost.youtube_v4.yt_upload_client_v4 import YTUploadClientV4

client = YTUploadClientV4()
out = client.upload_video(
    video_path="tests/smoke/demo.mp4",
    title="Filamet V4 Upload Smoke",
    description="Real upload smoke test",
    tags=["filamet","v4","smoke"],
    privacy="unlisted"
)
print("YT_UPLOAD_REAL_V4:", out)
