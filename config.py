import re from os
import getenv from dotenv import load_dotenv from pyrogram import filters

load_dotenv()

---------------- REQUIRED VALUES ----------------

API_ID = 24736076 API_HASH = "22fc694d8b2b4ded4350e3fe25807976" OWNER_ID = 7648822500

-------------------------------------------------

BOT_TOKEN = getenv("BOT_TOKEN", "7593167374:AAFhIpz4XRiW1TEQPX3t8WkG2hgpgJPBiKM") MONGO_DB_URI = getenv("MONGO_DB_URI", "music8890@cluster0.3d2hk.mongodb.net")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60)) LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME",music  bot ) HEROKU_API_KEY = getenv("HEROKU_API_KEY", HRKU-AASPwj_e-UxMsoC_B0IjrBrTfyI-kwThSQK3cF5VQq3A_wifkcHiep43)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/rishabhops/alice") UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main") GIT_TOKEN = getenv("GIT_TOKEN", None)

✅ Updated Support Links

SUPPORT_CHANNEL = "https://t.me/tufan_890" SUPPORT_GROUP = "https://t.me/Hindi_890"

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None) SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25)) TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600)) TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

STRING1 = getenv("STRING_SESSION", "STRING_SESSION_1") STRING2 = getenv("STRING_SESSION2", None) STRING3 = getenv("STRING_SESSION3", None) STRING4 = getenv("STRING_SESSION4", None) STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user() adminlist = {} lyrical = {} votemode = {} autoclean = [] confirmer = {}

---- Image URL replaced everywhere with the user-provided image ----

IMG_URL = "https://graph.org/file/bbc2fcdd0b3313a22be8e-fcec0333b7552f5906.jpg"

START_IMG_URL = "https://graph.org/file/bbc2fcdd0b3313a22be8e-fcec0333b7552f5906.jpg" PING_IMG_URL = "https://graph.org/file/bbc2fcdd0b3313a22be8e-fcec0333b7552f5906.jpg" PLAYLIST_IMG_URL = "https://graph.org/file/bbc2fcdd0b3313a22be8e-fcec0333b7552f5906.jpg   " STATS_IMG_URL = "https://graph.org/file/bbc2fcdd0b3313a22be8e-fcec0333b7552f5906.jpg  " TELEGRAM_AUDIO_URL = "https://graph.org/file/bbc2fcdd0b3313a22be8e-fcec0333b7552f5906.jpg" TELEGRAM_VIDEO_URL =  "https://graph.org/file/bbc2fcdd0b3313a22be8e-fcec0333b7552f5906.jpg" STREAM_IMG_URL = IMG_URL SOUNCLOUD_IMG_URL = IMG_URL YOUTUBE_IMG_URL = IMG_URL SPOTIFY_ARTIST_IMG_URL = IMG_URL SPOTIFY_ALBUM_IMG_URL = IMG_URL SPOTIFY_PLAYLIST_IMG_URL = IMG_URL

---------------------------------------------------------------------

def time_to_seconds(time_str: str) -> int: parts = [int(x) for x in str(time_str).split(":")] parts.reverse() return sum(p * (60 ** i) for i, p in enumerate(parts))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL and not re.match(r"^(?:http|https)://", SUPPORT_CHANNEL): raise SystemExit("[ERROR] - SUPPORT_CHANNEL must start with http:// or https://")

if SUPPORT_GROUP and not re.match(r"^(?:http|https)://", SUPPORT_GROUP): raise SystemExit("[ERROR] - SUPPORT_GROUP must start with http:// or https://")
