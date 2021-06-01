from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("")
    await message.reply_text(
        f"""Hai 👋🏻, I am Rams music 🎼

I can play music in your group's voice call. Developed by [rama](https://t.me/gksukaribett).

Add me to your group and play music freely!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎛 Commands", url="https://telegra.ph/PANDUAN-RAMS-MUSIC-BOT-06-01")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/wavyheartt"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/calonpenyanyi"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "📌 Owner", url="https://t.me/gksukaribett"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Rams Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/calonpenyanyi")
                ]
            ]
        )
   )


