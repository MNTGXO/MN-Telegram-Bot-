import os

API_ID = int(os.getenv("API_ID", 12345))
API_HASH = os.getenv("API_HASH", "your_api_hash_here")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")
OWNER_ID = int(os.getenv("OWNER_ID", 123456789))
MONGO_URI = os.getenv("MONGO_URI", "")
