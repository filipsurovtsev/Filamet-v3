from core.env.universal_secrets_loader_v4 import SecretsV4

s = SecretsV4()
print("YT_REFRESH_SMOKE:", {
    "client_id": s.get("yt", "client_id"),
    "client_secret": s.get("yt", "client_secret"),
    "refresh_token": bool(s.get("yt", "refresh_token"))
})
