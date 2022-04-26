from utils import Nocturnetls
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from os import getenv
from dotenv import load_dotenv

load_dotenv()


ID = 6328792 #getenv("ID")
HASH = "8c3600d42da9c66da7ef7ea4f9763a53" #getenv("HASH")
TOKEN = "5377908346:AAFU7rpT77UcDJBtUp8ov8CfDG6CquPx2k8" #getenv("TOKEN")
#OWNER = getenv("OWNER")

app = Client(
  "vot",
  api_id=ID,
  api_hash=HASH,
  bot_token=TOKEN
)


@app.on_message(filters.command("start"))
async def start(_, message):
  await message.reply_text("Im Alive")

@app.on_message(filters.command("novel"))
async def novel(_, message):
  query = message.text.split(" ", maxsplit=1)[1]
  if query:
    sex = Nocturnetls(query)
    novel = sex.get_novel()
    await message.reply_text(
      text=f"[{novel['name']}]({query})",
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton(
              text="Go To Novel",
              url=novel['uri']
            )
          ]
        ]
      ),
      disable_web_page_preview=True  
    )
  else:
    await message.reply_text("Give url to chapter of Novel")


app.run()
