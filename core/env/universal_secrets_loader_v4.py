import os
from typing import Dict

PATH = "/Users/admin/.filamet_secrets/secrets.env"
CACHE: Dict[str, str] = {}


def _load_file() -> Dict[str, str]:
    data: Dict[str, str] = {}
    if not os.path.exists(PATH):
        return data
    with open(PATH, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            k, v = line.split("=", 1)
            data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def load() -> Dict[str, str]:
    global CACHE
    if not CACHE:
        CACHE = _load_file()
    return CACHE


def get(key: str, default: str = "") -> str:
    env_val = os.getenv(key)
    if env_val is not None and env_val != "":
        return env_val
    data = load()
    return data.get(key, default)
