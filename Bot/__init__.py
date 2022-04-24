from pyrogram import Client
from os import getenv
from dotenv import load_dotenv

ID = getenv("ID")
HASH = getenv("HASH")
TOKEN = getenv("TOKEN")
OWNER = getenv("OWNER")

app = Client(
  "vot",
  api_id=ID,
  api_hash=HASH,
  bot_token=TOKEN
)

