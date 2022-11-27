# # (c) @AbirHasan2005


import os

from dotenv import load_dotenv
load_dotenv()

class Config(object):
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
    OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
    ABOUT_BOT_TEXT = f"""Nothing"""
	ABOUT_DEV_TEXT = f"""
**🌐 This Bot Was Devloped By** : @A2z_tech"""
	HOME_TEXT = """
Hello [{}](tg://user?id={})✋\n\n☁️ This Is A Unlimited Telegram Could Storage Bot For shorturllink.in. Send Me Any File And Select Method Wait Few Seconds Bot Will Be Upload To Our Server And Genarate shorturllink.in Link For Files. ⚡\n\nCurrently Supported Format :\n\n⟴ File 📁\n⟴ Video 🎥\n⟴ Photo 🖼️\n⟴ Audio 🎙️\n\nMore Format Soon ⚡\n\nNote : 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗔𝗟𝗦𝗢 𝗨𝗣𝗟𝗢𝗔𝗗 𝟰𝗚𝗕 𝗙𝗜𝗟𝗘𝗦 📥"""
	SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, `/apikey api`
            
Ex: `/apikey 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

