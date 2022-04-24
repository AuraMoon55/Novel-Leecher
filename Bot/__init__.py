from pyrogram import Client
from os import getenv
from dotenv import load_dotenv

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

