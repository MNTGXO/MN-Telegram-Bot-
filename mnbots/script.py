# mnbots/script.py
from pyrogram import Client
from config.vars import API_ID, API_HASH, BOT_TOKEN
from mnbots.commands import register_commands

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_commands(app)
