# functions/main_functions.py
from pyrogram import Client, filters
from config.vars import OWNER_ID
from config.dbvars import users_db

async def add_user(user_id):
    if isinstance(users_db, dict):
        users_db["users"].add(user_id)
    else:
        await users_db.update_one(
            {"user_id": user_id},
            {"$set": {"user_id": user_id}},
            upsert=True
        )

async def get_users():
    if isinstance(users_db, dict):
        return list(users_db["users"])
    else:
        return [user["user_id"] async for user in users_db.find({})]

async def broadcast_message(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply("Only the owner can use this command!")
        return

    users = await get_users()
    if not users:
        await message.reply("No users to broadcast to!")
        return

    reply = message.reply_to_message
    if not reply:
        await message.reply("Reply to a message to broadcast it!")
        return

    success = 0
    failed = 0
    for user_id in users:
        try:
            await reply.copy(user_id)
            success += 1
        except Exception as e:
            print(f"Failed to send to {user_id}: {e}")
            failed += 1

    await message.reply(f"Broadcast complete!\nSuccess: {success}\nFailed: {failed}")
