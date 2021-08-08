from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Youtube video və mahnıları rahatlıqla yükləyə biləcəyiniz bot"
    await message.reply_text(helptxt)
