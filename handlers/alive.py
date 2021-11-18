# https://t.me/LegendRajOp

from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(command(["start", f"start@DevilTrishaRoBot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/af3dad3866909b93b036b.png",
        caption=f"""
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Jøɩɳ Ɦɘɤɘ & Sʋƥƥøɤʈ 💞", url=f"https://t.me/JaiHindChatting")
                ]
            ]
        ),
    )


@Client.on_message(command(["help", f"help@DevilTrishaRoBot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/af3dad3866909b93b036b.png",
        caption=f"""
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Ƈɭɩƈƙ Ɦɘɤɘ Føɤ Ɦɘɭƥ 💞", url=f"https://t.me/JaiHindChatting")
                ]
            ]
        ),
    )
