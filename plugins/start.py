from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Kanal", url="https://t.me/elisbots")],
        [InlineKeyboardButton(
            "Problemlə bağlı 😊", url="https://t.me/abbasov1o")]
    ])
    welcomed = f"Salam <b>{message.from_user.first_name}</b>\nKömək üçün /help yazın!"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
