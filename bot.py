from pyrogram import Client, filters
from pyrogram.types import Message

# # ====== REQUIRED DETAILS ======
API_ID =34028673          # yahan apna API_ID
API_HASH =5bb0ce0f6b1c36c09a944e08ba9d4c68   # yahan apna API_HASH
BOT_TOKEN =AAFdVYd0ffngIe23IU9NGTWo5Ry4yv5ANKU # BotFather se mila token
# ==============================

app = Client(
    "kaju_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_cmd(client, message: Message):
    await message.reply_text(
        "🎵 Kaju Music Bot is alive!\n\nSend /start to check."
    )

print("Bot is running...")
app.run()
