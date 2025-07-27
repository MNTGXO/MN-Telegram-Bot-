# config/dbvars.py
from config.vars import MONGO_URI

if MONGO_URI:
    from motor.motor_asyncio import AsyncIOMotorClient

    mongo = AsyncIOMotorClient(MONGO_URI)
    db = mongo.pyrogram_bot
    users_db = db.users
else:
    # Fallback to in-memory storage (will reset on restart)
    users_db = {"users": set()}
