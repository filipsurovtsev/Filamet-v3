import os
from dotenv import load_dotenv

# Load .env if exists
load_dotenv()

class SecretsLoader:
    def __init__(self):
        self.cache = {}
        self._load_all()

    def _load_all(self):
        for key, value in os.environ.items():
            if any(t in key.lower() for t in [
                "token",
                "secret",
                "client",
                "api",
                "key"
            ]):
                self.cache[key] = value

    def get(self, key, default=None):
        return self.cache.get(key, default)

    def require(self, key):
        v = self.get(key)
        if not v:
            raise ValueError(f"Missing required secret: {key}")
        return v

secrets = SecretsLoader()
