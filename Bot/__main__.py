from Bot import app, OWNER
from .utils import Nocturnetls
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@app.on_message(filters.command("start") & filters.user(OWNER))
async def start(_, message):
  await message.reply_text("Im Alive")

@app.on_message(filters.command("novel") & filters.user(OWNER))
async def novel(_, message):
  query = message.text.split(" ", maxsplit=1)[1]
  if query:
    sex = Nocturnetls(query)
    novel = sex.get_novel()
    await message.reply_photo(
      photo=novel['cover'],
      caption=novel['name'],
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton(
              text="Go To Novel",
              url=novel['file']
            )
          ]
        ]
      )
    )
  else:
    await message.reply_text("Give url to chapter of Novel")

if __name__ == "__main__":
  app.run()