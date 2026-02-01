from core.env.universal_secrets_loader_v4 import get
print("TG_API_TOKEN_V4:", bool(get("TG_API_TOKEN_V4")))
print("VK_API_TOKEN_V4:", bool(get("VK_API_TOKEN_V4")))
print("YT_API_KEY_V4:", bool(get("YT_API_KEY_V4")))
print("SECRETS_LOADER_V4_SMOKE_OK")
