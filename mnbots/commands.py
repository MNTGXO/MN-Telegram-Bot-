# mnbots/commands.py
from pyrogram import filters
from functions.main_functions import add_user, broadcast_message
from functions.other_functions import owner_filter

def register_commands(app):
    @app.on_message(filters.command("start"))
    async def start(client, message):
        await add_user(message.from_user.id)
        await message.reply("Hello! Thanks for starting me.")

    @app.on_message(filters.command("broadcast") & owner_filter)
    async def broadcast(client, message):
        await broadcast_message(client, message)

    @app.on_message(filters.command("stats") & owner_filter)
    async def stats(client, message):
        users = await get_users()
        await message.reply(f"Total users: {len(users)}")
