# functions/other_functions.py
from pyrogram import filters
from config.vars import OWNER_ID

owner_filter = filters.user(OWNER_ID)

def parse_command(text):
    if " " in text:
        cmd, args = text.split(" ", 1)
        return cmd.lower(), args
    return text.lower(), ""
