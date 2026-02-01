from core.env.universal_secrets_loader_v4 import SecretsV4

s = SecretsV4()
print("UNIVERSAL_SECRETS_V4_SMOKE_OK", s.all())
