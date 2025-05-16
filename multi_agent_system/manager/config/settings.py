# config/settings.py – Centralized App Configuration

import json
from pathlib import Path
import os

# Load secrets from secrets.json
SECRETS_PATH = Path(__file__).parent / "secrets.json"

with open(SECRETS_PATH, "r") as f:
    secrets = json.load(f)

# Access values
SERPAPI_API_KEY = secrets.get("SERPAPI_API_KEY")
GOOGLE_API_KEY = secrets.get("GOOGLE_API_KEY")
DEFAULT_MODEL = secrets.get("DEFAULT_MODEL")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY