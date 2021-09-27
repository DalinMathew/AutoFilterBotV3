# (c) PR0FESS0R-99

import datetime

from Config import DB_URL, SESSION
from Database import Database

db = Database(DB_URL, SESSION)


async def handle_user_status(bot, cmd):
    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"#NEWUSER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{BOT_USERNAME} !!",
        )

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
            datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("You are Banned to Use This Bot ", quote=True)
            return
    await cmd.continue_propagation()
